#!/usr/bin/python
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
deleted = []


class MyHandler(FileSystemEventHandler):
    def on_deleted(self, event):
        deleted.append(str(event.src_path))

    def on_created(self, event):
        temp = str(event.src_path)
        if event.is_directory:
            return
        if ".txt" not in temp:
            print(f'Encrypt Alert: {event.event_type}  path : {event.src_path}')

    def on_modified(self, event):
        temp = str(event.src_path)
        if event.is_directory or '.gousputstream' in temp:
            return
        print(f'Encrypt Alert: {event.event_type}  path : {event.src_path}')


if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='data/', recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
