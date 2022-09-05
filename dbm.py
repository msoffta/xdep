import sqlite3
from sqlite3 import Error
import config

class BOT_DB:

    def __init__(self, db_file):
        self.c = sqlite3.connect(db_file)
        self.cur = self.c.cursor()
    

    def add_user(self, user_id):
        self.cur.execute("INSERT INTO 'users' ('user_id') VALUES (?)", (user_id,))
        return self.c.commit()