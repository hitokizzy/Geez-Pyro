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
    await app.start()
    print("LOG: Memulai Geez Pyro..")
    print("LOG: Loading Everything.")
    for all_module in ALL_MODULES:
        importlib.import_module("Geez.modules" + all_module)
        print(f"Successfully Imported {all_module} ")
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            await join(bot)
            try:
                await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HNDLR, gver))
            except BaseException:
                pass
            print(f"Started as {ex.first_name} | {ex.id} ")
            ids.append(ex.id)
        except Exception as e:
            print(f"{e}")
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("Geez").info("Starting Geez Pyro Userbot")
    install()
    LOOP.run_until_complete(main())

