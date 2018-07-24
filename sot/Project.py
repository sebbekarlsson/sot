import json
import os
import time
from watchdog.observers import Observer
from read_and_close import read_and_close
from sot.Watcher import Watcher
from sot.Transpiler import Transpiler
from sot.utils import try_except, loop
from sot.constants import SOT_PROJECT_CONFIG
from sot.exceptions import NoConfigException, ConfigMissingAttribute


class Project(object):

    def __init__(self, path='.'):
        self.path = path
        self.config = self.get_config(os.path.join(path, SOT_PROJECT_CONFIG))
        self.watcher = Watcher(self, self.config['watch'])
        self.observer = Observer()

    def validate_config(self, config):
        requirements = ['watch', 'main', 'out']

        for requirement in requirements:
            if requirement not in config:
                raise ConfigMissingAttribute(requirement)

        return config

    def get_config(self, path):
        if not os.path.isfile(path):
            raise NoConfigException()

        contents = read_and_close(path)

        return self.validate_config(json.loads(contents) if contents else {})

    def get_transpilers(self):
        return map(lambda x: Transpiler(**x), self.config['transpilers'])\
            if 'transpilers' in self.config else []

    def transpile(self, out='', ext=None, bundle=True):
        for transpiler in self.get_transpilers():
            out = transpiler.send_contents(out, ext)

        return self.bundle(out) if bundle else out

    def bundle(self, out):
        out_fname = os.path.join(self.path, self.config['out'])

        with open(out_fname, 'w+') as _file:
            _file.write(out)
        _file.close()

        return out

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
