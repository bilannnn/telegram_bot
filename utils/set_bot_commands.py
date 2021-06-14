from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Start bot"),
            types.BotCommand("help", "info"),
            types.BotCommand('menu', 'Menu'),
            types.BotCommand('items', 'Items')
        ]
    )
