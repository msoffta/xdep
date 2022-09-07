from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import bot
from dbm import BOT_DB
from dispatcher import dp, cot
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

@dp.message_handler(is_admin=True,commands=['ban','бан'], commands_prefix=['!', '.','/'])
async def ban_action(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Вы должны ответить на сообщение")
        return

    await cot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    await message.reply_to_message.reply(f"Вы забанены @{message.reply_to_message.from_user.username}")
@dp.message_handler(is_admin=True, commands=['kick','кик'], commands_prefix=['!','.','/'])
async def kick_action(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Вы должны ответеть на сообщение")
        return
    await cot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    await message.reply_to_message.reply(f"Вас выгнали @{message.reply_to_message.from_user.username}")

@dp.message_handler(is_admin=True, commands=['mute','мут'], commands_prefix=['!','.','/'])
async def mute_action(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Вы должны ответеть на сообщение")
        return
    await cot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,
                                   can_send_messages=False)
    await message.reply_to_message.reply("Вас лишили право на разговор"
                                         "\n Всегда думаете о чем говорите и присылаете"
                                         "\n Соблюдайте правила :)")

@dp.message_handler(is_admin=True, commands=['pin', 'пин'], commands_prefix=['!','.','/'])
async def pin_action(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Вы должны ответеть на сообщение")
    await cot.pin_chat_message(message.chat.id, message.message_id)
    await message.reply_to_message.reply("Закреплено")




@dp.message_handler(is_admin=True, commands=['id', 'айди'], commands_prefix=['!','.','/'])
async def id_action(message: types.Message):
    id_chat = message.chat.id
    msg_id = message.message_id
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        await message.answer(f"Айди чата: {id_chat}"
                             f"\n Айди сообщения: {msg_id}"
                             f"\n Айди юзера: {user_id}")
    if not message.reply_to_message:
        await message.answer(f"Айди чата: {id_chat}"
                         f"\n Айди сообщения: {msg_id}")