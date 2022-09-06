from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dbm import BOT_DB
from dispatcher import dp
import config

db = BOT_DB("users.db")

@dp.message_handler(commands='start')
async def start(message: types.Message):
    if(not db.user_exist(message.from_user.id)):
        db.add_user(message.from_user.id)
    inline = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("Добавить в чат", url='https://t.me/xdepbot?startgroup=new')
    inline.add(btn1)
    await message.answer("Привет, я многофункциональный бот добавь меня в свой чат", reply_markup=inline)


@dp.message_handler(commands='info')
async def info(message: types.Message):
    inline = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton("Создатель", url="t.me/theHero_7")
    inline.add(btn1)
    await message.answer("""Информация о боте
                          \nОсновные Административные команды:
        /ban  !ban  .ban
        /kick !kick .kick
        /mute !mute .mute
        /pin  !pin  .pin
        /id   !id   .id
                          \nОсновные игровые команды:
            Недоступно
        В будущих обновлениях""", reply_markup=inline)

@dp.message_handler(commands='ban', command)