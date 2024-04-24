from tkinter import *
from tkinter import ttk

from database import Database


class SessionWindow(Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Post Service')
        self.geometry('500x500+300+100')

        notebook = ttk.Notebook(self)
        notebook.pack(expand=True, fill=BOTH)
        frame1 = ttk.Frame(notebook)
        frame1.pack()
        notebook.add(frame1, text='Просмотр пользователей')

        frame2 = ttk.Frame(notebook)
        frame2.pack()
        notebook.add(frame2, text='Добавление пользователя')

        columns = ['id', 'login', 'password', 'name', 'surname', 'phone', 'email', 'birthdate', 'status']
        self.users_table = ttk.Treeview(columns=columns, show='headings', master=frame1)

        columns_names = ['ID', 'Login', 'Password', 'Name', 'Surname', 'Phone', 'Email', 'Birthdate', 'Status']
        columns_width = [30, 100, 100, 120, 120, 150, 150, 100, 100]

        for i in range(len(columns)):
            self.users_table.heading(columns[i], text=columns_names[i])
            self.users_table.column(f'#{i}', stretch=NO, width=columns_width[i])

        vertical_scrollbar = ttk.Scrollbar(orient=VERTICAL, command=self.users_table.yview, master=frame1)
        self.users_table.configure(yscrollcommand=vertical_scrollbar.set)

        horizontal_scrollbar = ttk.Scrollbar(orient=HORIZONTAL, command=self.users_table.xview, master=frame1)
        self.users_table.configure(xscrollcommand=horizontal_scrollbar.set)

        self.load_users_button = ttk.Button(text='Обновить', master=frame1)

        self.load_users_button.pack(side=BOTTOM, anchor=S)
        vertical_scrollbar.pack(side=RIGHT, fill=Y)
        self.users_table.pack(fill=BOTH, expand=True)
        horizontal_scrollbar.pack(side=BOTTOM, fill=X)























