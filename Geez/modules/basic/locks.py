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
from pyrogram import Client
from pyrogram.errors.exceptions.bad_request_400 import (
    ChatAdminRequired,
    ChatNotModified,
)
from pyrogram.types import ChatPermissions, Message
from geezlibs.geez import geez
from Geez.modules.basic import add_command_help
from Geez import cmds

incorrect_parameters = f"Parameter Wrong, Type `.help locks`"
data = {
    "msg": "can_send_messages",
    "stickers": "can_send_other_messages",
    "gifs": "can_send_other_messages",
    "media": "can_send_media_messages",
    "games": "can_send_other_messages",
    "inline": "can_send_other_messages",
    "url": "can_add_web_page_previews",
    "polls": "can_send_polls",
    "info": "can_change_info",
    "invite": "can_invite_users",
    "pin": "can_pin_messages",
}


async def current_chat_permissions(client: Client, chat_id):
    perms = []
    perm = (await client.get_chat(chat_id)).permissions
    if perm.can_send_messages:
        perms.append("can_send_messages")
    if perm.can_send_media_messages:
        perms.append("can_send_media_messages")
    if perm.can_send_other_messages:
        perms.append("can_send_other_messages")
    if perm.can_add_web_page_previews:
        perms.append("can_add_web_page_previews")
    if perm.can_send_polls:
        perms.append("can_send_polls")
    if perm.can_change_info:
        perms.append("can_change_info")
    if perm.can_invite_users:
        perms.append("can_invite_users")
    if perm.can_pin_messages:
        perms.append("can_pin_messages")
    return perms


async def tg_lock(
    client: Client,
    message: Message,
    parameter,
    permissions: list,
    perm: str,
    lock: bool,
):
    if lock:
        if perm not in permissions:
            return await message.edit_text(f"🔒 `{parameter}` **sudah di-lock!**")
        permissions.remove(perm)
    else:
        if perm in permissions:
            return await message.edit_text(f"🔓 `{parameter}` **sudah di-unlock!**")
        permissions.append(perm)
    permissions = {perm: True for perm in list(set(permissions))}
    try:
        await client.set_chat_permissions(
            message.chat.id, ChatPermissions(**permissions)
        )
    except ChatNotModified:
        return await message.edit_text(
            f"gunakan lock, terlebih dahulu."
        )
    except ChatAdminRequired:
        return await message.edit_text("`anda harus menjadi admin disini.`")
    await message.edit_text(
        (
            f"🔒 **Locked untuk non-admin!**\n  **Type:** `{parameter}`\n  **Chat:** {message.chat.title}"
            if lock
            else f"🔒 **Unlocked untuk non-admin!**\n  **Type:** `{parameter}`\n  **Chat:** {message.chat.title}"
        )
    )


@geez(["lock", "unlock"], cmds)
async def locks_func(client: Client, message: Message):
    if len(message.command) != 2:
        return await message.edit_text(incorrect_parameters)
    chat_id = message.chat.id
    parameter = message.text.strip().split(None, 1)[1].lower()
    state = message.command[0].lower()
    if parameter not in data and parameter != "all":
        return await message.edit_text(incorrect_parameters)
    permissions = await current_chat_permissions(client, chat_id)
    if parameter in data:
        await tg_lock(
            client,
            message,
            parameter,
            permissions,
            data[parameter],
            bool(state == "lock"),
        )
    elif parameter == "all" and state == "lock":
        try:
            await client.set_chat_permissions(chat_id, ChatPermissions())
            await message.edit_text(
                f"🔒 **Locked untuk non-admin!**\n  **Type:** `{parameter}`\n  **Chat:** {message.chat.title}"
            )
        except ChatAdminRequired:
            return await message.edit_text("`anda harus menjadi admin disini.`")
        except ChatNotModified:
            return await message.edit_text(
                f"🔒 **BErhasil di-Lock!**\n  **Type:** `{parameter}`\n  **Chat:** {message.chat.title}"
            )
    elif parameter == "all" and state == "unlock":
        try:
            await client.set_chat_permissions(
                chat_id,
                ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=True,
                    can_send_other_messages=True,
                    can_add_web_page_previews=True,
                    can_send_polls=True,
                    can_change_info=False,
                    can_invite_users=True,
                    can_pin_messages=False,
                ),
            )
        except ChatAdminRequired:
            return await message.edit_text("`anda harus menjadi admin disini`")
        await message.edit(
            f"🔒 **Unlocked untuk non-admin!**\n  **Type:** `{parameter}`\n  **Chat:** {message.chat.title}"
        )


@geez("lockall", cmds)
async def locktypes(client: Client, message: Message):
    permissions = await current_chat_permissions(client, message.chat.id)

    if not permissions:
        return await message.edit("🔒 **lock untuk semua!**")

    perms = ""
    for i in permissions:
        perms += f" • __**{i}**__\n"

    await message.edit_text(perms)


add_command_help(
    "locks",
    [
        [f"{cmds}lock [all atau spesific content]", "membatasi kiriman group."],
        [f"{cmds}unlock [all atau spesific content]",
            "membuka lock\n\nspesific content : Locks / Unlocks:` `msg` | `media` | `stickers` | `polls` | `info`  | `invite` | `webprev` |`pin` | `all`.",
        ],
    ],
)
