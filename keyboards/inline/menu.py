from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

first = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Button 1', callback_data='second'),
        ]
    ]
)

button_exit = InlineKeyboardButton('Exit', callback_data='exit')
button_call_manager = InlineKeyboardButton('Call manager', callback_data='call_manager')
button_test = InlineKeyboardButton('test', callback_data='test')

first.add(button_exit)
first.add(button_call_manager)

row_keyboard = InlineKeyboardMarkup().row(button_exit, button_call_manager, button_test)
button4 = InlineKeyboardButton('4', callback_data='4')
button5 = InlineKeyboardButton('5', callback_data='5')

markup3 = InlineKeyboardMarkup()

markup3.row(button_exit, button_call_manager, button_test)
markup3.add(InlineKeyboardButton('Big brother', callback_data='1'))
markup3.row(button4, button5)

social = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("Youtube", url='https://www.youtube.com/'),
         InlineKeyboardButton("Twitch", url='https://www.twitch.com/')],
        [InlineKeyboardButton("LinkdIn", url='https://www.linkedin.com/'), ],
        [InlineKeyboardButton("Twitter", url='https://x.com/'), ],
    ]
)

music_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Скрябін - Сам собі країна", url='https://www.youtube.com/watch?v=kvYZlkQEOuE')],
        [InlineKeyboardButton(text="YourCoach - Кобзар", url='https://www.youtube.com/watch?v=vdnVlxy1pcI'), ],
    ]
)

moovie_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("Жива сталь | Real steel (2011)",
                              url="https://filmix.ac/films/fantastiks/89732-fg9-zhivaya-stal-2011.html"),
         InlineKeyboardButton("Я - легенда | I am legend (2007)",
                              url="https://filmix.ac/films/drama/2896-ks5-ja-legenda-2007.html")],
    ]
)
