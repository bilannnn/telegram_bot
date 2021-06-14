import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.choice_button import choice, banana_keyboard, apple_keyboard
from loader import dp


@dp.message_handler(Command("items"))
async def show_items(message: Message):
    await message.answer(text="We have for sale: 5 apples, 1 bananas\n"
                              "if you don't need anything then click Cancel",
                         reply_markup=choice)


@dp.callback_query_handler(text_contains='banana')
async def buy_banana(call: CallbackQuery):
    await call.answer(cache_time=60)
    callback_data = call.data
    logging.info(f'call - {callback_data}')
    await call.message.answer('You chose a banana. There is only one banana. Thanks)',
                              reply_markup=banana_keyboard)


@dp.callback_query_handler(buy_callback.filter(item_name='apple'))
async def buy_apples(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f'call - {callback_data}')
    quantity = callback_data.get('quantity', 0)
    await call.message.answer(f'You chose a apples. We have {quantity} {"apples" if int(quantity) > 1 else "apple"}. Thanks)',
                              reply_markup=apple_keyboard)


@dp.callback_query_handler(text='cancel')
async def cancel_buying(call: CallbackQuery):
    await call.answer('You canceled your purchase.', show_alert=True)
    await call.message.edit_reply_markup(reply_markup=None)
