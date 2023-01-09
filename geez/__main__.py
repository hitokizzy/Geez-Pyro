from pyrogram import idle
from uvloop import install

from geez import *
from geez.helper.misc import create_botlog, git, heroku
from config import BOT_VER

MSG_ON = """
🔥 **Geez-Pyro** 🔥
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
🤖 **Userbot Version -** `{}`
⌨️ **Ketik** `{}alive` **untuk Mengecek Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""


async def main():
    for client in clients:
        try:
            await client.start()
            client.me = await client.get_me()
            await client.join_chat("ramsupportt")
            await client.join_chat("GeezSupport")
            await client.join_chat("Geezprojectt")
            await client.join_chat("userbotch")
            try:
                await client.send_message(LOG_GROUP, MSG_ON.format(BOT_VER))
            except BaseException:
                pass
            LOGGER("geez").info(f"Logged in as {client.me.first_name} | [ {client.me.id} ]")
        except Exception as a:
            LOGGER("main").warning(a)
    LOGGER("geez").info(f"Geez-Pyro v{BOT_VER} ⚙️[⚡ Activated ⚡]")
    if app and not str(LOG_GROUP).startswith("-100"):
        await create_botlog(app)
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("geez").info("Starting Geez-Pyro")
    install()
    git()
    heroku()
    LOOP.run_until_complete(main())
