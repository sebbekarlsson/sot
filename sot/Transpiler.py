import subprocess
from sot.constants import TMP_TRANSPILED_FILE


class Transpiler(object):

    def __init__(self, path):
        self.path = path

    def send_filepath(self, filepath):
        return subprocess.check_output(
            [
                self.path,
                filepath
            ]
        )

    def send_contents(self, contents, ext=None):
        fname = TMP_TRANSPILED_FILE if not ext else\
            TMP_TRANSPILED_FILE.split('.')[0] + '.' + ext

        with open(fname, 'w+') as _file:
            _file.write(contents)
        _file.close()

        return self.send_filepath(fname)
