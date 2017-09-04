from util import util


class User:
    def __init__(self, name, time, task):
        self.name = name
        self.time = time
        self.tasks = [task]

    def increment_time(self, time):
        self.time = self.time + time

    def add_task(self, task):
        self.tasks.append(task)

    def formatted_output(self):
        return self.name + " has spent " + util.format_time(self.time) + "while completing " + \
               str(len(self.tasks)) + " task" + ("s" if len(self.tasks) > 1 else "") + "."
