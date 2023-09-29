"""
if you can read this, this meant you use code from Geez | Ram Project
this code is from somewhere else
please dont hestitate to steal it
because Geez and Ram doesn't care about credit
at least we are know as well
who Geez and Ram is


kopas repo dan hapus credit, ga akan jadikan lu seorang developer

YANG NYOLONG REPO INI TRUS DIJUAL JADI PREM, LU GAY...
©2023 Geez | Ram Team
"""
import asyncio
import math
import os
import dotenv
import heroku3
import requests
import urllib3
from geezlibs.geez.utils.misc import is_heroku, paste_queue
from geezlibs.geez import geez
from config import HEROKU_API_KEY, HEROKU_APP_NAME
from config import CMD_HNDLR as cmds
from Geez import bot1
from Geez.modules.basic import add_command_help
from Geez.modules.basic.update import restart

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


@geez("logs", cmds)
async def log_(client, message):
    if await is_heroku():
        if HEROKU_API_KEY == "" and HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>Menggunakan App Heroku!</b>\n\nMasukan/atur  `HEROKU_API_KEY` dan `HEROKU_APP_NAME` untuk bisa melakukan update!"
            )
        elif HEROKU_API_KEY == "" or HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>Menggunakan App Heroku!</b>\n\n<b>pastikan</b> `HEROKU_API_KEY` **dan** `HEROKU_APP_NAME` <b>sudah di configurasi dengan benar!</b>"
            )
    else:
        return await message.reply_text("hanya untuk Heroku Deployment")
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        happ = Heroku.app(HEROKU_APP_NAME)
    except BaseException:
        return await message.reply_text(
            " Pastikan Heroku API Key, App name sudah benar"
        )
    data = happ.get_log()
    if len(data) > 1024:
        link = await paste_queue(data)
        url = link + "/index.txt"
        return await message.reply_text(
            f"Logs [{HEROKU_APP_NAME}]\n\n[Klik untuk melihat({url})"
        )
    else:
        return await message.reply_text(data)


@geez("getvar", cmds)
async def varget_(client, message):
    usage = f"**Usage:**\n{cmds}get_var [Var Name]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    check_var = message.text.split(None, 2)[1]
    if await is_heroku():
        if HEROKU_API_KEY == "" and HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>Menggunakan App Heroku!</b>\n\nMasukan/atur  `HEROKU_API_KEY` dan `HEROKU_APP_NAME` untuk bisa melakukan update!"
            )
        elif HEROKU_API_KEY == "" or HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>Menggunakan App Heroku!</b>\n\n<b>pastikan</b> `HEROKU_API_KEY` **dan** `HEROKU_APP_NAME` <b>sudah di configurasi dengan benar!</b>"
            )
        try:
            Heroku = heroku3.from_key(HEROKU_API_KEY)
            happ = Heroku.app(HEROKU_APP_NAME)
        except BaseException:
            return await message.reply_text(
                " Pastikan Heroku API Key, App name sudah benar"
            )
        heroku_config = happ.config()
        if check_var in heroku_config:
            return await message.reply_text(
                f"**Heroku Config:**\n\n**{check_var}:** `{heroku_config[check_var]}`"
            )
        else:
            return await message.reply_text("Var tidak ditemukan")
    else:
        path = dotenv.find_dotenv()
        if not path:
            return await message.reply_text(".env tidak ditemukan.")
        output = dotenv.get_key(path, check_var)
        if not output:
            return await message.reply_text("var tidak ditemukan")
        else:
            return await message.reply_text(
                f".env:\n\n**{check_var}:** `{str(output)}`"
            )


@geez("delvar", cmds)
async def vardel_(client, message):
    usage = f"**Usage:**\n{cmds}delvar [nama var]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    check_var = message.text.split(None, 2)[1]
    if await is_heroku():
        if HEROKU_API_KEY == "" and HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>Menggunakan App Heroku!</b>\n\nMasukan/atur  `HEROKU_API_KEY` dan `HEROKU_APP_NAME` untuk bisa melakukan update!"
            )
        elif HEROKU_API_KEY == "" or HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>Menggunakan App Heroku!</b>\n\n<b>pastikan</b> `HEROKU_API_KEY` **dan** `HEROKU_APP_NAME` <b>sudah di configurasi dengan benar!</b>"
            )
        try:
            Heroku = heroku3.from_key(HEROKU_API_KEY)
            happ = Heroku.app(HEROKU_APP_NAME)
        except BaseException:
            return await message.reply_text(
                " Pastikan Heroku API Key, App name sudah benar"
            )
        heroku_config = happ.config()
        if check_var in heroku_config:
            await message.reply_text(
                f"**Heroku Var:**\n\n`{check_var}` Sukses dihapus."
            )
            del heroku_config[check_var]
        else:
            return await message.reply_text(f"Var tidak ditemukan")
    else:
        path = dotenv.find_dotenv()
        if not path:
            return await message.reply_text(".env tidak ditemukan.")
        output = dotenv.unset_key(path, check_var)
        if not output[0]:
            return await message.reply_text(",env var tidak ditemukan")
        else:
            return await message.reply_text(
                f".env Var :\n\n`{check_var}` Berhasil dihapus. ketik {cmds}restart untuk restart bot."
            )


