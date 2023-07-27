import shutil
import time
import os

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

fromdir = "C:/Users/Eliana/Downloads/"
todir = "C:/Users/Eliana/Downloads/arquivos_baixados/"


dir_tree = {"Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
            "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p',  '.m4v', '.avi', '.mov'],
            "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
            "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']}


class Organizer (FileSystemEventHandler):
    def on_created(self, event):
        print(f"Olá, {event.src_path} foi criado!")

    def on_deleted(self, event):
        print(f"Opá, algum inergumino deletou {event.src_path}")


organizer = Organizer()
observer = Observer()
observer.schedule(organizer, fromdir, recursive=True)
# iniciar o observador
observer.start()
# iniciado 👍
try:
    while True:
        time.sleep(2)
        print("executando...")
except KeyboardInterrupt:
    print("interrompido!")
    observer.stop()
