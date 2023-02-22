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
from pyrogram import Client
from pyrogram.enums import MessagesFilter
from pyrogram.types import Message
from geezlibs import logging
from geezlibs.geez import geez
from geezlibs.geez.helper.basic import edit_or_reply
from Geez.modules.basic import add_command_help
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
    await asyncio.sleep(20)
    await message.delete()
    async for result in client.search_messages(bot, filter=MessagesFilter.PHOTO, limit=1):
        if result.photo:
            await client.send_photo(message.chat.id, result.photo.file_id, caption="**Powered by GeezProjects**")
            await result.delete()
            await xxx.delete()
