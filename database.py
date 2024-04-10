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

    def create_user(self, name, username, password):
        self.cur.execute('INSERT INTO users (name, login, password) values (?, ?, ?)',
                         (name, username, password))
        self.conn.commit()






# double - дробное число