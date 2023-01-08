import os
import sys
from re import sub
from time import time
import asyncio
from requests import get
from pyrogram import Client, filters, enums
from pyrogram.errors import ChatAdminRequired
from pyrogram.types import ChatPermissions, ChatPrivileges, Message


DEVS = get("https://raw.githubusercontent.com/vckyou/Reforestation/master/DEVS.json")
admins_in_chat = {}

from geez.modules.help import add_command_help
from geez.modules.basic.profile import extract_user

async def extract_user_and_reason(message, sender_chat=False):
    args = message.text.strip().split()
    text = message.text
    user = None
    reason = None
    if message.reply_to_message:
        reply = message.reply_to_message
        if not reply.from_user:
            if (
                reply.sender_chat
                and reply.sender_chat != message.chat.id
                and sender_chat
            ):
                id_ = reply.sender_chat.id
            else:
                return None, None
        else:
            id_ = reply.from_user.id

        if len(args) < 2:
            reason = None
        else:
            reason = text.split(None, 1)[1]
        return id_, reason

    if len(args) == 2:
        user = text.split(None, 1)[1]
        return await extract_userid(message, user), None

    if len(args) > 2:
        user, reason = text.split(None, 2)[1:]
        return await extract_userid(message, user), reason

    return user, reason


async def list_admins(client: Client, chat_id: int):
    global admins_in_chat
    if chat_id in admins_in_chat:
        interval = time() - admins_in_chat[chat_id]["last_updated_at"]
        if interval < 3600:
            return admins_in_chat[chat_id]["data"]

    admins_in_chat[chat_id] = {
        "last_updated_at": time(),
        "data": [
            member.user.id
            async for member in client.get_chat_members(
                chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS
            )
        ],
    }
    return admins_in_chat[chat_id]["data"]




unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)


@Client.on_message(
    filters.group & filters.command(["setchatphoto", "setgpic"], ".") & filters.me
)
async def set_chat_photo(client: Client, message: Message):
    zuzu = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    can_change_admin = zuzu.can_change_info
    can_change_member = message.chat.permissions.can_change_info
    if not (can_change_admin or can_change_member):
        await message.edit_text("Anda bukan admin, anda hanya remahan rengginang disini")
    if message.reply_to_message:
        if message.reply_to_message.photo:
            await client.set_chat_photo(
                message.chat.id, photo=message.reply_to_message.photo.file_id
            )
            return
    else:
        await message.edit_text("Reply ke gambar buat set!")



