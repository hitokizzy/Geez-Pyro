
import asyncio
from pyrogram import *
from pyrogram import Client as gez
from pyrogram import Client
from pyrogram.types import * 
from config import *
from geez.helper.basic import *
from geez.database.SQL import no_log_pms_sql
from geez.database.SQL.globals import *
from geez.helper.misc import *
from geez.modules.help import *


class LOG_CHATS:
    def __init__(self):
        self.RECENT_USER = None
        self.NEWPM = None
        self.COUNT = 0


LOG_CHATS_ = LOG_CHATS()


@gez.on_message(
    filters.private & filters.incoming & ~filters.service & ~filters.me & ~filters.bot
)
async def monito_p_m_s(client: Client, message: Message):
    if LOG_GROUP == -100:
        return
    if gvarstatus("PMLOG") and gvarstatus("PMLOG") == "false":
        return
    if not no_log_pms_sql.is_approved(message.chat.id) and message.chat.id != 777000:
        if LOG_CHATS_.RECENT_USER != message.chat.id:
            LOG_CHATS_.RECENT_USER = message.chat.id
            if LOG_CHATS_.NEWPM:
                await LOG_CHATS_.NEWPM.edit(
                    LOG_CHATS_.NEWPM.text.replace(
                        "**💌 #NEW_MESSAGE**",
                        f" • `{LOG_CHATS_.COUNT}` **Message**",
                    )
                )
                LOG_CHATS_.COUNT = 0
            LOG_CHATS_.NEWPM = await client.send_message(
                LOG_GROUP,
                f"💌 <b>#FORWARD #NEW_MESSAGE</b>\n<b> • From :</b> {message.from_user.mention}\n<b> • User ID :</b> <code>{message.from_user.id}</code>",
                parse_mode=enums.ParseMode.HTML,
            )
        try:
            async for pmlog in client.search_messages(message.chat.id, limit=1):
                await pmlog.forward(LOG_GROUP)
            LOG_CHATS_.COUNT += 1
        except BaseException:
            pass


@gez.on_message(filters.group & filters.mentioned & filters.incoming)
async def log_tagged_messages(client: Client, message: Message):
    if LOG_GROUP == -100:
        return
    if gvarstatus("GRUPLOG") and gvarstatus("GRUPLOG") == "false":
        return
    if (no_log_pms_sql.is_approved(message.chat.id)) or (LOG_GROUP == -100):
        return
    result = f"<b>📨 #TAGS #MESSAGE</b>\n<b> • From : </b>{message.from_user.mention}"
    result += f"\n<b> • Grup : </b>{message.chat.title}"
    result += f"\n<b> • 👀 </b><a href = '{message.link}'>View Messages</a>"
    result += f"\n<b> • Message : </b><code>{message.text}</code>"
    await asyncio.sleep(0.5)
    await client.send_message(
        LOG_GROUP,
        result,
        parse_mode=enums.ParseMode.HTML,
        disable_web_page_preview=True,
    )


@gez.on_message(filters.command("log", ".") & filters.me)
async def set_log_p_m(client: Client, message: Message):
    if LOG_GROUP != -100:
        if no_log_pms_sql.is_approved(message.chat.id):
            no_log_pms_sql.disapprove(message.chat.id)
            await message.edit("**The LOG chat of this group has been activated successfully**")


@gez.on_message(filters.command("nolog", ".") & filters.me)
async def set_no_log_p_m(client: Client, message: Message):
    if LOG_GROUP != -100:
        if not no_log_pms_sql.is_approved(message.chat.id):
            no_log_pms_sql.approve(message.chat.id)
            await message.edit("**LOG chat from this group has been disabled successfully**")


@gez.on_message(filters.command(["pmlog", "pmlogger"], ".") & filters.me)
async def set_pmlog(client: Client, message: Message):
    if LOG_GROUP == -100:
        return await message.edit(
            "**To Use this Module, you have to set ** `LOG_GROUP` **in config vars**"
        )
    input_str = get_arg(message)
    if input_str == "off":
        h_type = False
    elif input_str == "on":
        h_type = True
    if gvarstatus("PMLOG") and gvarstatus("PMLOG") == "false":
        PMLOG = False
    else:
        PMLOG = True
    if PMLOG:
        if h_type:
            await edit_or_reply(message, "**PM LOG has been activated**")
        else:
            addgvar("PMLOG", h_type)
            await edit_or_reply(message, "**PM LOG turned off successfully**")
    elif h_type:
        addgvar("PMLOG", h_type)
        await edit_or_reply(message, "**PM LOG has been activated**")
    else:
        await edit_or_reply(message, "**PM LOG turned off successfully**")


@gez.on_message(filters.command(["gruplog", "grouplog", "gclog"], ".") & filters.me)
async def set_gruplog(client: Client, message: Message):
    if LOG_GROUP == -100:
        return await message.edit(
            "**To Use this Module, you have to set ** `LOG_GROUP` **in config vars**"
        )
    input_str = get_arg(message)
    if input_str == "off":
        h_type = False
    elif input_str == "on":
        h_type = True
    if gvarstatus("GRUPLOG") and gvarstatus("GRUPLOG") == "false":
        GRUPLOG = False
    else:
        GRUPLOG = True
    if GRUPLOG:
        if h_type:
            await edit_or_reply(message, "**Group Log Sudah Diaktifkan**")
        else:
            addgvar("GRUPLOG", h_type)
            await edit_or_reply(message, "**Group Log Berhasil Dimatikan**")
    elif h_type:
        addgvar("GRUPLOG", h_type)
        await edit_or_reply(message, "**Group Log Berhasil Diaktifkan**")
    else:
        await edit_or_reply(message, "**Group Log Sudah Dimatikan**")


add_command_help(
    "Log",
    [
        ["log", "To enable chat logs from that chat/group",],
        ["nolog", "To disable chat logs from that chat/group",],
        [f"pmlog on/off", "to enable or disable private log messages to be forwarded to the log group"],
        [f"gruplog on/off", "To activate or deactivate the group tag, which will go to the log group."],
    ],
)
