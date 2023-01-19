# if you can read this, this meant you use code from Geez Ram Project
# this code is from somewhere else
# please dont hestitate to steal it
# because Geez and Ram doesn't care about credit
# at least we are know as well
# who Geez and Ram is
#
#
# kopas repo dan hapus credit, ga akan jadikan lu seorang developer
# ©2023 Geez & Ram Team
import asyncio
import math
import os
import random
import shutil
import sys
import dotenv
import heroku3
import requests
import urllib3
from datetime import datetime
from time import strftime, time
from geezlibs.geez.utils.misc import is_heroku, user_input, paste_queue
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError
from pyrogram import Client, filters
from pyrogram.types import Message

from config import BOTLOG_CHATID, HEROKU_API_KEY, HEROKU_APP_NAME, BRANCH, REPO_URL
from config import CMD_HNDLR as cmds
from geezlibs.geez.helper.cmd import *
from Geez import SUDO_USER, Client
from Geez.modules.basic import add_command_help

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    str(HEROKU_API_KEY),
    "https",
    str(HEROKU_APP_NAME),
    "HEAD",
    "main",
]

@Client.on_message(filters.command("restart", cmd) & filters.me)
async def restart_bot(_, message: Message):
    try:
        msg = await message.reply(" `Restarting bot...`")
        LOGGER(__name__).info("BOT SERVER RESTARTED !!")
    except BaseException as err:
        LOGGER(__name__).info(f"{err}")
        return
    await msg.edit_text("✅ **Bot has restarted !**\n\n")
    if HAPP is not None:
        HAPP.restart()
    else:
        args = [sys.executable, "-m", "Geez"]
        execle(sys.executable, *args, environ)


@Client.on_message(
    filters.command(["shutdown", "off"], cmd) & filters.me
)
async def shutdown_bot(client: Client, message: Message):
    if BOTLOG_CHATID:
        await client.send_message(
            BOTLOG_CHATID,
            "**#SHUTDOWN** \n"
            "**Geez-Userbot** telah di matikan!\nJika ingin menghidupkan kembali silahkan buka heroku",
        )
    await message.reply("🔌 **Geez-Userbot Berhasil di matikan!**")
    if HAPP is not None:
        HAPP.process_formation()["worker"].scale(0)
    else:
        sys.exit(0)


