import os
import time
import subprocess
import psutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ReloadHandler(FileSystemEventHandler):
    def __init__(self, command):
        self.command = command
        self.process = None
        self.start_process()

    def start_process(self):
        """Start the game process and terminate the old one."""
        if self.process:
            # Try to gracefully kill the old process
            self.kill_previous_process()

        self.process = subprocess.Popen(self.command, shell=True)

    def kill_previous_process(self):
        """Kill the previous game process."""
        if self.process:
            # Get the process ID of the old process
            pid = self.process.pid
            try:
                # Check if the process is still running and kill it
                p = psutil.Process(pid)
                p.terminate()  # Try to terminate gracefully
                p.wait(timeout=3)  # Wait for it to terminate cleanly
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass  # Process may have already closed

    def on_modified(self, event):
        """Restart the game when a .py file is modified."""
        if event.src_path.endswith(".py"):
            print(f"File {event.src_path} changed, restarting game...")
            self.start_process()

if __name__ == "__main__":
    path = "."  # Watch current directory
    command = "python main.py"  # Adjust if using a virtual environment

    event_handler = ReloadHandler(command)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        if event_handler.process:
            event_handler.kill_previous_process()  # Ensure cleanup
    observer.join()
