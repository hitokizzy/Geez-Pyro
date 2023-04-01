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
from pyrogram import filters, Client
from pyrogram.types import Message
from geezlibs.geez import geez
from Geez.modules.basic import add_command_help
from Geez import cmds

f = filters.chat([])

if f:
    @Client.on_message(f)
    async def auto_read(bot: Client, message: Message):
        await bot.read_history(message.chat.id)
        message.continue_propagation()


@geez("autoscroll", cmds)
async def add_to_auto_read(bot: Client, message: Message):
    if message.chat.id in f:
        f.remove(message.chat.id)
        await message.edit("Autoscroll deactivated")
    else:
        f.add(message.chat.id)
        await message.edit("Autoscroll activated")


add_command_help(
    "autoscroll",
    [
        [f"{cmds}autoscroll",f"Send {cmds}autoscroll in any chat to automatically read all sent messages until you call "
            "autoscroll again. This is useful if you have Telegram open on another screen.",
        ],
    ],
)