@geez("setvar", cmds)
async def setvar(client, message):
    usage = f"**Usage:**\n{cmds}setvar [nama var] [isi var]"
    if len(message.command) < 3:
        return await message.reply_text(usage)
    to_set = message.text.split(None, 2)[1].strip()
    value = message.text.split(None, 2)[2].strip()
    if await is_heroku():
        if HEROKU_API_KEY == "" and HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>Menggunakan App Heroku!</b>\n\nMasukan/atur  `HEROKU_API_KEY` dan `HEROKU_APP_NAME` untuk bisa melakukan update!"
            )
        elif HEROKU_API_KEY == "" or HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>Menggunakan App Heroku!</b>\n\n<b>pastikan</b> `HEROKU_API_KEY` **dan** `HEROKU_APP_NAME` <b>sudah di configurasi dengan benar!</b>"
            )
        try:
            Heroku = heroku3.from_key(HEROKU_API_KEY)
            happ = Heroku.app(HEROKU_APP_NAME)
        except BaseException:
            return await message.reply_text(
                " Pastikan Heroku API Key, App name sudah benar"
            )
        heroku_config = happ.config()
        if to_set in heroku_config:
            await message.reply_text(
                f"**Heroku Var diupdate:**\n\n`{to_set}` sukses ter-Update. Bot akan restart."
            )
        else:
            await message.reply_text(
                f"Vars `{to_set}`berhasil dibuat. Bot akan restart."
            )
        heroku_config[to_set] = value
    else:
        path = dotenv.find_dotenv()
        if not path:
            return await message.reply_text(".env not found.")
        output = dotenv.set_key(path, to_set, value)
        if dotenv.get_key(path, to_set):
            return await message.reply_text(
                f"**.env Var:**\n\n`{to_set}`berhasil diupdate. ketik {cmds}restart untuk merestart bot."
            )
        else:
            return await message.reply_text(
                f"**.env Var:**\n\n`{to_set}`berhasil dibuat. ketik {cmds}restart untuk merestart bot."
            )


@geez("usage", cmds)
async def usage_dynos(client, message):
    if await is_heroku():
        if HEROKU_API_KEY == "" and HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>Menggunakan App Heroku!</b>\n\nMasukan/atur  `HEROKU_API_KEY` dan `HEROKU_APP_NAME` untuk bisa melakukan update!"
            )
        elif HEROKU_API_KEY == "" or HEROKU_APP_NAME == "":
            return await message.reply_text(
                "<b>Menggunakan App Heroku!</b>\n\n<b>pastikan</b> `HEROKU_API_KEY` **dan** `HEROKU_APP_NAME` <b>sudah di configurasi dengan benar!</b>"
            )
    else:
            return await message.reply_text("Hanya untuk Heroku Deployment")
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        happ = Heroku.app(HEROKU_APP_NAME)
    except BaseException:
        return await message.reply_text(
            " Pastikan Heroku API Key, App name sudah benar"
        )
    dyno = await message.reply_text("Memeriksa penggunaan dyno...")
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
**Penggunaan Dyno Geez-Pyro**

Dyno terpakai:
  ┗ Terpakai: `{AppHours}`**h**  `{AppMinutes}`**m**  [`{AppPercentage}`**%**]
Dyno tersisa:
  ┗ Tersisa: `{hours}`**h**  `{minutes}`**m**  [`{percentage}`**%**]"""
    return await dyno.edit(text)

async def geez_log():
    botlog_chat_id = os.environ.get('BOTLOG_CHATID')
    if botlog_chat_id:
        return
   
    group_name = "GeezPyro BotLog"
    group_description = 'This group is used to log my bot activities'
    group = await bot1.create_supergroup(group_name, group_description)

    if await is_heroku():
        try:
            Heroku = heroku3.from_key(os.environ.get('HEROKU_API_KEY'))
            happ = Heroku.app(os.environ.get('HEROKU_APP_NAME'))
            happ.config()['BOTLOG_CHATID'] = str(group.id)
        except:
            pass
    else:
        with open('.env', 'a') as env_file:
            env_file.write(f'\nBOTLOG_CHATID={group.id}')

    message_text = 'Grouplog berhasil diaktifkan,\nmohon masukkan bot anda ke group ini, dan aktifkan mode inline.\nRestarting Geez Pyro...!'
    await bot1.send_message(group.id, message_text)
    restart()

add_command_help(
    "heroku",
    [
        [f"{cmds}getvar", "Check vars."],
        [f"{cmds}setvar", "Set Var."],
        [f"{cmds}usage", "Check Dyno usage."],
        [f"{cmds}delvar", "Del var."],
    ],
)
