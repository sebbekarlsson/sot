from watchdog.events import PatternMatchingEventHandler
from sot.Colors import Colors


class Watcher(PatternMatchingEventHandler):
    patterns = ['*.js']

    def __init__(self, project):
        PatternMatchingEventHandler.__init__(self)
        self.project = project

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

        if self.project.get_output_file() in event.src_path:
            return

        print('{}{}{}'.format(
            Colors.BOLD,
            'Detected change in: {}{}{}'.format(
                Colors.OKBLUE, event.src_path, Colors.ENDC),
            Colors.ENDC
        ))

        self.project.transpile(event.src_path)

        if self.process_main_file(self.project.get_main_file()):
            self.project.bundle()

            print('{}{}{}'.format(
                Colors.OKGREEN,
                'Wrote bundle: {}{}{}'.format(
                    Colors.OKBLUE,
                    self.project.get_output_file(),
                    Colors.ENDC
                ),
                Colors.ENDC
            ))

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)
