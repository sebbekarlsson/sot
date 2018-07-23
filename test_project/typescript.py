#!../venv/bin/python
import sys
import subprocess
import os


def run():
    fname = sys.argv[1]
    try:
        subprocess.check_output([
            '/usr/bin/tsc',
            fname.split('.')[0] + '.ts',
            '--outFile',
            '/tmp/typescript.tmp'
        ])
    except Exception:
        pass

    contents = ''

    contents_file = '/tmp/typescript.tmp'\
        if os.path.isfile('/tmp/typescript.tmp') else fname

    with open(contents_file) as _file:
        contents = _file.read()
    _file.close()

    print(contents)


run()
