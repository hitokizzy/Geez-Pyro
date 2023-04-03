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
import asyncio
import os
from pyrogram import Client
from pyrogram.enums import MessagesFilter
from pyrogram.types import Message
from geezlibs.geez import geez
from Geez import cmds

@geez("toanime", cmds)
async def convert_image(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.edit("**Mohon Balas Pesan Ini Ke Media**")
    if message.reply_to_message:
        await message.edit("`processing ...`")
    reply_message = message.reply_to_message
    photo = reply_message.photo.file_id
    bot = "qq_neural_anime_bot"
    xxx = await client.send_photo(bot, photo=photo)
    await asyncio.sleep(30)
    await message.delete()
    async for result in client.search_messages(bot, filter=MessagesFilter.PHOTO, limit=1):
        if result.photo:
            await client.send_photo(message.chat.id, result.photo.file_id, caption="**Powered by GeezProjects**")
            await result.delete()
            await xxx.delete()

@geez("gif", cmds)
async def sticker_to_gif(client: Client, message: Message):
    process = await message.reply("Memproses...")
    if not message.reply_to_message:
        return await process.edit("Harap balas ke Stiker...")
    await process.edit("Downloading...")
    file = await client.download_media(
        message.reply_to_message,
        f"geezram_{message.from_user.id}.mp4",
    )
    try:
        await client.send_animation(
            message.chat.id, file, reply_to_message_id=message.id
        )
        os.remove(file)
        await process.delete()
    except Exception as e:
        await process.edit(e)
