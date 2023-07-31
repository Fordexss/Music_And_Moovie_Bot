from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

colors = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Red"),
            KeyboardButton(text="Green"),
            KeyboardButton(text="Blue"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

phone = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Поширити номер телефону", request_contact=True),
            KeyboardButton("Поширити локацію", request_location=True),
        ]
    ]
)

action_choose = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Хочу подивитися фільм"),
            KeyboardButton("Хочу послухати музику"),
        ]
    ],
    resize_keyboard=True
)

