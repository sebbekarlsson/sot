import json
import os
import time
import ntpath
from watchdog.observers import Observer
from read_and_close import read_and_close
from sot.Watcher import Watcher
from sot.utils import try_except, loop
from sot.constants import SOT_PROJECT_CONFIG
from sot.Transpiler import Transpiler


class Project(object):

    def __init__(self, path='.'):
        self.path = path
        self.config_path = os.path.join(path, SOT_PROJECT_CONFIG)
        self.config = self.get_config()
        self.watcher = Watcher(self, self.get_watch_patterns())
        self.observer = Observer()

    def get_config(self):
        return json.loads(read_and_close(self.config_path))\
            if os.path.isfile(self.config_path) else {}

    def get_transpilers(self):
        return try_except(
            lambda x: map(
                lambda x: Transpiler(**x),
                self.get_config()['transpilers']
            ),
            KeyError,
            lambda x: []
        )

    def get_main_file(self):
        return os.path.join(self.path, self.get_config_attr('main')) if\
            self.get_config_attr('main') else None

    def get_output_file(self):
        return os.path.join(self.path, self.get_config_attr('out')) if\
            self.get_config_attr('out') else None

    def get_config_attr(self, attribute, default=None):
        return try_except(
            lambda x: self.get_config()[attribute],
            KeyError,
            lambda x: default
        )

    def get_watch_patterns(self):
        config = self.get_config()

        return config['watch'] if 'watch' in config else []

    def write_transpiled(self, filename, contents):
        with open(self.get_transpiled_name(filename), 'w+') as _file:
            _file.write(contents)
        _file.close()

        return contents

    def transpile(self, filepath=None, out=None):
        for transpiler in self.get_transpilers():
            if out:
                out = transpiler.execute(out)
            else:
                out = read_and_close(filepath)
                out = transpiler.execute(out)

        return self.write_transpiled(filepath, out) if filepath and out else\
            out

    def get_transpiled_name(self, filename):
        basename = ntpath.basename(filename)
        return filename.replace(basename, '.' + basename) + '.sot'

    def get_file_contents(self, filename, force=False):
        contents = ''

        with open(filename) as _file:
            contents = _file.read()
        _file.close()

        return contents

    def bundle(self):
        with open(self.get_output_file(), 'w+') as _file:
            _file.write(
                self.get_file_contents(
                    self.get_transpiled_name(self.get_main_file())
                )
            )
        _file.close()

    def _watcher(self, args):
        self.observer.start()

        loop(True, lambda: time.sleep(1))

    def start_watcher(self):
        self.observer.schedule(
            self.watcher,
            path=self.path,
            recursive=True
        )

        try_except(
            self._watcher,
            KeyboardInterrupt,
            lambda x: self.observer.stop()
        )

        self.observer.join(1)
