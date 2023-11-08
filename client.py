import socket
import tkinter as tk
from socket import *

class Reason:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('Знаешь, почему твоего рейтинга не хватило, чтобы остаться на кампусе?')
        self.win.geometry("1024x512+400+300")
        self.win.config(bg='#8B0000')
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect(("127.0.0.1", 12345))
        self.shlyapu()
    def shlyapu(self):
        btn = tk.Button(self.win, background='#8B0000', width=20, height=3,
                        text='Узнать причину :(', font="Times 25",command=self.click)
        btn.place(relx=0.5, rely=0.5, anchor='center')
        btn.focus()
    def click(self):
        self.client.send(bytes("\00", 'ascii'))
    def run(self):
        self.win.mainloop()
if __name__ == "__main__":
    app = Reason()
    app.run()