import logging
from aiogram import executor, Dispatcher, Bot, types
from aiogram.types import ReplyKeyboardMarkup

import config
from dbm import BOT_DB

db = BOT_DB("users.db")

# logging
logging.basicConfig(level=logging.INFO)

# init
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)



async def on_startup(dp):
    await bot.send_message(config.BOT_LOG, "Bot Started")

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer("Здравствуйте")
    if(not db.user_exist(message.from_user.id)):
        db.add_user(message.from_user.id)
        await message.answer("Я зарегестрировал вас")
    reply = ReplyKeyboardMarkup()
    btn1 = "Узнать время"
    reply.add(btn1)
    await message.answer("Выберите действие", reply_markup=reply)


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup)
