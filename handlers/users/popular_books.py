from aiogram.dispatcher import FSMContext

import parsing.get_books
from loader import dp
from aiogram.types import Message, ReplyKeyboardRemove, ParseMode
import keyboards
from aiogram.dispatcher.filters import Command

# --- Main Menu Handlers
@dp.message_handler(text=keyboards.default.menu.main_captions[2])
async def solve_tasks(message: Message):
    books = await parsing.get_books.get_books(keyboards.default.menu.main_captions[2])
    #await message.answer(f'{books[0]}')
    caption = f'{books[0]["name"]}\n' \
              f'Оценка: {books[0]["rate"]}\n' \
              f'Автор: {books[0]["author"]}\n' \
              f'Жанр: {books[0]["genre"]}\n' \
              f'Количество страниц: {books[0]["pages"]}\n' \
              f'Описание: {books[0]["about"]}\n' \
              f'<a href = {books[0]["name"]}>Ссылка для прочтения</a>'
#Вывод

    await message.answer_photo(books[0]["img"],  caption=caption, parse_mode="html")