import os
from os import getenv
from dotenv import load_dotenv
from base64 import b64decode as who
from pyrogram import Client, filters

load_dotenv("config.env")


API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")
STRING_SESSION1 = getenv("STRING_SESSION1")
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = = [-1001692751821, -1001675396283, -1001578091827, -1001473548283, -1001459812644]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = getenv("OWNER_ID", "2003295492")
BOT_TOKEN = getenv("BOT_TOKEN")
MONGO_URL = getenv("MONGO_URL", "mongodb://mongo:qEMvAihniInPbSc5EWYj@containers-us-west-162.railway.app:7264")

DB_URL = getenv(
    "DATABASE_URL",
    who("cG9zdGdyZXNxbDovL3Bvc3RncmVzOlFqS3VVMmFkRGVaSFF0dzhkajc2QGNvbnRhaW5lcnMtdXMtd2VzdC0xMjAucmFpbHdheS5hcHA6Njc2MC9yYWlsd2F5Cg==").decode("utf-8"),
)
ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/c78bb1efdeed38ee16eb2.png")
ALIVE_TEXT = getenv("ALIVE_TEXT", "")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = int(getenv("LOG_GROUP", ""))
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/hitokizzy/Geez-Pyro")
BRANCH = getenv("BRANCH", "main") #don't change
CMD_HANDLER = getenv("CMD_HANDLER", ".")

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
