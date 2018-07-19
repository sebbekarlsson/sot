import sys
from sot.Project import Project


def watch():
    Project(sys.argv[1] if len(sys.argv) > 1 else '.').start_watcher()


def run():
    watch()
