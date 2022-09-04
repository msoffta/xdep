import sqlite3
from sqlite3 import Error
import config
from main import bot, dp

async def connect(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        await bot.send_message(config.BOT_LOG, "Connected to SQL")
    except Error as e:
        await bot.send_message(config.BOT_LOG, f"Something broke:"
                                                 f"\nError: {e} ")
    return connection