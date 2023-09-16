#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("21878393", default=None, cast=int)
API_HASH = config("93ac7bc7579671c0b2415814bcbee731", default=None)
BOT_TOKEN = config("AAEMQZd7JOr3VHoNJcmTCtLescqa7_JfMWs", default=None)
SESSION = config("1AZWarzQBuwVSrEEcLmXgxUJzR8HYZjr9Je2VvLyBLg3g7EfU6auLv6ceGIozm-n30wOOYnczmnkg2p72CaU5BPKwHoKbOsTX1K4TTo9psXjZqMdXNIksbBiuYPQMQIqlK9irWDt_P8roj97T8w1icVW5NtseQ_DGXKhn3WbfWtG_zbVpCJAdVMM6UUMvbTfPGkzGV4s3JGkXN3_lGivWVAO5YbLQhkiwc8vDQsdUAiaKqxw8vfwdaElMq-CG4gwgH5OTHjxrMrqDbGqn8EwdTf-wtaOODKRhRmc3uiyZQzxyQeltQHZCmnQIz3-BMgdlfmPHw-XM9xrIzwComel70lGbsrT8fRg=", default=None)
FORCESUB = config("beelzebul", default=None)
AUTH = config("6183990677", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
