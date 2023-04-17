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

import os
import random
import glob
from phlogo import generate
from blackpink import blackpink
from PIL import Image, ImageDraw, ImageFont
from pyrogram import Client, enums
from pyrogram.types import Message
from geezlibs.geez import geez
from Geez import cmds
from Geez.modules.basic import add_command_help

@geez("phlogo", cmds)
async def make_logog(client: Client, message: Message):
    msg = await message.edit("`processing...`")
    try:
        match = message.text.split(maxsplit=1)[1]
    except IndexError:
        return await msg.edit("`Provide a name to make logo...`")
    if len(match.split()) >= 2:
        first, last = match.split()[:2]
    else:
        last = match
    logo = blackpink(match)
    name = "geezram.png"
    logo.save(name)
    await message.delete(msg)
    await client.send_photo(
        message.chat.id, photo=name, reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None
    )
    os.remove(name)

@geez("blink", cmds)
async def make_blink(client: Client, message: Message):
    msg = await message.edit("`processing...`")
    try:
        match = message.text.split(maxsplit=1)[1]
    except IndexError:
        return await msg.edit("`Provide a name to make logo...`")
    logo = blackpink(match)
    name = "geezram.png"
    logo.save(name)
    await message.delete(msg)
    await client.send_photo(
        message.chat.id, photo=name, reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None
    )
    os.remove(name)

@geez("logo", cmds)
async def logo_gen(client, message):
    xx = await message.reply_text("`processing...`")
    name = message.text.split(" ", 1)[1]
    if not name:
        await xx.edit(f"`Sediakan beberapa teks untuk digambar!\nContoh: {cmds}logo <nama Anda>!`")
        return
    bg_, font_ = "", ""
    if message.reply_to_message:
        temp = message.reply_to_message
        if temp.media:
            if temp.document:
                if "font" in temp.document.mime_type:
                    font_ = await temp.download()
                elif (".ttf" in temp.document.file_name) or (".otf" in temp.document.file_name):
                    font_ = await temp.download()
            elif temp.photo:
                bg_ = await temp.download()
    else:
        pics = []
        async for i in client.search_messages("AllLogoHyper", filter=enums.MessagesFilter.PHOTO
                ):
            if i.photo:
                pics.append(i)
        id_ = random.choice(pics)
        bg_ = await id_.download()
        fpath_ = glob.glob("cache/default.ttf")
        font_ = random.choice(fpath_)
    if not bg_:
        pics = []
        async for i in client.search_messages("AllLogoHyper", filter=enums.MessagesFilter.PHOTO
                ):
            if i.photo:
                pics.append(i)
        id_ = random.choice(pics)
        bg_ = await id_.download()
    if not font_:
        fpath_ = glob.glob("cache/default.ttf")
        font_ = random.choice(fpath_)
    if len(name) <= 8:
        fnt_size = 120
        strke = 10
    elif len(name) >= 9:
        fnt_size = 50
        strke = 5
    else:
        fnt_size = 100
        strke = 20
    img = Image.open(bg_)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_, fnt_size)
    w, h = draw.textsize(name, font=font)
    h += int(h * 0.21)
    image_width, image_height = img.size
    draw.text(
        ((image_width - w) / 2, (image_height - h) / 2),
        name,
        font=font,
        fill=(255, 255, 255),
    )
    x = (image_width - w) / 2
    y = (image_height - h) / 2
    draw.text((x, y), name, font=font, fill="white",
              stroke_width=strke, stroke_fill="black")
    flnme = "logo.png"
    img.save(flnme, "png")
    await xx.edit("`Uploading`")
    if os.path.exists(flnme):
        await message.delete(xx)
        await client.send_photo(
            chat_id=message.chat.id,
            photo=flnme,
            caption=f"Logo by {client.me.mention}",
        )
        os.remove(flnme)
        await xx.delete()
    if os.path.exists(bg_):
        os.remove(bg_) 
    if os.path.exists(font_):
        if not font_.startswith("cache/default.ttf"):
            os.remove(font_)

add_command_help(
    "logo",
    [
        [f"{cmds}logo <nama>", "membuat logo dengan background random."],
        [f"{cmds}phlogo <nama>", "membuat logo dengan tema PornHub."],
        [f"{cmds}blink <nama>", "membuat logo dengan tema Blackpink."],
    ],
)