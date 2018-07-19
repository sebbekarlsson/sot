#!../venv/bin/python
import sys
import re
from sot.Project import Project


def run():
    project = Project()
    indata = sys.argv[1]

    requires = re.findall(r'(require\((\'|\")(.*?)(\'|\")\))', indata)

    for req in requires:
        contents = ''

        with open(req[2]) as _file:
            contents = _file.read()
        _file.close()

        indata = indata.replace(req[0] + ';', project.transpile(out=contents))

    print(indata)


run()
