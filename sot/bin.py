import sys
import os
from sot.Project import Project
from sot.Colors import Colors


def watch():
    path = os.path.join(os.getcwd(), sys.argv[1]) if sys.argv[1][0] != '/'\
        else sys.argv[1] if len(sys.argv) > 1 else os.getcwd()

    project = Project(path)

    if not project.config:
        print(
            '{}{}{}'.format(
                Colors.FAIL,
                'Could not find any sot.json file',
                Colors.ENDC
            )
        )

        return

    print(
        '{}{}{}'.format(
            Colors.OKGREEN,
            'SOT watchdog started',
            Colors.ENDC
        )
    )

    project.start_watcher()


def run():
    watch()