@Client.on_message(filters.group & filters.command("ban", ".") & filters.me)
async def member_ban(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    rd = await message.edit_text("`Processing...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await rd.edit("Saya tidak punya wewenang")
    if not user_id:
        return await rd.edit("tidak dapat menemukan pengguna.")
    if user_id == client.me.id:
        return await rd.edit("haa.. gimana ???.")
    if user_id in DEVS:
        return await rd.edit("Saya tidak bisa ban Devs saya!")
    if user_id in (await list_admins(client, message.chat.id)):
        return await rd.edit("Saya tidak bisa banned Admin.")
    try:
        mention = (await client.get_users(user_id)).mention
    except IndexError:
        mention = (
            message.reply_to_message.sender_chat.title
            if message.reply_to_message
            else "Anon"
        )
    msg = (
        f"**Banned User:** {mention}\n"
        f"**Banned By:** {message.from_user.mention if message.from_user else 'Anon'}\n"
    )
    if message.command[0][0] == "d":
        await message.reply_to_message.delete()
    if reason:
        msg += f"**Reason:** {reason}"
    await message.chat.ban_member(user_id)
    await rd.edit(msg)



@Client.on_message(filters.group & filters.command("unban", ".") & filters.me)
async def member_unban(client: Client, message: Message):
    reply = message.reply_to_message
    rd = await message.edit_text("`Processing...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await rd.edit("Saya tidak punya wewenang")
    if reply and reply.sender_chat and reply.sender_chat != message.chat.id:
        return await rd.edit("channel tidak bisa dibanned")

    if len(message.command) == 2:
        user = message.text.split(None, 1)[1]
    elif len(message.command) == 1 and reply:
        user = message.reply_to_message.from_user.id
    else:
        return await rd.edit(
            "Berikan Username atau reply pesannya."
        )
    await message.chat.unban_member(user)
    umention = (await client.get_users(user)).mention
    await rd.edit(f"Unbanned! {umention}")



@Client.on_message(filters.command(["pin", "unpin"], ".") & filters.me)
async def pin_message(client: Client, message):
    if not message.reply_to_message:
        return await message.edit_text("Balas pesan untuk pin/unpin.")
    rd = await message.edit_text("`Processing...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_pin_messages:
        return await rd.edit("Saya tidak punya wewenang")
    r = message.reply_to_message
    if message.command[0][0] == "u":
        await r.unpin()
        return await rd.edit(
            f"**Unpinned [this]({r.link}) message.**",
            disable_web_page_preview=True,
        )
    await r.pin(disable_notification=True)
    await rd.edit(
        f"**Pinned [this]({r.link}) message.**",
        disable_web_page_preview=True,
    )


@Client.on_message(filters.command("mute", ".") & filters.me)
async def mute(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message)
    rd = await message.edit_text("`Processing...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await rd.edit("Saya tidak punya wewenang")
    if not user_id:
        return await rd.edit("Tidak dapat menemukan pengguna.")
    if user_id == client.me.id:
        return await rd.edit("ha?? gimana....")
    if user_id in DEVS:
        return await rd.edit("saya tidak bisa mute devs saya!")
    if user_id in (await list_admins(client, message.chat.id)):
        return await rd.edit("saya tidak bisa mute Admin.")
    mention = (await client.get_users(user_id)).mention
    msg = (
        f"**Muted User:** {mention}\n"
        f"**Muted By:** {message.from_user.mention if message.from_user else 'Anon'}\n"
    )
    if reason:
        msg += f"**Reason:** {reason}"
    await message.chat.restrict_member(user_id, permissions=ChatPermissions())
    await rd.edit(msg)



@Client.on_message(filters.group & filters.command("unmute", ".") & filters.me)
async def unmute(client: Client, message: Message):
    user_id = await extract_user(message)
    rd = await message.edit_text("`Processing...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await rd.edit("Saya tidak punya wewenangs")
    if not user_id:
        return await rd.edit("tidak dapat menemukan pengguna.")
    await message.chat.restrict_member(user_id, permissions=unmute_permissions)
    umention = (await client.get_users(user_id)).mention
    await rd.edit(f"Unmuted! {umention}")


@Client.on_message(filters.command(["kick", "dkick"], ".") & filters.me)
async def kick_user(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message)
    rd = await message.edit_text("`Processing...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await rd.edit("Saya tidak punya wewenang")
    if not user_id:
        return await rd.edit("tidak dapat menggunakan pengguna.")
    if user_id == client.me.id:
        return await rd.edit("lah, au yaaa....")
    if user_id == DEVS:
        return await rd.edit("saya tdak bisa kick developers saya.")
    if user_id in (await list_admins(client, message.chat.id)):
        return await rd.edit("saya tidak bisa kick Admini.")
    mention = (await client.get_users(user_id)).mention
    msg = f"""
**Kicked User:** {mention}
**Kicked By:** {message.from_user.mention if message.from_user else 'Anon'}"""
    if message.command[0][0] == "d":
        await message.reply_to_message.delete()
    if reason:
        msg += f"\n**Reason:** `{reason}`"
    try:
        await message.chat.ban_member(user_id)
        await rd.edit(msg)
        await asyncio.sleep(1)
        await message.chat.unban_member(user_id)
    except ChatAdminRequired:
        return await rd.edit("**Maaf Anda Bukan admin**")


@Client.on_message(
    filters.group & filters.command(["promote", "fullpromote"], ".") & filters.me
)
async def promotte(client: Client, message: Message):
    user_id = await extract_user(message)
    umention = (await client.get_users(user_id)).mention
    rd = await message.edit_text("`Processing...`")
    if not user_id:
        return await rd.edit("tidak dapat menemukan pengguna.")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_promote_members:
        return await rd.edit("Saya tidak punya wewenang")
    if message.command[0][0] == "f":
        await message.chat.promote_member(
            user_id,
            privileges=ChatPrivileges(
                can_manage_chat=True,
                can_delete_messages=True,
                can_manage_video_chats=True,
                can_restrict_members=True,
                can_change_info=True,
                can_invite_users=True,
                can_pin_messages=True,
                can_promote_members=True,
            ),
        )
        return await rd.edit(f"Fully Promoted! {umention}")

    await message.chat.promote_member(
        user_id,
        privileges=ChatPrivileges(
            can_manage_chat=True,
            can_delete_messages=True,
            can_manage_video_chats=True,
            can_restrict_members=True,
            can_change_info=True,
            can_invite_users=True,
            can_pin_messages=True,
            can_promote_members=False,
        ),
    )
    await rd.edit(f"Promoted! {umention}")


@Client.on_message(filters.group & filters.command("demote", ".") & filters.me)
async def demote(client: Client, message: Message):
    user_id = await extract_user(message)
    rd = await message.edit_text("`Processing...`")
    if not user_id:
        return await rd.edit("Tidak dapat menemukan pengguna.")
    if user_id == client.me.id:
        return await rd.edit("lah, au yaa.")
    await message.chat.promote_member(
        user_id,
        privileges=ChatPrivileges(
            can_manage_chat=False,
            can_delete_messages=False,
            can_manage_video_chats=False,
            can_restrict_members=False,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False,
            can_promote_members=False,
        ),
    )
    umention = (await client.get_users(user_id)).mention
    await rd.edit(f"Demoted! {umention}")


add_command_help(
    "Admin",
    [
        ["ban [reply/username/userid]", "Ban someone."],
        [
            f"unban [reply/username/userid]",
            "Unban someone.",
        ],
        ["kick [reply/username/userid]", "kick out someone from your group."],
        [
            f"promote `or` .fullpromote",
            "Promote someone.",
        ],
        ["demote", "Demote someone."],
        [
            "mute [reply/username/userid]",
            "Mute someone.",
        ],
        [
            "unmute [reply/username/userid]",
            "Unmute someone.",
        ],
        [
            "pin [reply]",
            "to pin any message.",
        ],
        [
            "unpin [reply]",
            "To unpin any message.",
        ],
        [
            "setgpic [reply ke image]",
            "To set an group profile pic",
        ],
    ],
)
