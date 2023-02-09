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
from pyrogram import filters, Client
from geezlibs.geez.database.rraid import *
from cache.data import *
from Geez import SUDO_USER
from Geez.modules.basic import *
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
