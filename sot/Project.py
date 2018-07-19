import json
import os
import time
from watchdog.observers import Observer
from read_and_close import read_and_close
from sot.Watcher import Watcher
from sot.utils import try_except
from sot.constants import SOT_PROJECT_CONFIG


class Project(object):

    def __init__(self, path):
        self.path = path
        self.config_path = os.path.join(path, SOT_PROJECT_CONFIG)
        self.config = self.get_config()
        self.observer = Observer()

    def _get_config(self):
        return json.loads(read_and_close(self.config_path))

    def get_config(self):
        return try_except(
            self._get_config,
            ValueError,
            lambda x: {}
        )

    def _watcher(self):
        self.observer.start()

        while True:
            time.sleep(1)

    def start_watcher(self):
        self.observer.schedule(
            Watcher(),
            path=self.path,
            recursive=True
        )

        try_except(
            self._watcher,
            KeyboardInterrupt,
            lambda x: self.observer.stop()
        )

        self.observer.join(1)
