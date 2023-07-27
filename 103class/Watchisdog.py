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
        name, extention = os.path.splitext(event.src_path)
        time.sleep(1)
        for key, value in dir_tree.items():
            time.sleep(1)
            if extention in value:
                filename = os.path.basename(event.src_path)
                path1 = fromdir+filename
                path2 = todir+key
                path3 = todir+key+"/"+filename
                if os.path.exists(path2):
                    print("movendo:", filename)
                    shutil.move(path1, path3)
                    time.sleep(1)
                else:
                    os.makedirs(path2)
                    print("movendo:", filename)
                    shutil.move(path1, path3)
                    time.sleep(1)


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
