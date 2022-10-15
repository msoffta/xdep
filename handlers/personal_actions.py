from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from Database.dbm import BOT_DB
from dispatcher import dp, bot
import config

db = BOT_DB()


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer_sticker('CAADAgADQQADPIpXGiCbHYE8KiBgAg')

@dp.message_handler(is_admin=True, commands=['ban', 'бан'], commands_prefix=['!', '.', '/'])
async def ban_action(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Вы должны ответить на сообщение")
        return

    await bot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    await message.reply_to_message.reply(f"Вы забанены @{message.reply_to_message.from_user.username}")


@dp.message_handler(is_admin=True, commands=['kick', 'кик'], commands_prefix=['!', '.', '/'])
async def kick_action(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Вы должны ответеть на сообщение")
        return
    await bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    await message.reply_to_message.reply(f"Вас выгнали @{message.reply_to_message.from_user.username}")


@dp.message_handler(is_admin=True, commands=['mute', 'мут'], commands_prefix=['!', '.', '/'])
async def mute_action(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Вы должны ответеть на сообщение")
        return
    await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,
                                   can_send_messages=False)
    await message.reply_to_message.reply("Вас лишили право на разговор"
                                         "\n Всегда думаете о чем говорите и присылаете"
                                         "\n Соблюдайте правила :)")


@dp.message_handler(is_admin=True, commands=['pin', 'пин'], commands_prefix=['!', '.', '/'])
async def pin_action(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Вы должны ответеть на сообщение")
    await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    await message.reply_to_message.reply("Закреплено")


@dp.message_handler(is_admin=True, commands=['id', 'айди'], commands_prefix=['!', '.', '/'])
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


@dp.message_handler(content_types=['new_chat_members', 'pinned_message'])
async def delete_message(message: types.Message):
    await bot.delete_message(message.chat.id, message.message_id)


@dp.message_handler(is_admin=True, commands=['promote'])
async def promote(message: types.Message):
    try:
        title = message.get_args()
        await bot.promote_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id,
                                      is_anonymous=False,
                                      can_manage_chat=True,
                                      can_change_info=True,
                                      can_delete_messages=True,
                                      can_invite_users=True,
                                      can_restrict_members=True,
                                      can_pin_messages=True)
        await bot.set_chat_administrator_custom_title(message.chat.id, message.reply_to_message.from_user.id, custom_title = (title if title else "Админ"))
        await message.reply_to_message.reply(f"Вы стали администратором чата"
                                             f"\nС префиксом {title}")
    except Exception as error:
        await message.answer(f"Я не смог дать права администратора @{message.reply_to_message.from_user.username}"
                             f"\n P.S Вот причина: {error}")

@dp.message_handler(is_admin=True, commands='dmute', commands_prefix=['!', '.', '/'])
async def dmute(message: types.Message):
    if not message.reply_to_message:
        await message.answer("ВЫ должны ответить на сообщение")
    try:
        await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,
                                       can_send_messages=False)
        await message.reply_to_message.delete()
        await message.answer(f"Пользователь @{message.reply_to_message.from_user.username},"
                             f"{message.reply_to_message.from_user.id},"
                             f"{message.reply_to_message.from_user.first_name} "
                             f"\nбыл ограничен и его сообщение были удалены ")
    except Exception as e:
        await message.answer(f"Я не могу ограничить и удалить его сообщение"
                             f"\n Причина: {e}")


@dp.message_handler(is_admin=True, commands='dban', commands_prefix=['!', '.', '/'])
async def dban(message: types.Message):
    if not message.reply_to_message:
        await message.answer("ВЫ должны ответить на сообщение")
    try:
        await bot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id,
                                  can_send_messages=False)
        await message.reply_to_message.delete()
        await message.answer(f"Пользователь @{message.reply_to_message.from_user.username},"
                             f"{message.reply_to_message.from_user.id},"
                             f"{message.reply_to_message.from_user.first_name} "
                             f"\nбыл забанен и его сообщение были удалены ")
    except Exception as e:
        await message.answer(f"Я не могу забанить и удалить его сообщение"
                             f"\n Причина: {e}")

@dp.message_handler(is_admin=True, commands='unban', commands_prefix=['!', '.', '/'])
async def unban(message: types.Message):
    if not message.reply_to_message:
        await message.answer("Вы должны ответить на сообщение")
    try:
        await bot.unban_chat_member(message.chat.id,
                                    message.reply_to_message.from_user.id)
        await message.answer(f"Пользователь @{message.reply_to_message.from_user.username},"
                             f"{message.reply_to_message.from_user.id},"
                             f"{message.reply_to_message.from_user.first_name} "
                             f"\nбыл разбанен")
    except Exception as e:
        await message.answer(f"Я не могу разбанить"
                             f"\n Причина: {e}")

@dp.message_handler(is_admin=True, commands='unmute', commands_prefix=['!', '.', '/'])
async def unmute(message: types.Message):
    if not message.reply_to_message:
        await message.answer("Я не знаю кому разрешить право на разговор")
    try:
        await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id,
                                       can_send_messages=True, until_date=0)

        await message.answer(f"Пользователь @{message.reply_to_message.from_user.username},"
                             f"{message.reply_to_message.from_user.id},"
                             f"{message.reply_to_message.from_user.first_name} "
                             f"\nможет говорить")
    except Exception as e:
        await message.answer(f"Я не могу разрешить ему право на разговор"
                             f"\n Причина: {e}")

@dp.message_handler(commands='send')
async def send(message: types.Message):
    text = message.text.replace('/send', '')
    await bot.delete_message(message.chat.id, message.message_id)
    await message.answer(text)
