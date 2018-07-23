#!../venv/bin/python
import sys
import re
from bs4 import BeautifulSoup


def run():
    infile = sys.argv[1]
    contents = ''

    with open(infile) as _file:
        contents = _file.read()
    _file.close()

    htmls = re.findall(r'(HTML`([\s\S]*)`)', contents)

    for html in htmls:
        soup = BeautifulSoup(html[1], 'html.parser')
        lines = soup.prettify().split('\n')
        htmldef = '[{}]'\
            .format(
                ', '.join(['"' + line + '"' for line in lines if line])
            ) + '.join("")'

        contents = contents.replace(html[0], htmldef)

    print(contents)


run()
