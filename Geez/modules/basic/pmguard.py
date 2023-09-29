from pyrogram import filters, Client
from pyrogram.types import Message
from geezlibs import DEVS
from geezlibs.geez import geez, devs
from geezlibs.geez.utils.geezlogs import izzy_meira
from geezlibs.geez.database.pmpermit import get_approved_users, pm_guard, allow_user
from geezlibs.geez.database import pmpermit as TOD
from config import BOTLOG_CHATID
from Geez import cmds, bot
PM_LOGGER = BOTLOG_CHATID
FLOOD_CTRL = 0
ALLOWED = []
USERS_AND_WARNS = {}

async def denied_users(filter, client: Client, message: Message):
    if not await pm_guard():
        return False
    if message.chat.id in (await get_approved_users()):
        return False
    else:
        return True

def get_arg(message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])


@geez("setlimit", cmds)
async def pmguard(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**Set limit to what?**")
        return
    await TOD.set_limit(int(arg))
    await message.edit(f"**Limit set to {arg}**")



@geez("setblocking", cmds)
async def setpmmsg(client, message):
    arg = get_arg(message)
    if not arg:
        await message.edit("**What message to set**")
        return
    if arg == "default":
        await TOD.set_block_message(TOD.BLOCKED)
        await message.edit("**Block message set to default**.")
        return
    await TOD.set_block_message(f"`{arg}`")
    await message.edit("**Custom block message set**")


@Client.on_message(filters.command(["allow", "ok", "approve", "k"], cmds) & filters.me & filters.private)
async def allow(client, message):
    chat_id = message.chat.id
    pmpermit, pm_message, limit, block_message = await TOD.get_pm_settings()
    await TOD.allow_user(chat_id)
    await message.edit(f"**Menerima pesan dari [you](tg://user?id={chat_id}).**")
    async for message in client.search_messages(
        chat_id=message.chat.id, query=pm_message, limit=1, from_user="me"
    ):
        await message.delete()
    USERS_AND_WARNS.update({chat_id: 0})


@Client.on_message(filters.command(["deny", "fuck", "no", "blok"], cmds) & filters.me & filters.private)
async def deny(client, message):
    chat_id = message.chat.id
    await TOD.deny_user(chat_id)
    await message.edit(f"**I have denied [you](tg://user?id={chat_id}) to PM me.**")


@Client.on_message(
    filters.private
    & filters.create(denied_users)
    & filters.incoming
    & ~filters.service
    & ~filters.me
    & ~filters.bot
    & ~filters.via_bot
)
async def reply_pm(app: Client, message):
    global FLOOD_CTRL
    pmpermit, pm_message, limit, block_message = await TOD.get_pm_settings()
    user = message.from_user
    user_id = user.id
    user_warns = 0 if user_id not in USERS_AND_WARNS else USERS_AND_WARNS[user_id]
    group = await izzy_meira(bot)
    if group:
        await app.send_message(group.id, f"pesan dari {user.first_name}:\n{message.text}")
    else:
        await app.send_message("me", f"pesan dari {user.first_name}:\n{message.text}")
    if user_warns <= limit - 2:
        user_warns += 1
        USERS_AND_WARNS.update({user_id: user_warns})
        if not FLOOD_CTRL > 0:
            FLOOD_CTRL += 1
        else:
            FLOOD_CTRL = 0
            return
        async for message in app.search_messages(
            chat_id=message.chat.id, query=pm_message, limit=1, from_user="me"
        ):
            await message.delete()
        await message.reply(pm_message, disable_web_page_preview=True)
        return
    await message.reply(block_message, disable_web_page_preview=True)
    await app.block_user(message.chat.id)
    USERS_AND_WARNS.update({user_id: 0})
