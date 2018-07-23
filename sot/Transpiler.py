import subprocess
from sot.constants import TMP_TRANSPILED_FILE


class Transpiler(object):

    def __init__(self, path):
        self.path = path

    def execute(self, filepath):
        return (
            subprocess.check_output(
                [
                    self.path,
                    filepath
                ]
            )
        )

    def execute_contents(self, contents):
        with open(TMP_TRANSPILED_FILE, 'w+') as _file:
            _file.write(contents)
        _file.close()

        return self.execute(TMP_TRANSPILED_FILE)
