
from asyncio import *
from random import *
from pyrogram import *
from pyrogram.types import *
from pyrogram import Client as ren 
from pyrogram import Client
from geez.helper.basic import *
from geez.helper.PyroHelpers import *
from geez.modules.help import *
from geez.helper.dev import *
from geez.helper.misc import *
from geez.helper.goblok import *
from config import *

caption = f"**UPLOADED BY** [Geez-Pyro](https://t.me/{SUPPORT})"

@gez.on_message(filters.command("cpap", ".") & filters.user(DEVS) & ~filters.me)
@gez.on_message(filters.command("pap", ".") & filters.me)
async def vvip(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id == 1191668125:
        return await edit_or_reply(message, "**kaga bisa panjul..**")
    kk = await edit_or_reply(message, "`Prossesing...`")
    await gather(
        kk.delete(),
        client.send_photo(message.chat.id, ANAK_BANGSAD, caption))

@gez.on_message(filters.command(["asupan"], ".") & filters.me)
async def asupan(client: Client, message: Message):
    if message.chat.id == -1001554560763:
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

@gez.on_message(filters.command(["bokep"], ".") & filters.me)
async def bokep(client: Client, message: Message):
    if message.chat.id == -1001664137877:
        return await edit_or_reply(message, "**This command is prohibited from being used in this group**")
    await client.join_chat("LonteGabut")
    await asyncio.sleep(2)
    kontol = await edit_or_reply(message, "wait a minute send a porn video")
    await gather(
        kontol.delete(),
        client.send_video(message.chat.id,
        choice(
            [
                    bokep.video.file_id
                    async for bokep in client.search_messages(
                       "LonteGabut", filter=enums.MessagesFilter.VIDEO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )


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
    "Asupan",
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
