import asyncio
from datetime import datetime

import humanize
from pyrogram import filters, Client
from pyrogram.types import Message

from geez.helper.PyroHelpers import GetChatID, ReplyCheck
from geez.modules.help import add_command_help

AFK = False
AFK_REASON = ""
AFK_TIME = ""
USERS = {}
GROUPS = {}


def subtract_time(start, end):
    subtracted = humanize.naturaltime(start - end)
    return str(subtracted)


@Client.on_message(
    ((filters.group & filters.mentioned) | filters.private) & ~filters.me & ~filters.service, group=3
)
async def collect_afk_messages(bot: Client, message: Message):
    if AFK:
        last_seen = subtract_time(datetime.now(), AFK_TIME)
        is_group = True if message.chat.type in ["supergroup", "group"] else False
        CHAT_TYPE = GROUPS if is_group else USERS

        if GetChatID(message) not in CHAT_TYPE:
            text = (
                f"`Pesan Otomatis Geez Pyro.\n"
                f"Saya sedang offline/afk.\n"
                f"Last seen: {last_seen}\n"
                f"Reason: ```{AFK_REASON.upper()}```\n"
            )
            await bot.send_message(
                chat_id=GetChatID(message),
                text=text,
                reply_to_message_id=ReplyCheck(message),
            )
            CHAT_TYPE[GetChatID(message)] = 1
            return
        elif GetChatID(message) in CHAT_TYPE:
            if CHAT_TYPE[GetChatID(message)] == 50:
                text = (
                    f"`Pesan Otomatis Geez Pyro.\n"
                    f"Last seen: {last_seen}\n"
                    f"Saya sedang Offline/afk.\n"
                    f"Jangan tag/kirim pesan...`"
                )
                await bot.send_message(
                    chat_id=GetChatID(message),
                    text=text,
                    reply_to_message_id=ReplyCheck(message),
                )
            elif CHAT_TYPE[GetChatID(message)] > 50:
                return
            elif CHAT_TYPE[GetChatID(message)] % 5 == 0:
                text = (
                    f"`Maaf, saya maih Offline/afk.\n"
                    f"Last seen: {last_seen}\n"
                    f"Still busy: ```{AFK_REASON.upper()}```\n"
                    f"Coba lagi lain kali.`"
                )
                await bot.send_message(
                    chat_id=GetChatID(message),
                    text=text,
                    reply_to_message_id=ReplyCheck(message),
                )

        CHAT_TYPE[GetChatID(message)] += 1


@Client.on_message(filters.command("afk", ".") & filters.me, group=3)
async def afk_set(bot: Client, message: Message):
    global AFK_REASON, AFK, AFK_TIME

    cmd = message.command
    afk_text = ""

    if len(cmd) > 1:
        afk_text = " ".join(cmd[1:])

    if isinstance(afk_text, str):
        AFK_REASON = afk_text

    AFK = True
    AFK_TIME = datetime.now()

    await message.delete()


@Client.on_message(filters.command("afk", "!") & filters.me, group=3)
async def afk_unset(bot: Client, message: Message):
    global AFK, AFK_TIME, AFK_REASON, USERS, GROUPS

    if AFK:
        last_seen = subtract_time(datetime.now(), AFK_TIME).replace("ago", "").strip()
        await message.edit(
            f"`Selama AFK (for {last_seen}), kamu menerima {sum(USERS.values()) + sum(GROUPS.values())} "
            f"pesan dari {len(USERS) + len(GROUPS)}`"
        )
        AFK = False
        AFK_TIME = ""
        AFK_REASON = ""
        USERS = {}
        GROUPS = {}
        await asyncio.sleep(5)

    await message.delete()

if AFK:
   @Client.on_message(filters.me, group=3)
   async def auto_afk_unset(bot: Client, message: Message):
       global AFK, AFK_TIME, AFK_REASON, USERS, GROUPS

       if AFK:
           last_seen = subtract_time(datetime.now(), AFK_TIME).replace("ago", "").strip()
           reply = await message.reply(
               f"`Selama AFK (for {last_seen}), kamu menerima {sum(USERS.values()) + sum(GROUPS.values())} "
               f"pesan dari {len(USERS) + len(GROUPS)}`"
           )
           AFK = False
           AFK_TIME = ""
           AFK_REASON = ""
           USERS = {}
           GROUPS = {}
           await asyncio.sleep(5)
           await reply.delete()


add_command_help(
    "afk",
    [
        [".afk", "Activates AFK mode with reason as anything after .afk\nUsage: ```.afk <reason>```"],
        ["!afk", "Deactivates AFK mode."],
    ],
)
