import importlib
import time
from pyrogram import idle
from uvloop import install
from geezlibs import logging
from geezlibs import BOT_VER, __version__ as gver
from Geez import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bot1, bots, app, ids
from config import CMD_HNDLR
from Geez.modules import ALL_MODULES


MSG_ON = """
**Geez Pyro Userbot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
**Userbot Version -** `{}`
**Geez Library Version - `{}`**
**Ketik** `{}geez` **untuk Mengecheck Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
©️2023 Geez|RAM Projects
"""
MSG_BOT = (f"**Geez Pyro Assistant**\nis alive...")




async def main():
    await app.start()
    LOGGER("Geez").info("LOG: Memulai Geez Pyro..")
    LOGGER("Geez").info("LOG: Loading Everything.")
    for all_module in ALL_MODULES:
        importlib.import_module("Geez.modules" + all_module)
        LOGGER("Geez").info("module initializing.")
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            await logging(bot)
            try:
                await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, gver, CMD_HNDLR))
                await app.send_message(BOTLOG_CHATID, MSG_BOT)
            except BaseException as a:
                LOGGER("Geez").warning(f"{a}")
            LOGGER("Geez").info(f"Started as {ex.first_name} | {ex.id} ")
            ids.append(ex.id)
        except Exception as e:
            LOGGER("Geez").info(f"{e}")
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("Geez").info("Starting Geez Pyro Userbot")
    install()
    LOOP.run_until_complete(main())
