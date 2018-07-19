from watchdog.events import PatternMatchingEventHandler


class Watcher(PatternMatchingEventHandler):
    patterns = ['*.java']

    def __init__(self):
        PatternMatchingEventHandler.__init__(self)
        print('Watcher hello')

    def process(self, event):
        """
        event.event_type
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """
        print(event.__dict__)

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)
