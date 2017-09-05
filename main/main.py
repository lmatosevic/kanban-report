import argparse

from lxml import etree
from util import util
from model.user import User
from model.task import Task


class Main:
    def __init__(self):
        self.results = {}

    def run(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-f", "--file", help="Input html file with print report", required=True)
        parser.add_argument("-r", "--root", help="Root element in provided xml dom", required=False)
        args = parser.parse_args()

        file = open(args.file, mode="r", encoding="UTF-8")
        root = etree.HTML(file.read())

        last_task_name = ""
        last_user_name = ""

        for element in root.iter(args.root if args.root is not None else "ul"):
            if element.tag == "h3" and element.attrib["class"] == "task-name":
                last_task_name = element.text
            if element.attrib["class"] == "task-section task-smallProperties":
                for item in element.iter("li"):
                    label = item.find(".//div[@class='propertyLabel']").text
                    value = item.find(".//div[@class='propertyValue']").text
                    if label == "Responsible:":
                        last_user_name = value
                    if label == "Time spent:":
                        task_time = util.get_seconds(value)
                        task = Task(last_task_name, task_time)
                        user = User(last_user_name, task_time, task)
                        if self.results.get(user.name) is None:
                            self.results[user.name] = user
                        else:
                            existing_user = self.results.get(user.name)
                            existing_user.increment_time(task_time)
                            existing_user.add_task(task)

        total = 0
        for user in sorted(self.results.values(), key=lambda x: x.time, reverse=True):
            print(user.formatted_output())
            total += user.time

        print("\r\nTotal time: " + util.format_time(total))


def main():
    Main().run()

if __name__ == "__main__":
    main()
