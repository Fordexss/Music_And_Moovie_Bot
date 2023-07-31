import emoji
from aiogram import types

from loader import dp

emoji_hamburger = emoji.emojize('🥪')
emoji_smile = emoji.emojize('😋')


@dp.message_handler(text="Доброго ранку")
async def promo(message: types.Message):
    await message.reply('Доброго ранку, чим будеш снідати?')
    await message.answer(emoji_hamburger)
    await message.answer(emoji_smile)
