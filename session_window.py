from tkinter import *
from tkinter import ttk

from database import Database


class SessionWindow(Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry('500x500')
        self.title("Добро пожаловать")
        self.db = Database()

        # создаем виджет со вкладками
        self.notebook = ttk.Notebook(self)
        # создаем фреймы, на которых разместим списки пользователей и товаров
        self.frame1 = Frame(self.notebook)
        self.frame2 = Frame(self.notebook)

        # создаем вкладки
        self.notebook.add(self.frame1, text="Просмотр пользователей")
        self.notebook.add(self.frame2, text="Просмотр товаров")
        self.notebook.pack(expand=True, fill=BOTH)

        # создаем переменную для списка пользователей
        self.users_list = Variable()
        # создаем таблицу списочную
        self.users_listbox = Listbox(listvariable=self.users_list, master=self.frame1)

        # создаем колоночки, задавая имена для обращения к ним внутри программы
        self.columns = ['id', 'name', 'login', 'password', 'address']

        # создаем таблицу. show='headings' - тип отображения, отображаться будут имена столбцов в данном случае
        self.users_table = ttk.Treeview(columns=self.columns, show='headings', master=self.frame1)

        # названия столбцов таблицы
        columns_names = ['ID', 'Name', 'Login', 'Password', 'Address']
        columns_width = [30, 100, 100, 100, 130]

        for i in range(len(self.columns)):
            self.users_table.heading(self.columns[i], columns_names[i])
            self.users_table.column(f'#{i}', stretch=NO, width=columns_width[i])


        self.frame1.pack()
        self.frame2.pack()
        self.users_table.pack()




















