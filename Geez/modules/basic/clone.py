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
import os

from pyrogram import *
from pyrogram.types import *

from geezlibs.geez.helper.basic import edit_or_reply, get_text, get_user

from Geez.modules.basic.help import add_command_help
from Geez import cmds

OWNER = os.environ.get("OWNER", None)
BIO = os.environ.get("BIO", "Geez Pyro Userbot")


@Client.on_message(filters.command("clone", cmds) & filters.me)
async def clone(client: Client, message: Message):
    text = get_text(message)
    op = await message.edit_text("`Cloning`")
    userk = get_user(message, text)[0]
    user_ = await client.get_users(userk)
    if not user_:
        await op.edit("`Whom i should clone:(`")
        return

    get_bio = await client.get_chat(user_.id)
    f_name = user_.first_name
    c_bio = get_bio.bio
    pic = user_.photo.big_file_id
    poto = await client.download_media(pic)

    await client.set_profile_photo(photo=poto)
    await client.update_profile(
        first_name=f_name,
        bio=c_bio,
    )
    await message.edit(f"**BErhasil Clone** __{f_name}__")


@Client.on_message(filters.command("revert", cmds) & filters.me)
async def revert(client: Client, message: Message):
    await message.edit("`Reverting`")
    r_bio = BIO

    # Get ur Name back
    await client.update_profile(
        first_name=OWNER,
        bio=r_bio,
    )
    # Delte first photo to get ur identify
    photos = [p async for p in client.get_chat_photos("me")]
    await client.delete_profile_photos(photos[0].file_id)
    await message.edit("`I am back!`")


add_command_help(
    "clone",[
        [f"{cmds}clone", "Clone profile seseorang."],
        [f"{cmds}revert", "Kembali ke profile (bio dan nama terkadang menggunakan default)."],
    ],
)
