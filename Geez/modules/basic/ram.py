import random
import asyncio
from pyrogram import Client
from pyrogram.types import Message
from geezlibs import DEVS
from geezlibs.geez import geez
from geezlibs.geez.database.ram import get_ram_users, unram_user
from Geez.modules.basic.profile import extract_user
from Geez import cmds
from cache.data import RAM
from Geez.modules.basic import add_command_help


RAMS=[]

@geez("r", cmds)
async def rams(client: Client, message: Message):
    rama = random.choice(RAM)
    await message.edit(rama)

@geez("rw", cmds)
async def ramrep(client: Client, message: Message):  
    rw_text = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 2)
    if len(rw_text) == 2:
        counts = int(rw_text[0])
        ok = await client.get_users(rw_text[1])
        id = ok.id
        if int(id) in DEVS:
            text = ("`Ilmu anda tidak cukup untuk lawan devs`")
            await message.reply_text(text)
        else:
            fname = ok.first_name
            mention = f"[{fname}](tg://user?id={id})"
            for _ in range(counts):
                reply = random.choice(RAM)
                msg = f"{mention} {reply}"
                await client.send_message(message.chat.id, msg)
                await asyncio.sleep(0.10)
    elif message.reply_to_message:
        counts = int(rw_text[0])
        user_id = message.reply_to_message.from_user.id
        ok = await client.get_users(user_id)
        id = ok.id
        if int(id) in DEVS:
            text = ("`Ilmu anda tidak cukup untuk lawan devs`")
            await message.reply_text(text)
        else:
            fname = ok.first_name
            mention = f"[{fname}](tg://user?id={id})"
            for _ in range(counts):
                reply = random.choice(RAM)
                msg = f"{mention} {reply}"
                await client.send_message(message.chat.id, msg)
                await asyncio.sleep(0.10)
    else:
        await message.reply_text(f"gunakan: {cmds}rw [user id] [jumlah]")


@geez("srw", cmds)
async def ramstop(client: Client, message: Message):
    args = await extract_user(message)
    reply = message.reply_to_message
    ex = await message.edit_text("`Processing...`")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            await ex.edit("`Target tidak ditemukan!`")
            return
    elif reply:
        user_id = reply.from_user.id
        user = await client.get_users(user_id)
    else:
        await ex.edit("`Target tidak ditemukan!`")
        return
    try:
        if user.id not in (await get_ram_users()):
            await ex.edit("mode spam reply tidak aktif untuk user")
            return
        await unram_user(user.id)
        RAMS.remove(user.id)
        await ex.edit(f"[{user.first_name}](tg://user?id={user.id}) Spam reply dihentikan!")
    except Exception as message:
        await ex.edit(f"**ERROR:** `{message}`")
        return
    
add_command_help(
    "ram",
    [
        [f"{cmds}r","ram-ubot special words.",],
        [f"{cmds}rw [username]","mengaktifkan spam reply.",],
        [f"{cmds}srw","menghentikan spam reply.",],
    ],
)