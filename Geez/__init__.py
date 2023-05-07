import asyncio
import logging
import sys
import time
from os import getenv
from datetime import datetime
from logging.handlers import RotatingFileHandler
from typing import Any, Dict
from aiohttp import ClientSession
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from gpytranslate import Translator
from pyrogram import Client, filters
from pytgcalls import GroupCallFactory
from geezlibs.geez.database import db_x
from config import (
    API_HASH,
    API_ID,
    CMD_HNDLR,
    STRING_SESSION1,
    STRING_SESSION2,
    STRING_SESSION3,
    STRING_SESSION4,
    STRING_SESSION5,
    STRING_SESSION6,
    STRING_SESSION7,
    STRING_SESSION8,
    STRING_SESSION9,
    STRING_SESSION10,
    STRING_SESSION11,
    STRING_SESSION12,
    STRING_SESSION13,
    STRING_SESSION14,
    STRING_SESSION15,
    SUDO_USERS,
    BOT_TOKEN
)
cmds = CMD_HNDLR
CMD_HELP = {}
clients = []
ids = []
LOG_FILE_NAME = "logs.txt"
SUDOERS = filters.user()

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("asyncio").setLevel(logging.CRITICAL)
logging.getLogger("pytgcalls").setLevel(logging.WARNING)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("pyrogram.client").setLevel(logging.WARNING)
logging.getLogger("pyrogram.session.auth").setLevel(logging.CRITICAL)
logging.getLogger("pyrogram.session.session").setLevel(logging.CRITICAL)

LOGS = logging.getLogger(__name__)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
if (
    not STRING_SESSION1
    and not STRING_SESSION2
    and not STRING_SESSION3
    and not STRING_SESSION4
    and not STRING_SESSION5
    and not STRING_SESSION6
    and not STRING_SESSION7
    and not STRING_SESSION8
    and not STRING_SESSION9
    and not STRING_SESSION10
    and not STRING_SESSION11
    and not STRING_SESSION12
    and not STRING_SESSION13
    and not STRING_SESSION14
    and not STRING_SESSION15
):
    LOGGER(__name__).warning("STRING SESSION TIDAK DITEMUKAN, SHUTDOWN BOT!")
    sys.exit()

if not BOT_TOKEN:
   LOGGER(__name__).error("WARNING: BOT TOKEN TIDAK DITEMUKAN, SHUTDOWN BOT")
   sys.exit()

db = db_x

async def load_sudoers():
    global SUDOERS
    LOGGER("Geez").info("Loading sudoers")
    sudoersdb = db.sudoers
    sudoers = await sudoersdb.find_one({"sudo": "sudo"})
    sudoers = [] if not sudoers else sudoers["sudoers"]
    for user_id in SUDO_USERS:
        SUDOERS.add(user_id)
        if user_id not in sudoers:
            sudoers.append(user_id)
            await sudoersdb.update_one(
                {"sudo": "sudo"},
                {"$set": {"sudoers": sudoers}},
                upsert=True,
            )
    if sudoers:
        for user_id in sudoers:
            SUDOERS.add(user_id)

LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(load_sudoers())
SUDO_USER = SUDOERS
trl = Translator()
aiosession = ClientSession()
CMD_HELP = {}
scheduler = AsyncIOScheduler()
StartTime = time.time()
START_TIME = datetime.now()
TEMP_SETTINGS: Dict[Any, Any] = {}
TEMP_SETTINGS["PM_COUNT"] = {}
TEMP_SETTINGS["PM_LAST_MSG"] = {}

app = Client(
    name="app",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Geez/modules/bot"),
    in_memory=True,
)

bot1 = (
    Client(
        name="bot1",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION1,
        plugins=dict(root="Geez/modules"),
    )
    if STRING_SESSION1
    else None
)

bot2 = (
    Client(
        name="bot2",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION2,
        plugins=dict(root="Geez/modules"),
    )
    if STRING_SESSION2
    else None
)

bot3 = (
    Client(
        name="bot3",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION3,
        plugins=dict(root="Geez/modules"),
    )
    if STRING_SESSION3
    else None
)

bot4 = (
    Client(
        name="bot4",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION4,
        plugins=dict(root="Geez/modules"),
    )
    if STRING_SESSION4
    else None
)

bot5 = (
    Client(
        name="bot5",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION5,
        plugins=dict(root="Geez/modules"),
    )
    if STRING_SESSION5
    else None
)
bot6 = (
    Client(
        name="bot6",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION6,
        plugins=dict(root="Geez/modules"),
    )
    if STRING_SESSION6
    else None
)
bot7 = (
    Client(
        name="bot7",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION7,
        plugins=dict(root="Geez/modules"),
    )
    if STRING_SESSION7
    else None
)
bot8 = (
    Client(
        name="bot8",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION8,
        plugins=dict(root="Geez/modules"),
    )
    if STRING_SESSION8
    else None
)
bot9 = (
    Client(
        name="bot9",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION9,
        plugins=dict(root="Geez/modules"),
    )
    if STRING_SESSION9
    else None
)
bot10 = (
    Client(
        name="bot10",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION10,
        plugins=dict(root="Geez/modules"),
    )
    if STRING_SESSION10
    else None
)
bot11 = (
    Client(
        name="bot11",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION11,
        plugins=dict(root="Geez/modules"),
    )
    if STRING_SESSION11
    else None
)

bot12 = (
    Client(
        name="bot12",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION12,
        plugins=dict(root="Geez/modules"),
    )
    if STRING_SESSION12
    else None
)

bot13 = (
    Client(
        name="bot13",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION13,
        plugins=dict(root="Geez/modules"),
    )
    if STRING_SESSION13
    else None
)

bot14 = (
    Client(
        name="bot14",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION14,
        plugins=dict(root="Geez/modules"),
    )
    if STRING_SESSION14
    else None
)

bot15 = (
    Client(
        name="bot15",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION15,
        plugins=dict(root="Geez/modules"),
    )
    if STRING_SESSION15
    else None
)

bots = [bot for bot in [bot1, bot2, bot3, bot4, bot5, bot6, bot7, bot8, bot9, bot10, bot11, bot12, bot13, bot14, bot15] if bot]

for bot in bots:
    if not hasattr(bot, "group_call"):
        setattr(bot, "group_call", GroupCallFactory(bot).get_group_call())
