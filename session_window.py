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
        self.frame1.pack()
        self.frame2.pack()

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

        # создаем показатели ширины для каждого столбца
        columns_width = [30, 100, 100, 100, 130]


        # создаем столбцы
        for i in range(len(self.columns)):
            # сопотавляем столбец с названием этого столбца
            self.users_table.heading(self.columns[i], text=columns_names[i])
            # сопостовляем ширину и колонку
            self.users_table.column(f'#{i}', stretch=NO, width=columns_width[i])


        # создаем скроллбары
        vertical_scrollbar = ttk.Scrollbar(orient=VERTICAL, command=self.users_table.yview, master=self.frame1)
        self.users_table.configure(yscrollcommand=vertical_scrollbar.set)

        horizontal_scrollbar = ttk.Scrollbar(orient=HORIZONTAL, command=self.users_table.xview, master=self.frame1)
        self.users_table.configure(xscrollcommand=horizontal_scrollbar.set)

        self.load_users_button = ttk.Button(text='Обновить', master=self.frame1, command=self.load_users_list)

        self.load_users_button.pack(side=BOTTOM, anchor=S)
        vertical_scrollbar.pack(side=RIGHT, fill=Y)
        self.users_table.pack(fill=BOTH, expand=True)
        horizontal_scrollbar.pack(side=BOTTOM, fill=X)

        self.users_table.pack()

        # создание таблицы с товарами
        # создаем колоночки, задавая имена для обращения к ним внутри программы
        self.columns_products = ['id', 'name', 'description', 'price', 'amount']

        # создаем таблицу. show='headings' - тип отображения, отображаться будут имена столбцов в данном случае
        self.products_table = ttk.Treeview(columns=self.columns, show='headings', master=self.frame1)

        # названия столбцов таблицы
        product_columns_names = ['ID', 'Name', 'Description', 'Price', 'Amount']

        # создаем показатели ширины для каждого столбца
        product_columns_width = [30, 100, 100, 100, 130]

        # создаем таблицу. show='headings' - тип отображения, отображаться будут имена столбцов в данном случае
        self.products_table = ttk.Treeview(columns=self.columns_products, show='headings', master=self.frame2)
        # создаем столбцы
        for i in range(len(self.columns)):
            # сопотавляем столбец с названием этого столбца
            self.products_table.heading(self.columns_products[i], text= product_columns_names[i])
            # сопостовляем ширину и колонку
            self.products_table.column(f'#{i}', stretch=NO, width=product_columns_width[i])

        self.products_table.pack()

    def load_users_list(self):
        users = self.db.get_all_users()
        for i in self.users_table.get_children():
            self.users_table.delete(i)

        for user in users:
            self.users_table.insert('', END, values=(
                user[0], user[1], user[2], user[3], user[4]))

# Сопоставить названия столбцов внутри с назаниями столбцов для пользововаетял и установить ширину каждой колонке, как в строке
















