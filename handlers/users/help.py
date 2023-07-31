from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Почати діалог",
            "/help - Отримати довідку",
            "/saysomething - Скажи цитату"
            "/action - Подивитися фільми / послухати музику")
    
    await message.answer("\n".join(text))
