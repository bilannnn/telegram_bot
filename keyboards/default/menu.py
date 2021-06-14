from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ok!"),
        ],
        [
            KeyboardButton(text="Question"),
            KeyboardButton(text="Info")
        ],
    ],
    resize_keyboard=True
)