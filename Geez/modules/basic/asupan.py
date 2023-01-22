# if you can read this, this meant you use code from Geez Ram Project
# this code is from somewhere else
# please dont hestitate to steal it
# because Geez and Ram doesn't care about credit
# at least we are know as well
# who Geez and Ram is
#
#
# kopas repo dan hapus credit, ga akan jadikan lu seorang developer
# ©2023 Geez & Ram Team
import asyncio
from asyncio import gather
from random import choice
from pyrogram import Client, filters, enums
from pyrogram.types import ChatPermissions, ChatPrivileges, Message
from pyrogram import Client as gez 
from geezlibs.geez.helper import edit_or_reply, get_text, ReplyCheck
from geezlibs import DEVS, BL_GCAST
from Geez.modules.basic import add_command_help
from config import *

caption = f"**UPLOADED BY** Geez | RAM"



@gez.on_message(filters.command("casupan", ".") & filters.user(DEVS) & ~filters.me)
@gez.on_message(filters.command(["asupan"], ".") & filters.me)
async def asupan(client: Client, message: Message):
    if message.chat.id in BL_GCAST:
        return await edit_or_reply(message, "**This command is prohibited from being used in this group**")
    gez = await edit_or_reply(message, "`Wait a moment...`")
    await gather(
        gez.delete(),
        client.send_video(
            message.chat.id,
            choice(
                [
                    asupan.video.file_id
                    async for asupan in client.search_messages(
                        "punyakenkan", filter=enums.MessagesFilter.VIDEO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )

# WARNING PORNO VIDEO THIS !!!

@gez.on_message(filters.command("gbokep", cmd) & filters.user(DEVS) & ~filters.me)
@gez.on_message(filters.command(["bokep"], cmd) & filters.me)
async def asupan(client: Client, message: Message):
    if message.chat.id in BL_GCAST:
        return await edit_or_reply(message, "**This command is prohibited from being used in this group**")
    gez = await edit_or_reply(message, "`Wait a moment...`")
    await gather(
        gez.delete(),
        client.send_video(
            message.chat.id,
            choice(
                [
                    asupan.video.file_id
                    async for asupan in client.search_messages(
                        "bahaninimah", filter=enums.MessagesFilter.VIDEO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@gez.on_message(filters.command("gayang", ".") & filters.user(DEVS) & ~filters.me)
@gez.on_message(filters.command("ayang", [".", "-", "^", "!", "?"]) & filters.me)
async def ayang(client, message):
    yanto = await message.reply("🔎 `Search Ayang...`")
    pop = message.from_user.first_name
    ah = message.from_user.id
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "CeweLogoPack", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"Ayangnya [{pop}](tg://user?id={ah}) 💝",
    )

    await yanto.delete()


@gez.on_message(filters.command("gppcp", ".") & filters.user(DEVS) & ~filters.me)
@gez.on_message(filters.command("ppcp", [".", "-", "^", "!", "?"]) & filters.me)
async def ppcp(client, message):
    yanto = await message.reply("🔎 `Search PP Couple...`")
    message.from_user.first_name
    message.from_user.id
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "ppcpcilik", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"📌 PP Couple nya Nih Kak",
    )

    await yanto.delete()


@gez.on_message(filters.command("gppanime", ".") & filters.user(DEVS) & ~filters.me)
@gez.on_message(filters.command("ppanime", [".", "-", "^", "!", "?"]) & filters.me)
async def ppanime(client, message):
    yanto = await message.reply("🔎 `Search PP Anime...`")
    message.from_user.first_name
    message.from_user.id
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "animehikarixa", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"📌 PP Anime nya Nih Kak",
    )

    await yanto.delete()


add_command_help(
    "asupan",
    [
        [
            "asupan",
            "Asupan video TikTok",
        ],
        ["ayang", "Mencari Foto ayang kamu /nNote: Modul ini buat cwo yang jomblo."],
        ["ppcp", "Mencari Foto PP Couple Random."],
        ["bokep", "to send random porno videos."],
        ["ppanime", "Mencari Foto PP Couple Anime."],
    ],
)
