import subprocess


class Transpiler(object):

    def __init__(self, path):
        self.path = path

    def execute(self, indata):
        return (
            subprocess.check_output(
                [
                    self.path,
                    indata
                ]
            )
        )
