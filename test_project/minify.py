#!../venv/bin/python
import sys
from jsmin import jsmin


def run():
    print(jsmin(sys.argv[1]))


run()
