# if you can read this, this meant you use code from Geez | Ram Project
# this code is from somewhere else
# please dont hestitate to steal it
# because Geez and Ram doesn't care about credit
# at least we are know as well
# who Geez and Ram is
#
#
# kopas repo dan hapus credit, ga akan jadikan lu seorang developer
# ©2023 Geez | Ram Team
import random
import asyncio
import os
import sys
import asyncio
import re
from random import choice
from pyrogram import filters, Client
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import *
from pyrogram import Client, errors, filters
from pyrogram.types import ChatPermissions, Message
from pyrogram import __version__
from geezlibs.geez.helper.utility import get_arg
from geezlibs.geez.helper.PyroHelpers import get_ub_chats
from geezlibs.geez.database.rraid import *
from cache.data import *
from Geez import SUDO_USER, cmds
from Geez.modules.basic import *
from Geez.modules.basic.profile import extract_user, extract_user_and_reason
SUDO_USERS = SUDO_USER
from .spam import RAIDS



if RAIDS:
 @Client.on_message(filters.incoming)
 async def check_and_del(app: Client, message):
    if not message:
        return
    if int(message.chat.id) in BL_GCAST:
        return
    try:
        if message.from_user.id in (await get_rraid_users()):
            await message.reply_text(f"{random.choice(RAM)}")
    except AttributeError:
        pass
