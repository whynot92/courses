import sqlite3


class DB():
    def __init__(self):
        with sqlite3.connect("mydb.db") as conn:
            cursor = conn.cursor()

            cursor.execute('''CREATE TABLE IF NOT EXISTS person(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT, 
                        age INTEGER
                        )''')

