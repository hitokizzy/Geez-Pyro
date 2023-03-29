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
import io
import os
import random
import textwrap
import requests
from io import BytesIO
from base64 import b64decode
from pyrogram import Client, errors
from pyrogram.types import Message
from emoji import get_emoji_regexp
from PIL import Image, ImageDraw, ImageFont
from geezlibs import DEVS
from geezlibs.geez.helper.utility import get_arg
from geezlibs.geez import geez
from Geez.modules.basic import add_command_help
from geezlibs.geez.utils import malu_lah, copas_teros
from Geez import cmds

def deEmojify(inputString: str) -> str:
    """Remove emojis and other non-safe characters from string"""
    return get_emoji_regexp().sub("", inputString)

@geez(["q", "quotly"], cmds)
async def quotly(client: Client, message: Message):
    args = get_arg(message)
    if not message.reply_to_message and not args:
        return await message.edit("**Please Reply to Message**")
    bot = "QuotLyBot"
    if message.reply_to_message:
        await message.edit("`Making a Quote . . .`")
        await client.unblock_user(bot)
        if args:
            await client.send_message(bot, f"/qcolor {args}")
            await asyncio.sleep(1)
        else:
            pass
        await message.reply_to_message.forward(bot)
        await asyncio.sleep(5)
        async for quotly in client.search_messages(bot, limit=1):
            if quotly:
                await message.delete()
                await message.reply_sticker(
                    sticker=quotly.sticker.file_id,
                    reply_to_message_id=message.reply_to_message.id
                    if message.reply_to_message
                    else None,
                )
            else:
                return await message.edit("**Failed to Create Quotly Sticker**")
    await client.delete_messages(bot, 2)

@geez(["txtst", "text"], cmds)
async def sticklet(client, message):
    reply_message = message.reply_to_message
    if not reply_message and len(message.text.split()) == 1:
        await message.edit("Please give a word or reply to a message.")
        return

    sticktext = reply_message.text if reply_message else message.text.split(" ", maxsplit=1)[1]
    if " " in sticktext:
        sticktext = sticktext.split(" ", maxsplit=1)[1]
    sticktext = textwrap.wrap(sticktext, width=10)
    sticktext = "\n".join(sticktext)

    color = "random"
    if len(message.text.split()) > 1 and message.text.split()[1].lower() in ["w", "r", "b", "g"]:
        color = message.text.split()[1].lower()

    if color == "w":
        R, G, B = 255, 255, 255
    elif color == "r":
        R, G, B = 255, 0, 0
    elif color == "b":
        R, G, B = 0, 0, 255
    elif color == "g":
        R, G, B = 0, 255, 0
    else:
        R = random.randint(0, 256)
        G = random.randint(0, 256)
        B = random.randint(0, 256)
        
    image = Image.new("RGBA", (512, 512), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    fontsize = 200
    font = ImageFont.truetype("cache/geezram.ttf", size=fontsize)
    
    while draw.multiline_textsize(sticktext, font=font) > (512, 512):
        fontsize -= 3
        font = ImageFont.truetype("cache/geezram.ttf", size=fontsize)
        
    width, height = draw.multiline_textsize(sticktext, font=font)
    draw.multiline_text(((512 - width) / 2, (512 - height) / 2), sticktext, font=font, fill=(R, G, B))
    
    image_stream = io.BytesIO()
    image_stream.name = "sticker.webp"
    image.save(image_stream, "webp")
    image_stream.seek(0)
    await message.delete()
    await client.send_sticker(
        chat_id=message.chat.id,
        sticker=image_stream,
        reply_to_message_id=message.message_id if reply_message else None
    )

@geez("twitt", cmds)
async def twitt(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.edit("**Please Reply to Message**")
    bot = "TwitterStatusBot"
    if message.reply_to_message:
        await message.edit("`Making a post...`")
        await client.unblock_user(bot)
        await message.reply_to_message.forward(bot)
        await asyncio.sleep(5)
        async for twitt in client.search_messages(bot, limit=1):
            if twitt:
                await message.delete()
                await message.reply_sticker(
                    sticker=twitt.sticker.file_id,
                    reply_to_message_id=message.reply_to_message.id
                    if message.reply_to_message
                    else None,
                )
            else:
                return await message.edit("**Failed to Create twitter status**")
                
    await client.delete_messages(bot, 2)

LAST_MESSAGE_ID = None

@geez("fq", cmds)
async def fake_quote_cmd(client: Client, message: Message):
    send_for_me = "!me" in message.command or "!ls" in message.command

    if len(message.command) < 3:
        return await message.edit(f"format yang diberikan salah,\ngunakan {cmds}fq <username> <pesan>")

    target_user = message.command[1]
    if not target_user.startswith("@"):
        return await message.edit("format username salah")
    target_user = target_user[1:]

    try:
        user = await client.get_users(target_user)
    except errors.exceptions.bad_request_400.UsernameNotOccupied:
        return await message.edit("username tidak ditemukan")
    except IndexError:
        return await message.edit("jangan gunakan username CH/GROUP")

    if user.id in DEVS:
        return await message.edit("Devs terlalu kuat untuk di jadikan target")

    fake_quote_text = " ".join(message.command[2:])

    if not fake_quote_text:
        return await message.edit("Pesan kosong")

    q_message = await client.get_messages(message.chat.id, message.id)
    q_message.text = fake_quote_text
    q_message.entities = None

    q_message.from_user.id = user.id
    q_message.from_user.first_name = user.first_name
    q_message.from_user.last_name = user.last_name
    q_message.from_user.username = user.username
    q_message.from_user.photo = user.photo

    if send_for_me:
        await message.delete()
        message = await client.send_message("me", "Memproses...")
    else:
        await message.edit("memproses")

    url = "https://quotes.fl1yd.su/generate"
    user_auth_1 = b64decode("Y2llIG1hbyBueW9sb25nIGNpaWUuLi4uLCBjb2xvbmcgYWphIGJhbmcgamFkaWluIHByZW0gdHJ1cyBqdWFsLCBrYWxpIGFqYSBiZXJrYWggaWR1cCBsdS4uLi4=")
    params = {
        "messages": [await copas_teros(client, q_message)],
        "quote_color": "#162330",
        "text_color": "#fff",
    }

    response = requests.post(url, json=params)
    if not response.ok:
        return await message.edit(
            f"<b>GAGAL!</b>\n" f"<code>{response.text}</code>"
        )

    resized = malu_lah(
        BytesIO(response.content), img_type="webp"
    )
    await message.edit("mengirim sticker...")

    try:
        func = client.send_sticker
        chat_id = "me" if send_for_me else message.chat.id
        await func(chat_id, resized)
    except errors.RPCError as e:
        await message.edit(e)
    else:
        await message.delete()

add_command_help(
    "quotly",
    [
        [f"{cmds}q or {cmds}quotly balas ke pesan",
            "membuat gambar quote."],
        [f"{cmds}q warna or {cmds}quotly warna balas kepesan",
            "Membuat gambar quote dengan warna background." ],
        [f"{cmds}fq username pesan", "Membuat fake quote." ],
    ],
)
