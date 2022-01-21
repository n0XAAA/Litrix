from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
main_captions = ["Русская классика", "По жанрам", "Популярные", "Жанр"]
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=main_captions[0]),
        ],
        [
            KeyboardButton(text=main_captions[1]),
            KeyboardButton(text=main_captions[2])
        ],
    ],
    resize_keyboard=True
)