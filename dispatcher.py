import logging
from aiogram import Bot, Dispatcher, types
from filters import IsOwnerFilter, IsAdminFilter, MemberCanRestrictFilter
import config

# Configure logging
logging.basicConfig(level=logging.INFO)

# prerequisites
if not config.BOT_TOKEN:
    exit("No token provided")

# init
cot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(cot)

async def on_startup(dp):
    await cot.send_message(config.BOT_LOG, "Бот запущен")

# activate filters
dp.filters_factory.bind(IsOwnerFilter)
dp.filters_factory.bind(IsAdminFilter)
dp.filters_factory.bind(MemberCanRestrictFilter)
