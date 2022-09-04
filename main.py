import logging
from aiogram import executor, Dispatcher, Bot, types
import config
import dbm

# logging
logging.basicConfig(level=logging.INFO)

# init
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)



async def on_startup(dp):
    await dbm.connect("main.sqlite")
    await bot.send_message(config.BOT_LOG, "Bot Started")


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer("testing")


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup)
