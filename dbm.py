import sqlite3
from sqlite3 import Error
import config
from dispatcher import bot, dp


class BOT_DB:

    def __init__(self, db_file):
        self.c = sqlite3.connect(db_file)
        self.cur = self.c.cursor()

    def user_exist(self, user_id):
        exist = self.cur.execute("SELECT user_id FROM users WHERE user_id = ?", (user_id,))
        return bool(len(exist.fetchall()))

    def add_user(self, user_id):
        self.cur.execute("INSERT INTO 'users' ('user_id') VALUES (?)", (user_id,))
        return self.c.commit()

    def addfilter(self, filters, filter_msg, state):
        self.cur.execute("INSERT INTO 'users' ('filters', 'filter_msg', 'state') VALUES (?, ?, ?)",
                         (filters, filter_msg, state,))
        return self.c.commit()

    def getfilter(self):
        filters = self.cur.execute("SELECT filters FROM users")
        return filters.fetchall()

    def getfilter_msg(self):
        filter_msg = self.cur.execute("SELECT filter_msg FROM users")
        return filter_msg.fetchall()

    def getstate(self):
        statetype = self.cur.execute("SELECT state FROM users")
        return statetype.fetchone()
