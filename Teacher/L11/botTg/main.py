from aiogram import Bot, Dispatcher, executor, types
import func

global bot
global dp
from commands import commands

commands()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=main)