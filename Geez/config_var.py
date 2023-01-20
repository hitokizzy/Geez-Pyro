import os
from os import getenv
from dotenv import load_dotenv

load_dotenv(".env")


class Config((object)):
    API_ID = int(getenv("API_ID", "6435225")) #optional
    API_HASH = getenv("API_HASH", "") #optional
    SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
    OWNER_ID = int(getenv("OWNER_ID"))
    MONGO_URL = getenv("MONGO_URL")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    ALIVE_PIC = getenv("ALIVE_PIC")
    ALIVE_TEXT = getenv("ALIVE_TEXT")
    PM_LOGGER = getenv("PM_LOGGER")
    BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
    GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
    REPO_URL = getenv("REPO_URL", "https://github.com/hitokizzy/Geez-Pyro")
    HEROKU_API_KEY = getenv("HEROKU_API_KEY")
    HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
    BRANCH = getenv("BRANCH", "main") #don't change
    CMD_HNDLR = getenv("CMD_HNDLR", ".") 
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
