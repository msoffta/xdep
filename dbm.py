import sqlite3
from sqlite3 import Error
import config
from main import bot, dp

async def connect(path):
    connection = None
    try:
        connection = sqlite3.connect('B:\\xdep\main.sqlite')
        await bot.send_message(config.BOT_OWNER, "Connected to SQL")
    except Error as e:
        await bot.send_message(config.BOT_OWNER, f"Something broke:"
                                                 f"\nError: {e} ")
    return connection