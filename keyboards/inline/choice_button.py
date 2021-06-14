from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from cfg.config import Urls
from keyboards.inline.callback_datas import buy_callback

# choice = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text='Buy apple', callback_data=buy_callback.new(
#                 item_name='apple', quantity=1
#             )),
#             InlineKeyboardButton(text='Buy banana', callback_data=buy_callback.new(
#                 item_name='banana', quantity=1
#             )),
#         ],
#         [
#             InlineKeyboardButton(text='Cancel', callback_data='cancel')
#         ]
#     ]
# )


choice = InlineKeyboardMarkup(row_width=2)

buy_apple = InlineKeyboardButton(text='Buy apple', callback_data=buy_callback.new(
                item_name='apple', quantity=5))
choice.insert(buy_apple)

buy_apple = InlineKeyboardButton(text='Buy banana', callback_data=buy_callback.new(
                item_name='banana', quantity=1))
choice.insert(buy_apple)

cancel = InlineKeyboardButton(text='Cancel', callback_data='cancel')
choice.insert(cancel)


banana_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Buy now!', url=Urls.BANANA)
        ]
    ]
)

apple_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Buy now!', url=Urls.APPLES)
        ]
    ]
)