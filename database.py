import sqlite3

class Database:
    def __init__(self):
        self.db_filename = 'post_service.db'
        self.conn = sqlite3.connect(self.db_filename)
        self.cur = self.conn.cursor()

        self.cur.execute('''CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL, 
                    login TEXT NOT NULL UNIQUE, 
                    password TEXT NOT NULL,
        
                    address TEXT);
                    ''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS products (
                    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL, 
                    description TEXT NOT NULL UNIQUE, 
                    price DOUBLE NOT NULL,
                    amount INTEGER NOT NULL);
            ''')

        self.cur.execute("""CREATE TABLE IF NOT EXISTS orders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    product_id INTEGER NOT NULL);
                    """)




    def create_user(self, name, username, password):
        self.cur.execute('INSERT INTO users (name, login, password) values (?, ?, ?)',
                         (name, username, password))
        self.conn.commit()

    def get_user_by_login(self, username):
        self.cur.execute('SELECT * FROM users WHERE login = ?', (username, ))
        return self.cur.fetchone() # достаем из ответ от БД 1 запись и возвращаем ее

    def get_all_users(self):
        self.cur.execute('SELECT * FROM users')
        # print(self.cur.fetchone()) # достаем 1 запись
        # print(self.cur.fetchmany(3)) # достаем несколько записей
        return self.cur.fetchall() # достаем все записи


    def get_all_orders(self):
        self.cur.execute('SELECT * FROM orders')
        return self.cur.fetchall()

    def get_all_orders_with_names(self):
        orders = self.get_all_orders()
        orders_with_names = []
        for order in orders:
            self.cur.execute('SELECT name FROM users WHERE user_id = ?', (order[1], ))
            user = self.cur.fetchone()[0]
            self.cur.execute('SELECT name FROM products WHERE product_id = ?', (order[2],))
            product = self.cur.fetchone()[0]
            orders_with_names.append([order[0], user, product])

        return orders_with_names




# Реализовать метод, который достат все товары из базы данных





# double - дробное число
