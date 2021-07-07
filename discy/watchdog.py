# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 11:17:18 2021

@author: Julian Brink
"""
'''
Dieses Script nutzt das Modul "watchdog" um einen bestimmten System Ordner zu 
observieren und bei Veränderungen im Ordner bestimmte Handlungen auszuführen.
Explizit wird hier mein anderes Script gestartet, sobald eine neue Datei im 
Ordner erstellt wird: 
    pandas_read_transform_write_to_SQL_Server.py
    
Der zu überwachende Ordner, ist der Ordner, in dem dieses Script selbst liegt.
Das wird durch "DIRECTORY_TO_WATCH = '.'" notiert. (Sonst wäre ein Ordner Pfad anzugeben)

Mein anderes Script befindet sich auch in dem selben Ordner und muss erst importiert werden.
Aus diesem Script wird dann eine bestimmte Function ausgeführt. 
'''
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import scorecard_reader


class Watcher:
    DIRECTORY_TO_WATCH = "."

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print("Received created event - %s." % event.src_path)
            try:
                pandas_read_transform_write_to_SQL_Server.func()
            except:
                print('something went wrong, try again')

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            print("Received modified event - %s." % event.src_path)


if __name__ == '__main__':
    w = Watcher()
    w.run()