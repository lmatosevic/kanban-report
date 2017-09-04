from setuptools import setup
from setuptools import find_packages

desc = """\
Kanban report
==============

This command tool is used for extracting data from kaban-flow' web application for scrum management.
Input to this program is html report taken from kanaban-flow's print report page.
Output is generated to stdout with statistics about users and completed tasks with logged time.
"""

setup(name="kanban-report",
      version="1.0",
      author="luka",
      packages=find_packages(),
      install_requires=["lxml", "argparse"],
      entry_points={
          'console_scripts': [
              'kanban-report = main.main:main'
          ]
      },
      description="Kanban report generator tool",
      long_description=desc)
