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
from datetime import datetime
from pyrogram import filters, Client
from pyrogram.types import Message
from geezlibs.geez.database import check_afk, go_afk, no_afk
from geezlibs.geez import geez
from Geez.modules.basic import add_command_help
from Geez import cmds
from config import BOTLOG_CHATID

def get_text(message: Message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None

afk_sanity_check: dict = {}
afkstr = """
#AFK Activated\n reason {}
"""
onlinestr ="""
#AFK De-activated\nAfk for {}
"""
async def is_afk_(f, client, message):
    af_k_c = await check_afk()
    if af_k_c:
        return bool(True)
    else:
        return bool(False)
    
is_afk = filters.create(func=is_afk_, name="is_afk_")

@geez("afk", cmds)
async def set_afk(client, message: Message):
    if len(message.command) == 1:
        return await message.reply(f"tolong berikan alasan,\ncontoh : {cmds}afk coly")
    pablo = await message.edit("Processing..")
    msge = None
    msge = get_text(message)
    start_1 = datetime.now()
    afk_start = start_1.replace(microsecond=0)
    if msge:
        msg = f"I'am afk.\nReason: **{msge}**"
        await client.send_message(BOTLOG_CHATID, afkstr.format(msge))
        await go_afk(afk_start, msge)
    else:
        msg = "**I Am Busy And I Am Going Afk**."
        await client.send(BOTLOG_CHATID, afkstr.format(msge))
        await go_afk(afk_start)
    await pablo.edit(msg)

@Client.on_message(
    is_afk
    & (filters.mentioned | filters.private)
    & ~filters.me
    & ~filters.bot
    & filters.incoming
)
async def afk_er(client, message):
    if not message:
        return
    if not message.from_user:
        return
    if message.from_user.id == client.me.id:
        return
    use_r = int(message.from_user.id)
    if use_r not in afk_sanity_check.keys():
        afk_sanity_check[use_r] = 1
    else:
        afk_sanity_check[use_r] += 1
    if afk_sanity_check[use_r] == 5:
        await message.reply_text(
            "`Bawel, saya tidak akan reply anda. ;(`"
        )
        afk_sanity_check[use_r] += 1
        return
    if afk_sanity_check[use_r] > 5:
        return
    lol = await check_afk()
    reason = lol["reason"]
    if reason == "":
        reason = None
    back_alivee = datetime.now()
    afk_start = lol["time"]
    afk_end = back_alivee.replace(microsecond=0)
    total_afk_time = str((afk_end - afk_start))
    message_to_reply = (
        f"I Am **AFK** Right Now. \n**Last Seen :** `{total_afk_time}`\n**Reason** : `{reason}`"
        if reason
        else f"I Am **AFK** Right Now. \n**Last Seen :** `{total_afk_time}`"
    )
    await message.reply(message_to_reply)

@Client.on_message(filters.outgoing & filters.me & is_afk)
async def no_afke(client, message: Message):
    lol = await check_afk()
    back_alivee = datetime.now()
    afk_start = lol["time"]
    afk_end = back_alivee.replace(microsecond=0)
    total_afk_time = str((afk_end - afk_start))
    kk = await message.reply(f"Iam Online, no longer AFK\nAFK selama{total_afk_time}")
    await kk.delete()
    await no_afk()
    await client.send_message(BOTLOG_CHATID, onlinestr.format(total_afk_time))

add_command_help(
    "afk",
    [
        [f"{cmds}afk","Mengaktifkan mode afk.",
        ],
    ],
)