# from aiogram import types
# from aiogram.dispatcher import FSMContext
#
# from loader import dp
#
#
# @dp.message_handler(state=None)
# async def bot_echo(message: types.Message):
#     await message.answer(f"Echo"
#                          f"Message:\n"
#                          f"{message.text}")
#
#
# @dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
# async def bot_echo_all(message: types.Message, state: FSMContext):
#     state = await state.get_state()
#     await message.answer(f"Echo <code>{state}</code>.\n"
#                          f"\nmessage:\n"
#                          f"<code>{message}</code>")
