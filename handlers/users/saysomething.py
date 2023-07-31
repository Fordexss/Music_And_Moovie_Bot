import random

from aiogram import types
from aiogram.dispatcher.filters import Command

from data.quotes import quotes
from loader import dp


@dp.message_handler(Command('saysomething'))
async def say_something(message: types.Message):
    randomizer = random.randint(0, len(quotes) - 1)
    say_quote = f"{quotes[randomizer]}"
    await message.reply(say_quote)
