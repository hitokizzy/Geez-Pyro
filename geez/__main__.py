import asyncio
import importlib
from uvloop import install
from pyrogram import Client, idle
from geez.helper import join
from geez.modules import ALL_MODULES
from geez import clients, ids, app
from geez.helper.error import *
from geez.helper.misc import heroku, git
from config import *
from geez import *

async def start_bot():
    await app.start()
    print("LOG: Memulai Geez Pyro..")
    for all_module in ALL_MODULES:
        importlib.import_module("geez.modules" + all_module)
        print(f"Successfully Imported {all_module} ")
    for cli in clients:
        try:
            await cli.start()
            ex = await cli.get_me()
            await join(cli)
            try:
                await cli.send_photo(LOG_GROUP, photo=LOG_ALIVE, caption=ALIVE_ONLINE)
            except BaseException:
                pass
            print(f"Started {ex.first_name} ")
            ids.append(ex.id)
        except Exception as e:
            print(f"{e}")
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("Geez").info("Geez Pyro Diaktifkan")
    install()
    git()
    heroku()
    loop.run_until_complete(start_bot())
