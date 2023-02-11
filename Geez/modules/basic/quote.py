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
import random
import textwrap
from pyrogram import Client, filters, enums
from pyrogram.types import Message
from pyrogram.errors import YouBlockedUser
from emoji import get_emoji_regexp
from PIL import Image, ImageDraw, ImageFont
from geezlibs.geez.helper.utility import get_arg
from Geez.modules.basic import add_command_help
from geezlibs.geez.helper.PyroHelpers import ReplyCheck
from Geez import cmds

def deEmojify(inputString: str) -> str:
    """Remove emojis and other non-safe characters from string"""
    return get_emoji_regexp().sub("", inputString)

@Client.on_message(filters.me & filters.command(["q", "quotly"], cmds))
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

@Client.on_message(filters.me & filters.command(["txtst", "textsticker"], cmds))
async def sticklet(client, message):
    R = random.randint(0, 256)
    G = random.randint(0, 256)
    B = random.randint(0, 256)
    reply_message = message.reply_to_message
    if reply_message:
        sticktext = reply_message.text
    elif len(message.text.split(" ")) >= 2:
        sticktext = message.text.split(" ", maxsplit=1)[1]
    else:
        ain = await message.edit("Please give a word or reply to a message.")
        return
        
    sticktext = textwrap.wrap(sticktext, width=10)
    sticktext = "\n".join(sticktext)
    
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
    await ain.delete()
    await client.send_sticker(
        chat_id=message.chat.id,
        sticker=image_stream,
        reply_to_message_id=ReplyCheck(message)
    )

@Client.on_message(filters.command(["twitt"], cmds) & filters.me)
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

add_command_help(
    "quotly",
    [
        [f"{cmds}q or {cmds}quotly",
            "membuat gambar quote."],
        [f"{cmds}q <warna> or {cmds}quotly <warna>",
            "Membuat gambar quote dengan warna background." ],
    ],
)
