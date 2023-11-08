import tkinter as tk
import threading
from socket import *
import random

class Reason:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('Дело вот в чём')
        self.win.geometry("1024x256+400+300")
        self.win.config(bg='#FFFFE0')

        self.app_border()
        self.start()

    def _server_run(self):
        server = socket(AF_INET, SOCK_STREAM)
        server.bind(("127.0.0.1", 12345))
        server.listen()
        user, addr = server.accept()
        while True:
            data = user.recv(1024)
            if not data:
                break
            self.update_text()

    def app_border(self):
        self.frame = tk.Frame(self.win, background='#FFFFE0')
        self.frame.pack(fill=tk.BOTH, expand=True)
    def kontsovka(self):
        f = open('Причины.txt', encoding='utf-8')
        data = f.read()
        lines = data.split('\n')
        line = random.randrange(len(lines))
        return lines[line]
    def start(self):
        new_thread = threading.Thread(target=self._server_run)
        new_thread.start()

    def update_text(self):
        text = tk.Label(self.win, width=60, height=3, background='#FFFFE0', text=self.kontsovka(), font="Times 25")
        text.place(relx=0.5, rely=0.5, anchor='center')
    def run(app):
        app.win.mainloop()
if __name__ == "__main__":
    app = Reason()
    app.run()