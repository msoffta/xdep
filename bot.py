from aiogram import executor
from dispatcher import dp, on_startup
import handlers


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)