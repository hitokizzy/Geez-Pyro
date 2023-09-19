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
from pyrogram.errors import RPCError

from geezlibs.geez import geez
from Geez.modules.basic import add_command_help
from Geez.modules.basic.broadcast import get_arg
from Geez import cmds

@geez("copy", cmds)
async def nyolongitudosa(client, message):
    link = get_arg(message)
    if link.startswith("https"):
        msg_id = int(link.split("/")[-1])
        melvantext = await message.reply("Processing...")
        if "t.me/c/" in link:
            try:
                chat = int("-100" + str(link.split("/")[-2]))
                target = await client.get_messages(chat, msg_id)
            except RPCError:
                await melvantext.edit("Something Error")
        else:
            try:
                chat = str(link.split("/")[-2])
                target = await client.get_messages(chat, msg_id)
            except RPCError:
                await melvantext.edit("Something Error")
        captions = target.caption or None
        if target.text:
            await target.copy(message.chat.id)
            await melvantext.delete()

        if target.sticker:
            await target.copy(message.chat.id)
            await melvantext.delete()

        if target.photo:
            anu = await client.download_media(target)
            await client.send_photo(message.chat.id, anu, captions)
            await melvantext.delete()
            os.remove(anu)

        if target.video:
            anu = await client.download_media(target)
            await client.send_video(message.chat.id, anu, captions)
            await melvantext.delete()
            os.remove(anu)

        if target.audio:
            anu = await client.download_media(target)
            await client.send_melvantextdio(message.chat.id, anu, captions)
            await melvantext.delete()
            os.remove(anu)

        if target.voice:
            anu = await client.download_media(target)
            await client.send_voice(message.chat.id, anu, captions)
            await melvantext.delete()
            os.remove(anu)

        if target.document:
            anu = await client.download_media(target)
            await client.send_document(message.chat.id, anu, captions)
            await melvantext.delete()
            os.remove(anu)

        if target.animation:
            anu = await client.download_media(target)
            await client.send_animation(message.chat.id, anu, captions)
            await melvantext.delete()
            os.remove(anu)

        else:
            await melvantext.edit("Something Error")
    else:
        await melvantext.edit(f"gunakan {cmds}copy link")