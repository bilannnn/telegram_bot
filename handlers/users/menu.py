from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu
from loader import dp


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Chose one, please:", reply_markup=menu)


@dp.message_handler(Text(equals=["Ok!", "Questions", "Info"]))
async def get_food(message: Message):
    await message.answer(f"You chose {message.text}. ", reply_markup=ReplyKeyboardRemove())