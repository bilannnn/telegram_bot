import yaml

with open('/home/rostyslav/Desktop/Telegram_bots/telegram_bot/cfg/configs.yaml', 'r') as file:
    __parse_data__ = yaml.load(file, Loader=yaml.FullLoader)
    BOT_CFG = __parse_data__['bot_cfg']


class Config:
    BOT_TOKEN = BOT_CFG['bot_token']
    ADMIN_ID = BOT_CFG['admin_id']
    ID = BOT_CFG['id']