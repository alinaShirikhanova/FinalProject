import sqlite3

db_filename = 'post_service.db'
conn = sqlite3.connect(db_filename)
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL, 
            login TEXT NOT NULL UNIQUE, 
            password TEXT NOT NULL,
            
            address TEXT);
            ''')


