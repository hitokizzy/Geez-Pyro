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
import asyncio
import random
from datetime import datetime
from platform import python_version
from geezlibs import __version__ as gver
from geezlibs import logging
from geezlibs import BOT_VER
from geezlibs.geez.helper.PyroHelpers import ReplyCheck
from pyrogram import __version__, filters, Client
from pyrogram.types import Message
from config import ALIVE_PIC, ALIVE_TEXT
from Geez import START_TIME, SUDO_USER, app
from Geez.modules.basic import add_command_help
from Geez.modules.bot.inline import get_readable_time
from Geez import cmds

geezlogo = [
    "https://telegra.ph/file/d03ce0fb84f81be3aeb09.png",
    "https://telegra.ph/file/200355acbe58c46400f5b.png",
    "https://telegra.ph/file/c78bb1efdeed38ee16eb2.png",
    "https://telegra.ph/file/4143843c984a8ecdc813e.png"
]

alive_logo = ALIVE_PIC or random.choice(geezlogo)

if ALIVE_TEXT:
   txt = ALIVE_TEXT
else:
    txt = (
        f"**Geez Pyro Userbot**\n\n"
        f"〄 **Versi**: `{BOT_VER}`\n"
        f"  ├• **Uptime**: `{str(datetime.now() - START_TIME).split('.')[0]}`\n"
        f"  ├• **Phython**: `{python_version()}`\n"
        f"  ├• **Pyrogram**: `{__version__}`\n"
        f"  └• **Geez Library**: `{gver}`\n\n"
        f"©️2023 [Geez|RAM Support](t.me/GeezRam)\n"
    )

@Client.on_message(filters.command(["geez"], cmds) & filters.me)
async def module_help(client: Client, message: Message):
    await logging(client)
    cmd = message.command
    help_arg = ""
    bot_username = (await app.get_me()).username
    if len(cmd) > 1:
        help_arg = "".join(cmd[1:])
    elif not message.reply_to_message and len(cmd) == 1:
        try:
            nice = await client.get_inline_bot_results(bot=bot_username, query="Alive")
            await asyncio.gather(
                message.delete(),
                client.send_inline_bot_result(
                    message.chat.id, nice.query_id, nice.results[0].id
                ),
            )
        except BaseException as e:
            print(f"{e}")

@Client.on_message(
    filters.command(["alive", "awake"], cmds) & (filters.me | filters.user(SUDO_USER))
)
async def alive(client: Client, message: Message):
    xx = await message.reply_text("⚡️")
    await logging(client)
    await asyncio.sleep(3)
    try:
       await message.delete()
    except:
       pass
    send = client.send_video if alive_logo.endswith(f"{cmds}mp4") else client.send_photo
    xd = (f"{txt}")
    try:
        await asyncio.gather(
            xx.delete(),
            send(
                message.chat.id,
                alive_logo,
                caption=xd,
                reply_to_message_id=ReplyCheck(message),
            ),
        )
    except BaseException:
        await xx.edit(xd, disable_web_page_preview=True)

@Client.on_message(filters.command("repo", cmds) & filters.me)
async def repo(bot: Client, message: Message):
    await asyncio.sleep(1)
    await message.edit("Mengambil informasi repo.....")
    await asyncio.sleep(1)
    await message.edit("repo Geez-Pyro Official: \n\n\nhttps://github.com/hitokizzy/Geez-Pyro")


@Client.on_message(filters.command("creator", cmds) & filters.me)
async def creator(bot: Client, message: Message):
    await message.edit("https://github.com/vckyou")


@Client.on_message(filters.command("id", cmds) & filters.me)
async def get_id(bot: Client, message: Message):
    file_id = None
    user_id = None

    if message.reply_to_message:
        rep = message.reply_to_message

        if rep.audio:
            file_id = f"**File ID**: `{rep.audio.file_id}`"
            file_id += "**File Type**: `audio`"

        elif rep.document:
            file_id = f"**File ID**: `{rep.document.file_id}`"
            file_id += f"**File Type**: `{rep.document.mime_type}`"

        elif rep.photo:
            file_id = f"**File ID**: `{rep.photo.file_id}`"
            file_id += "**File Type**: `photo`"

        elif rep.sticker:
            file_id = f"**Sicker ID**: `{rep.sticker.file_id}`\n"
            if rep.sticker.set_name and rep.sticker.emoji:
                file_id += f"**Sticker Set**: `{rep.sticker.set_name}`\n"
                file_id += f"**Sticker Emoji**: `{rep.sticker.emoji}`\n"
                if rep.sticker.is_animated:
                    file_id += f"**Animated Sticker**: `{rep.sticker.is_animated}`\n"
                else:
                    file_id += "**Animated Sticker**: `False`\n"
            else:
                file_id += "**Sticker Set**: __None__\n"
                file_id += "**Sticker Emoji**: __None__"

        elif rep.video:
            file_id = f"**File ID**: `{rep.video.file_id}`\n"
            file_id += "**File Type**: `video`"

        elif rep.animation:
            file_id = f"**File ID**: `{rep.animation.file_id}`\n"
            file_id += "**File Type**: `GIF`"

        elif rep.voice:
            file_id = f"**File ID**: `{rep.voice.file_id}`\n"
            file_id += "**File Type**: `Voice Note`"

        elif rep.video_note:
            file_id = f"**File ID**: `{rep.animation.file_id}`\n"
            file_id += "**File Type**: `Video Note`"

        elif rep.location:
            file_id = "**Location**:\n"
            file_id += f"**longitude**: `{rep.location.longitude}`\n"
            file_id += f"**latitude**: `{rep.location.latitude}`"

        elif rep.venue:
            file_id = "**Location**:\n"
            file_id += f"**longitude**: `{rep.venue.location.longitude}`\n"
            file_id += f"**latitude**: `{rep.venue.location.latitude}`\n\n"
            file_id += "**Address**:\n"
            file_id += f"**title**: `{rep.venue.title}`\n"
            file_id += f"**detailed**: `{rep.venue.address}`\n\n"

        elif rep.from_user:
            user_id = rep.from_user.id

    if user_id:
        if rep.forward_from:
            user_detail = (
                f"**Forwarded User ID**: `{message.reply_to_message.forward_from.id}`\n"
            )
        else:
            user_detail = f"**User ID**: `{message.reply_to_message.from_user.id}`\n"
        user_detail += f"**Message ID**: `{message.reply_to_message.id}`"
        await message.edit(user_detail)
    elif file_id:
        if rep.forward_from:
            user_detail = (
                f"**Forwarded User ID**: `{message.reply_to_message.forward_from.id}`\n"
            )
        else:
            user_detail = f"**User ID**: `{message.reply_to_message.from_user.id}`\n"
        user_detail += f"**Message ID**: `{message.reply_to_message.id}`\n\n"
        user_detail += file_id
        await message.edit(user_detail)

    else:
        await message.edit(f"**Chat ID**: `{message.chat.id}`")




add_command_help(
    "misc",
    [
        [f"{cmds}alive", "Check if the bot is alive or not."],
        [f"{cmds}repo", "Display the repo of this userbot."],
        [f"{cmds}creator", "Show the creator of this userbot."],
        [f"{cmds}id", "Send id of what you replied to."],
    ],
)

add_command_help(
    "system",
    [
        [f"{cmds}restart", "You are retarded if you do not know what this does."],
        [f"{cmds}shutdown", "You are retarded if you do not know what this does."],
    ],
)
