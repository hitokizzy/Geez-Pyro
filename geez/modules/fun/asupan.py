
from asyncio import *
from random import *
from pyrogram import *
from pyrogram.types import *
from pyrogram import Client as gez 
from pyrogram import Client
from geez.helper.basic import *
from geez.helper.PyroHelpers import *
from geez.modules.help import *


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
    if message.chat.id in CHANNEL:
        return await edit_or_reply(message, "**This command is prohibited from being used in this group**")
    await client.join_chat("https://t.me/LonteGabut")
    await asyncio.sleep(2)
    kontol = await edit_or_reply(message, "wait a minute send a porn video")
    await gather(
        kontol.delete(),
        client.send_video(message.chat.id,
        choice(
            [
                    bokep.video.file_id
                    async for bokep in client.search_messages(
                       -1001664137877, filter=enums.MessagesFilter.VIDEO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )


add_command_help(
    "asupan",
    [
        ["asupan", "to send random asupan videos."],
        ["bokep", "to send random porno videos."],
    ],
)
