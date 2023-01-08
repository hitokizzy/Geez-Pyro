# credits : @xtsea

import asyncio
from pyrogram import *
from pyrogram.types import *
from pyrogram import Client as gez
from pyrogram import Client
from base64 import b64decode as who
from geez.helper.basic import *
from geez.helper.PyroHelpers import *
from geez.modules.help import *
from geez.helper.dev import *
from geez.helper.misc import *
from geez.helper.error import *
from config import *

@gez.on_message(filters.command("takepm", ".") & filters.me)
async def takepm(client: Client, message: Message):
    lol = message.reply_to_message
    if not lol:
       return await message.edit("**Please reply**")
    try:
       await lol.copy(message.from_user.id)
       await message.delete()
    except BaseException:
        pass

@gez.on_message(filters.command("take", ".") & filters.me)
async def take(client: Client, message: Message):
    lol = message.reply_to_message
    if not lol:
       return await message.edit("**Please reply**")
    try:
       await lol.copy(message.chat.id)
       await message.delete()
    except BaseException:
        pass


@gez.on_message(filters.command("fwd", ".") & filters.me)
async def fwd(client: Client, message: Message):
    lol = message.reply_to_message
    if not lol:
       return await message.edit("**Please reply**")
    try:
       await lol.forward(message.chat.id)
       await message.delete()
    except BaseException:
        pass

