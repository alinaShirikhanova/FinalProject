from tkinter import *

from sign_up_window import SignUpWindow


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title('Картина')
        self.geometry('500x500')
        # создание фрейма
        self.frame = Frame(self, width=400, height=400)
        # создание фрейма
        self.label = Label(self.frame, text='Добро пожаловать', font="Times 30")
        self.button = Button(self.frame, text='Зарегистрироваться', command=self.create_reg_window)

        self.frame.pack()
        self.label.pack()
        self.button.pack()

    def create_reg_window(self):
        SignUpWindow()

