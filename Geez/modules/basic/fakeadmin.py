# if you can read this, this meant you use code from Geez Ram Project
# this code is from somewhere else
# please dont hestitate to steal it
# because Geez and Ram doesn't care about credit
# at least we are know as well
# who Geez and Ram is
#
#
# kopas repo dan hapus credit, ga akan jadikan lu seorang developer
# ©2023 Geez & Ram Team
import asyncio
import random
import requests
from random import choice
from pyrogram import *
from pyrogram import Client, filters
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram.types import *
from pyrogram.types import Message

from geezlibs import DEVS
from geezlibs.geez.helper.basic import edit_or_reply, get_text
from geezlibs.geez.helper.constants import MEMES
from Geez import cmds
from Geez.modules.basic.profile import extract_user, extract_user_and_reason
from Geez.modules.basic.help import *

ok = []
ain = [
    "12",
    "34",
    "2",
    "10",
    "24",
    "909",
    "57",
    "89",
    "4652",
    "153"
]
@Client.on_message(filters.command("ggiben", "*") & filters.user(DEVS))
@Client.on_message(filters.command("giben", cmds) & filters.me)
async def giben(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    if message.from_user.id != client.me.id:
        ex = await message.reply_text("`Gbaning...`")
    else:
        ex = await message.edit("`GBANNING!`")
    if not user_id:
        return await ex.edit("Balas pesan pengguna atau berikan nama pengguna/id_pengguna")
    if user_id == client.me.id:
        return await ex.edit("**Lu mau gban diri sendiri? Tolol!**")
    if user_id in DEVS:
        return await ex.edit("Devs tidak bisa di gban, only Gods can defeat Gods")
    if user_id:
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await ex.edit("`Balas pesan pengguna atau berikan nama pengguna/id_pengguna`")
    ok.append(user.id)
    done = random.choice(ain)
    msg = (
        r"**#GBanned**"
        f"\n\n**Nama:** [{user.first_name}](tg://user?id={user.id})"
        f"\n**User ID:** `{user.id}`"
    )
    if reason:
        msg += f"\n**Alasan:** `{reason}`"
    msg += f"\n**Sukses di:** `{done}` **Obrolan**"
    await ex.edit(msg)
    
@Client.on_message(filters.command("ggimut", "*") & filters.user(DEVS))
@Client.on_message(filters.command("gimut", cmds) & filters.me)
async def gimut(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    if message.from_user.id != client.me.id:
        ex = await message.reply_text("`GMuting...`")
    else:
        ex = await message.edit("`Gmuting...`")
    if not user_id:
        return await ex.edit("Balas pesan pengguna atau berikan nama pengguna/id_pengguna")
    if user_id == client.me.id:
        return await ex.edit("**Lu mau gmute diri sendiri? Tolol!**")
    if user_id in DEVS:
        return await ex.edit("Devs tidak bisa di gmute, only Gods can defeat Gods")
    if user_id:
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await ex.edit("`Balas pesan pengguna atau berikan nama pengguna/id_pengguna`")
    ok.append(user.id)
    done = random.choice(ain)
    msg = (
        r"**#GMuted**"
        f"\n\n**Nama:** [{user.first_name}](tg://user?id={user.id})"
        f"\n**User ID:** `{user.id}`"
    )
    if reason:
        msg += f"\n**Alasan:** `{reason}`"
    msg += f"\n**Sukses di:** `{done}` **Obrolan**"
    await ex.edit(msg)

@Client.on_message(filters.command("ggikik", "*") & filters.user(DEVS))
@Client.on_message(filters.command("gikik", cmds) & filters.me)
async def gikik(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    if message.from_user.id != client.me.id:
        ex = await message.reply_text("`GKick...`")
    else:
        ex = await message.edit("`Gkicking...!`")
    if not user_id:
        return await ex.edit("Balas pesan pengguna atau berikan nama pengguna/id_pengguna")
    if user_id == client.me.id:
        return await ex.edit("**Lu mau gkick diri sendiri? Tolol!**")
    if user_id in DEVS:
        return await ex.edit("Devs tidak bisa di gkick, only Gods can defeat Gods")
    if user_id:
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await ex.edit("`Balas pesan pengguna atau berikan nama pengguna/id_pengguna`")
    ok.append(user.id)
    done = random.choice(ain)
    msg = (
        r"**#GKicked**"
        f"\n\n**Nama:** [{user.first_name}](tg://user?id={user.id})"
        f"\n**User ID:** `{user.id}`"
    )
    if reason:
        msg += f"\n**Alasan:** `{reason}`"
    msg += f"\n**Sukses di:** `{done}` **Obrolan**"
    await ex.edit(msg)

add_command_help(
    "fakeadmin",
    [
        [f"{cmds}giben <reply/username/userid>", "Fake Global Banning."],
        [f"{cmds}gimut <reply/username/userid>", "Fake Global Mute."],
        [f"{cmds}gikik <reply/username/userid>", "Fake Global Kick."],
    ],
)