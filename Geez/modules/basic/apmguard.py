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

from geezlibs.geez.database import pmpermit as TOD
from geezlibs.geez import geez
from Geez import SUDO_USER
from Geez.modules.basic import add_command_help
from .pmguard import get_arg
from Geez import cmds

@geez("pmguard", cmds)
async def pmguard(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**on atau off ??**")
        return
    if arg == "off":
        await TOD.set_pm(False)
        await message.edit("**PM Guard Dimatikan**")
    if arg == "on":
        await TOD.set_pm(True)
        await message.edit("**PM Guard diaktifkan**")
        
@geez("setpmmsg", cmds)
async def setpmmsg(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**berikan pesan untuk set**")
        return
    if arg == "default":
        await TOD.set_permit_message(TOD.PMPERMIT_MESSAGE)
        await message.edit("**pesan Anti PM diset ke default**.")
        return
    await TOD.set_permit_message(f"`{arg}`")
    await message.edit("**Pesan custom Anti Pm diset**")


add_command_help(
    "antipm",
    [
        [f"{cmds}pmguard [on or off]", " -> mengaktifkan dan menonaktifkan anti-pm."],
        [f"{cmds}setpmmsg [message or default]", " -> Sets a custom anti-pm message."],
        [f"{cmds}setblockmsg [message or default]", "-> Sets custom block message."],
        [f"{cmds}setlimit [value]", " -> This one sets a max. message limit for unwanted PMs and when they go beyond it, bamm!."],
        [f"{cmds}ok", " -> Allows a user to PM you."],
        [f"{cmds}no", " -> Denies a user to PM you."],
    ],
)