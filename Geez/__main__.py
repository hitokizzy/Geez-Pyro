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


async def main():
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("ramsupport")
            await bot.join_chat("GeezSupport")
            await bot.join_chat("userbotch")
            await bot.join_chat("Geezprojectt")
            try:
                await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER))
            except BaseException:
                pass
            LOGGER("Geez").info(f"Logged in as {ex.first_name} | [ {ex.id} ]")
        except Exception as a:
            LOGGER("main").warning(a)
    LOGGER("Geez").info(f"Geez Pyro v{BOT_VER} ⚙️[⚡ Activated ⚡]")
    if bot1 and not str(BOTLOG_CHATID).startswith("-100"):
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("Geez").info("Starting Geez Pyro Userbot")
    install()
    LOOP.run_until_complete(main())
