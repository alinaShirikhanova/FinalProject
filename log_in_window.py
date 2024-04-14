from tkinter import *

from database import Database


class LoginWindow(Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry('500x500')
        self.title("Окно авторизации")
        self.frame = Frame(self, width=300, height=300)
        self.frame.pack()
        self.db = Database()


        # создание лейбла логин
        self.login = Label(self.frame, text="Логин")
        self.login.grid(row=0, column=0)

        self.login_var = StringVar()
        self.pass_var = StringVar()

        self.login_entry = Entry(self.frame, textvariable=self.login_var)
        self.login_entry.grid(row=0, column=1)

        # создание лейбла пароль
        self.password = Label(self.frame, text="Пароль")
        self.password.grid(row=1, column=0)

        self.pass_entry = Entry(self.frame, textvariable=self.pass_var)
        self.pass_entry.grid(row=1, column=1)

        self.notif = Label(self.frame, text='')
        self.notif.grid(row=3, column=1)

        self.button = Button(self.frame, text='Войти', command=self.log_in)
        self.button.grid(row=4, column=1)

    def log_in(self):
        user = self.db.get_user_by_login(self.login_var.get())
        print(user)

        if self.pass_var.get() == user[3]:
            self.notif.config(text='Вы успешно авторизованы', bg='green')
        else:
            self.notif.config(text='Неверный логин или пароль', bg='red')






