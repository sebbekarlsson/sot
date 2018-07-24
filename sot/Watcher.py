from watchdog.events import PatternMatchingEventHandler
from read_and_close import read_and_close
from sot.Colors import Colors


class Watcher(PatternMatchingEventHandler):
    patterns = []

    def __init__(self, project, watch_patterns):
        PatternMatchingEventHandler.__init__(self)
        self.project = project
        self.patterns = watch_patterns

    def process_main_file(self, main_file):
        return self.project.transpile(main_file) if main_file else None

    def process(self, event):
        """
        event.event_type
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """
        if self.project.config['out'] in event.src_path:
            return

        print('{}{}{}'.format(
            Colors.BOLD,
            'Detected change in: {}{}{}'.format(
                Colors.OKBLUE, event.src_path, Colors.ENDC),
            Colors.ENDC
        ))

        self.project.transpile(read_and_close(self.project.config['main']))

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)
