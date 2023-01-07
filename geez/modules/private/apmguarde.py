from pyrogram import filters, Client
from pyrogram import Client as ren
import asyncio
from geez import SUDO_USER
from geez.modules.help import *
from pyrogram.methods import messages
from .pmguard import get_arg, denied_users

import geez.database.mongodb.pmpermitdb as geez



@gez.on_message(filters.command("pmguard", ["."]) & filters.me)
async def pmguard(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**I only understand on or off**")
        return
    if arg == "off":
        await geez.set_pm(False)
        await message.edit("**PM Guard Deactivated**")
    if arg == "on":
        await geez.set_pm(True)
        await message.edit("**PM Guard Activated**")

@gez.on_message(filters.command("setpmmsg", ["."]) & filters.me)
async def setpmmsg(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**What message to set**")
        return
    if arg == "default":
        await geez.set_permit_message(geez.PMPERMIT_MESSAGE)
        await message.edit("**Anti_PM message set to default**.")
        return
    await geez.set_permit_message(f"`{arg}`")
    await message.edit("**Custom anti-pm message set**")


add_command_help(
    "PM Permit",
    [
        [".pmguard [on or off]", " -> Activates or deactivates anti-pm."],
        [".setpmmsg [message or default]", " -> Sets a custom anti-pm message."],
        [".setblockmsg [message or default]", "-> Sets custom block message."],
        [".setlimit [value]", " -> This one sets a max. message limit for unwanted PMs and when they go beyond it, bamm!."],
        [".allow", " -> Allows a user to PM you."],
        [".deny", " -> Denies a user to PM you."],
    ],
)
