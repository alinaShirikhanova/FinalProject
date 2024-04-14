from tkinter import *

from log_in_window import LoginWindow
from sign_up_window import SignUpWindow


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title('Главное окно')
        self.geometry('500x500')

        # создание фрейма
        self.frame = Frame(self, width=400, height=400)
        # создание фрейма
        self.label = Label(self.frame, text='Добро пожаловать', font="Times 30")
        self.button = Button(self.frame, text='Зарегистрироваться', command=self.create_reg_window)
        self.button_auth = Button(self.frame, text='Войти', command=self.create_auth_window)


        self.frame.pack()
        self.label.pack()
        self.button.pack()
        self.button_auth.pack()

    def create_reg_window(self):
        SignUpWindow()

    def create_auth_window(self):
        LoginWindow()

