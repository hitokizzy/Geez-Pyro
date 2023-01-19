import importlib
from pyrogram import idle
from uvloop import install

from config import CMD_HNDLR
from Geez.modules import ALL_MODULES
from Geez import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bot1, bots, app, ids
from geezlibs import join
from geezlibs import BOT_VER, __version__ as gver
MSG_ON = """
**Geez Pyro Userbot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
**Userbot Version -** `{}`
**Geez Library Version - `{}`**
**Ketik** `{}alive` **untuk Mengecheck Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
©️2023 Geez|RAM Projects
"""
BOT_ON = (f"**Geez Pyro Assistant**\n\nready and connected")

async def main():
    await app.start()
    LOGGER("Geez").info("Memulai Geez Pyro..")
    LOGGER("Geez").info("Loading Everything.")
    for all_module in ALL_MODULES:
        importlib.import_module("Geez.modules" + all_module)
        LOGGER("Geez").info(f"Successfully Imported {all_module} ")
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            await join(bot)
            try:
                await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, gver, CMD_HNDLR))
                await app.send_message(BOTLOG_CHATID, BOT_ON)
            except BaseException:
                pass
            LOGGER("Geez").info(f"Started as {ex.first_name} | {ex.id} ")
            ids.append(ex.id)
        except Exception as e:
            print(f"{e}")
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("Geez").info("Starting Geez Pyro Userbot")
    install()
    LOOP.run_until_complete(main())
