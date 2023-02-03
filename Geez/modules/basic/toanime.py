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
import time
from pyrogram import Client, filters, enums
from pyrogram.types import Message
from geezlibs import logging
from geezlibs.geez.helper.basic import edit_or_reply
from Geez.modules.basic import add_command_help
from Geez import cmds

@Client.on_message(filters.command("toanime", cmds) & filters.me)
async def convert_image(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.edit("**Please Reply to photo**")
    if message.reply_to_message:
        await message.edit("`processing ...`")
        await logging(client)
    reply_message = message.reply_to_message
    photo = reply_message.photo.file_id
    bot = "qq_2d_ai_bot"
    await client.send_photo(bot, photo=photo)
    await asyncio.sleep(18)
    async for result in client.search_messages(bot, limit=1):
        if result.photo:
            await message.edit("uploading...")
            converted_image_file = await client.download_media(result)
            await client.send_photo(message.chat.id, converted_image_file, caption="Powered by Geez Pyro")
            await message.delete()
        else:
            await message.edit("`error message ...`")

add_command_help(
    "anime ai",
    [
        [f"{cmds}toanime", "convert foto ke anime menggunakan ai bot"],
    ],
)