@Client.on_message(
    filters.command(["logs"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def log_(client, message):
    if await is_heroku():
        if HEROKU_API_KEY == "" and HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>HEROKU APP DETECTED!</b>\n\nIn order to update your Client, you need to set up the `HEROKU_API_KEY` and `HEROKU_APP_NAME` vars respectively!"
            )
        elif HEROKU_API_KEY == "" or HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>HEROKU APP DETECTED!</b>\n\n<b>Make sure to add both</b> `HEROKU_API_KEY` **and** `HEROKU_APP_NAME` <b>vars correctly in order to be able to update remotely!</b>"
            )
    else:
        return await message.reply_text("Only for Heroku Apps")
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        happ = Heroku.app(HEROKU_APP_NAME)
    except BaseException:
        return await message.reply_text(
            " Please make sure your Heroku API Key, Your App name are configured correctly in the heroku"
        )
    data = happ.get_log()
    if len(data) > 1024:
        link = await paste_queue(data)
        url = link + "/index.txt"
        return await message.reply_text(
            f"Here is the Log of Your App[{HEROKU_APP_NAME}]\n\n[Click Here to checkout Logs]({url})"
        )
    else:
        return await message.reply_text(data)


@Client.on_message(
    filters.command(["getvar"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def varget(client: Client, message: Message):
    usage = "**Usage:**\n/getvar [Var Name]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    check_var = message.text.split(None, 2)[1]
    if await is_heroku():
        if HEROKU_API_KEY == "" and HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>HEROKU APP DETECTED!</b>\n\nIn order to update your Client, you need to set up the `HEROKU_API_KEY` and `HEROKU_APP_NAME` vars respectively!"
            )
        elif HEROKU_API_KEY == "" or HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>HEROKU APP DETECTED!</b>\n\n<b>Make sure to add both</b> `HEROKU_API_KEY` **and** `HEROKU_APP_NAME` <b>vars correctly in order to be able to update remotely!</b>"
            )
        try:
            Heroku = heroku3.from_key(HEROKU_API_KEY)
            happ = Heroku.app(HEROKU_APP_NAME)
        except BaseException:
            return await message.reply_text(
                " Please make sure your Heroku API Key, Your App name are configured correctly in the heroku"
            )
        heroku_config = happ.config()
        if check_var in heroku_config:
            return await message.reply_text(
                f"**Heroku Config:**\n\n**{check_var}:** `{heroku_config[check_var]}`"
            )
        else:
            return await message.reply_text("No such Var")
    else:
        path = dotenv.find_dotenv()
        if not path:
            return await message.reply_text(".env not found.")
        output = dotenv.get_key(path, check_var)
        if not output:
            return await message.reply_text("No such Var")
        else:
            return await message.reply_text(
                f".env:\n\n**{check_var}:** `{str(output)}`"
            )


@Client.on_message(
    filters.command(["delvar"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def vardel(client: Client, message: Message):
    usage = "**Usage:**\n/delvar [Var Name]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    check_var = message.text.split(None, 2)[1]
    if await is_heroku():
        if HEROKU_API_KEY == "" and HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>HEROKU APP DETECTED!</b>\n\nIn order to update your Client, you need to set up the `HEROKU_API_KEY` and `HEROKU_APP_NAME` vars respectively!"
            )
        elif HEROKU_API_KEY == "" or HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>HEROKU APP DETECTED!</b>\n\n<b>Make sure to add both</b> `HEROKU_API_KEY` **and** `HEROKU_APP_NAME` <b>vars correctly in order to be able to update remotely!</b>"
            )
        try:
            Heroku = heroku3.from_key(HEROKU_API_KEY)
            happ = Heroku.app(HEROKU_APP_NAME)
        except BaseException:
            return await message.reply_text(
                " Please make sure your Heroku API Key, Your App name are configured correctly in the heroku"
            )
        heroku_config = happ.config()
        if check_var in heroku_config:
            await message.reply_text(
                f"**Heroku Var Deletion:**\n\n`{check_var}` has been deleted successfully."
            )
            del heroku_config[check_var]
        else:
            return await message.reply_text(f"No such Var")
    else:
        path = dotenv.find_dotenv()
        if not path:
            return await message.reply_text(".env not found.")
        output = dotenv.unset_key(path, check_var)
        if not output[0]:
            return await message.reply_text("No such Var")
        else:
            return await message.reply_text(
                f".env Var Deletion:\n\n`{check_var}` has been deleted successfully. To restart the bot touch /restart command."
            )


@Client.on_message(
    filters.command(["setvar"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def setvar(client: Client, message: Message):
    usage = "**Usage:**\n/setvar [Var Name] [Var Value]"
    if len(message.command) < 3:
        return await message.reply_text(usage)
    to_set = message.text.split(None, 2)[1].strip()
    value = message.text.split(None, 2)[2].strip()
    if await is_heroku():
        if HEROKU_API_KEY == "" and HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>HEROKU APP DETECTED!</b>\n\nIn order to update your Client, you need to set up the `HEROKU_API_KEY` and `HEROKU_APP_NAME` vars respectively!"
            )
        elif HEROKU_API_KEY == "" or HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>HEROKU APP DETECTED!</b>\n\n<b>Make sure to add both</b> `HEROKU_API_KEY` **and** `HEROKU_APP_NAME` <b>vars correctly in order to be able to update remotely!</b>"
            )
        try:
            Heroku = heroku3.from_key(HEROKU_API_KEY)
            happ = Heroku.app(HEROKU_APP_NAME)
        except BaseException:
            return await message.reply_text(
                " Please make sure your Heroku API Key, Your App name are configured correctly in the heroku"
            )
        heroku_config = happ.config()
        if to_set in heroku_config:
            await message.reply_text(
                f"**Heroku Var Updation:**\n\n`{to_set}` has been updated successfully. Bot will Restart Now."
            )
        else:
            await message.reply_text(
                f"Added New Var with name `{to_set}`. Bot will Restart Now."
            )
        heroku_config[to_set] = value
    else:
        path = dotenv.find_dotenv()
        if not path:
            return await message.reply_text(".env not found.")
        output = dotenv.set_key(path, to_set, value)
        if dotenv.get_key(path, to_set):
            return await message.reply_text(
                f"**.env Var updated:**\n\n`{to_set}`has been updated successfully. To restart the bot touch /restart command."
            )
        else:
            return await message.reply_text(
                f"**.env var updated:**\n\n`{to_set}` has been added sucsessfully. To restart the bot touch /restart command."
            )

@Client.on_message(
    filters.command(["usage"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def usage_dynos(client, message):
    ### Credits CatUserbot
    if await is_heroku():
        if HEROKU_API_KEY == "" and HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>HEROKU APP DETECTED!</b>\n\nIn order to update your Client, you need to set up the `HEROKU_API_KEY` and `HEROKU_APP_NAME` vars respectively!"
            )
        elif HEROKU_API_KEY == "" or HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>HEROKU APP DETECTED!</b>\n\n<b>Make sure to add both</b> `HEROKU_API_KEY` **and** `HEROKU_APP_NAME` <b>vars correctly in order to be able to update remotely!</b>"
            )
    else:
        return await message.reply_text("Only for Heroku Apps")
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        happ = Heroku.app(HEROKU_APP_NAME)
    except BaseException:
        return await message.reply_text(
            " Please make sure your Heroku API Key, Your App name are configured correctly in the heroku"
        )
    dyno = await message.reply_text("Checking Heroku Usage. Please Wait")
    account_id = Heroku.account().id
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = "/accounts/" + account_id + "/actions/get-quota"
    r = requests.get("https://api.heroku.com" + path, headers=headers)
    if r.status_code != 200:
        return await dyno.edit("Unable to fetch.")
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)
    await asyncio.sleep(1.5)
    text = f"""
**Penggunaan Dyno Geez Pyro**

Usage:
  ╰┈➤Terpakai: `{AppHours}`**h**  `{AppMinutes}`**m**  [`{AppPercentage}`**%**]
Remaining Quota:
  ╰┈➤Tersisa: `{hours}`**h**  `{minutes}`**m**  [`{percentage}`**%**]"""
    return await dyno.edit(text)

add_command_help(
    "Heroku",
    [
        ["delvar <vars>", "Delete var in Heroku/env."],
        ["getvar <vars>", "See var in Heroku/env."],
        ["setvar <old var> <new var>", "Set var in Heroku/env."],
        ["usage", "See dyno usage in heroku."],
    ],
)
