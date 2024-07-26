import sys
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import subprocess

class FileChangeHandler(PatternMatchingEventHandler):
    def __init__(self, patterns):
        super().__init__(patterns=patterns)
        self.process = None
        self.restart_process()

    def restart_process(self):
        if self.process:
            self.process.kill()
            self.process.wait()
        print("Starting main.py...")
        self.process = subprocess.Popen([sys.executable, 'main.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.log_output()

    def log_output(self):
        for line in self.process.stdout:
            print(line.decode(), end='')

    def on_modified(self, event):
        print(f'{event.src_path} has been modified')
        self.restart_process()

    def on_created(self, event):
        print(f'{event.src_path} has been created')
        self.restart_process()

if __name__ == "__main__":
    path = "."
    event_handler = FileChangeHandler(patterns=["*.py"])
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    print(f"Watching for file changes in {path}...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
