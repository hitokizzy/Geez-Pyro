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
from pyrogram import Client, filters
from pyrogram.enums import ChatType, UserStatus
from pyrogram.types import Message
from Geez import SUDO_USER
from pyrogram.errors.exceptions.flood_420 import FloodWait

from Geez.modules.basic import add_command_help
from Geez import cmds

@Client.on_message(
    filters.command(["invite"], cmds) & (filters.me | filters.user(SUDO_USER))
)
async def inviteee(client: Client, message: Message):
    mg = await message.reply_text("`Adding Users!`")
    user_s_to_add = message.text.split(" ", 1)[1]
    if not user_s_to_add:
        await mg.edit("`Give Me Users To Add! Check Help Menu For More Info!`")
        return
    user_list = user_s_to_add.split(" ")
    try:
        await client.add_chat_members(message.chat.id, user_list, forward_limit=100)
    except BaseException as e:
        await mg.edit(f"`Unable To Add Users! \nTraceBack : {e}`")
        return
    await mg.edit(f"`Sucessfully Added {len(user_list)} To This Group / Channel!`")

@Client.on_message(
    filters.command(["inviteall"], cmds) & (filters.me | filters.user(SUDO_USER))
)
async def inv(client: Client, message: Message):
    ex = await message.reply_text("`Processing . . .`")
    text = message.text.split(" ", 1)
    queryy = text[1]
    chat = await client.get_chat(queryy)
    tgchat = message.chat
    await ex.edit_text(f"inviting users from {chat.username}")
    async for member in client.get_chat_members(chat.id):
        user = member.user
        zxb = [
            UserStatus.ONLINE,
            UserStatus.OFFLINE,
            UserStatus.RECENTLY,
            UserStatus.LAST_WEEK,
        ]
        if user.status in zxb:
            try:
                await client.add_chat_members(tgchat.id, user.id)
            except FloodWait as e:
                return
            except Exception as e:
                pass

@Client.on_message(filters.command("invitelink", cmds) & filters.me)
async def invite_link(client: Client, message: Message):
    um = await message.edit_text("`Processing...`")
    if message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        message.chat.title
        try:
            link = await client.export_chat_invite_link(message.chat.id)
            await um.edit(f"**Link Invite:** {link}")
        except Exception:
            await um.edit("Denied permission")


add_command_help(
    "invite",
    [
        [f"{cmds}invitelink","mengambil link group private. [Memerlukan wewenang Admin]",],
        [f"{cmds}invite @username", "invite pengguna ke group."],
        [f"{cmds}inviteall @username", "menambah member group secara masal (akun anda mungkin akan terbatasi/limit)."],
    ],
)
