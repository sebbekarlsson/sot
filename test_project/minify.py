#!../venv/bin/python
import sys
from jsmin import jsmin


def run():
    infile = sys.argv[1]
    indata = ''

    with open(infile) as _file:
        indata = _file.read()
    _file.close()

    print(jsmin(indata))


run()
