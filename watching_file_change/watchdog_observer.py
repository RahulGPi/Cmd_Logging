import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class LogFileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == "path file -> cmd_commands.log":
            subprocess.run(["python", "path file -> Main.py"])

if __name__ == "__main__":
    event_handler = LogFileHandler()
    observer = Observer()
    observer.schedule(event_handler, path='path file to the workspace Cmd_logging', recursive=False)  # Note the directory path here
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
