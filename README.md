# Kanban Flow Report
>Python command tool which is used for extracting data from kaban-flow' web application for scrum management.

Input to this program is html report taken from kanaban-flow's print report page.
Output is generated to stdout with statistics about users and completed tasks with logged time.

## Installation
To install this command line tool, run following command using PIP Installs Python (pip):

`pip install kanban-report`

Or you can install module using only python. First, clone project using git:

`git clone https://gitlab.com/int-rev/kanban-report.git`

and then open terminal in newly downloaded folder and run following commnad:

`python setup.py install`

## Usage
Usage is very simple, just download html report from kanban-flow web app (Reports->Print) then copy and paste html content into file ond disk.

```
usage: kanban-report-script.py [-h] -f FILE [-r ROOT]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Input html file with print report
  -r ROOT, --root ROOT  Root element in provided xml dom
```

Example usage:

`kanban-report -f report.html --root body`