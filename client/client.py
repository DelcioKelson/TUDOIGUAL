import socket
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import LoggingEventHandler
import sys
import logging

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                 # Reserve a port for your service.
s.connect((host, port))


class OnMyWatch:
    # Set the directory on watch
    watchDirectory = "/home/ferramenta/Documents/SSI/TG/TUDOIGUAL/client"
  
    def __init__(self):
        self.observer = Observer()
  
    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchDirectory, recursive = True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")
  
        self.observer.join()
  
  
class Handler(FileSystemEventHandler):
  
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None
        if ".swp" not in event.src_path:
            filename = event.src_path.split('/')[-1]
            s.send(filename.encode())
            if event.event_type == 'created' or event.event_type == 'modified':
                # Event is created or modified, you can process it now
                print("Watchdog received created event - % s." % event.src_path)
                option = "created"
                s.send(option.encode())
                f = open(event.src_path,'rb')
                l = f.read(1024)
                while (l):
                    print ('Sending...')
                    s.send(l)
                    l = f.read(1024)
                f.close()
                print ("Done Sending")
                s.shutdown(socket.SHUT_WR)

            elif event.event_type == 'deleted':
                # Event is modified, you can process it now
                print("Watchdog received deleted event - % s." % event.src_path)
                option = "deleted"
                s.send(option.encode())

if __name__ == '__main__':
    watch = OnMyWatch()
    watch.run()