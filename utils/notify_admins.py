import logging

from aiogram import Dispatcher

from cfg.config import Config


async def on_startup_notify(dp: Dispatcher):
    for admin in Config.ADMIN_ID:
        try:
            await dp.bot.send_message(admin, "Гарного тобі дня, а я починаю працювати)")

        except Exception as err:
            logging.exception(err)
