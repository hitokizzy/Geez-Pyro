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

from pyrogram import Client
from pyrogram.types import Message
from geezlibs.geez import geez
from Geez.modules.basic import add_command_help
from Geez import cmds


@geez("pamer", cmds)
async def pamer(client: Client, message: Message):
    await message.delete()
    fake = message.reply_to_message
    if not fake:
        await client.send_message("me", "`Mohon balas ke media.`")
    file_ = "**Pap timer.**" if not fake.caption else fake.caption
    if fake.text:
        await fake.copy("me")
        await message.delete()
    if fake.photo:
        meira = await fake.download()
        await client.send_photo("me", photo=meira, caption=file_)
        await message.delete()
        os.remove(meira)
    if fake.video:
        meira = await fake.download()
        await client.send_video("me", video=meira, caption=file_)
        await message.delete()
        os.remove(meira)
    if fake.audio:
        meira = await fake.download()
        await client.send_audio("me", audio=meira, caption=file_)
        await message.delete()
        os.remove(meira)
    if fake.voice:
        await client.send_voice("me", voice=meira, caption=file_)
        await message.delete()
        os.remove(meira)
    if fake.document:
        await client.send_document("me", document=meira, caption=file_)
        await message.delete()
        os.remove(meira)

add_command_help(
    "pamer",
    [
        [f"{cmds}pamer","Mengambil media dengan timmer (pap timmer) tidak bisa untuk media sekali lihat.",
        ],
    ],
)