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

from pyrogram import Client, filters
from pyrogram.types import Message
from geezlibs import DEVS
from geezlibs.geez.helper.PyroHelpers import get_ub_chats
from Geez.modules.basic.profile import extract_user_and_reason
from geezlibs.geez import geez, devs
from geezlibs.geez.database import gbandb as Geez
from geezlibs.geez.database import gmutedb as Gmute
from Geez.modules.basic import add_command_help
from Geez import cmds

ok = []

@Client.on_message(filters.command("ggban", "*") & filters.user(DEVS))
@geez("gban", cmds)
async def gban_user(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    if message.from_user.id != client.me.id:
        ex = await message.reply_text("`Gbaning...`")
    else:
        ex = await message.edit("`Gbaning on progress`")
    if not user_id:
        return await ex.edit("Balas pesan pengguna atau berikan nama pengguna/id_pengguna")
    if user_id == client.me.id:
        return await ex.edit("**Lu mau gban diri sendiri? Tolol!**")
    if user_id in DEVS:
        return await ex.edit("Devs tidak bisa di gban, only Gods can defeat Gods")
    if user_id:
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await ex.edit("`Balas pesan pengguna atau berikan nama pengguna/id_pengguna`")

    if (await Geez.gban_info(user.id)):
        return await ex.edit(
            f"[user](tg://user?id={user.id}) **pengguna telah di gban**"
        )
    f_chats = await get_ub_chats(client)
    if not f_chats:
        return await ex.edit("**tidak menjadi admin dimanapun, kasian...**")
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

@Client.on_message(filters.command("gugban", "*") & filters.user(DEVS))
@geez("ungban", cmds)
async def ungban_user(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    if message.from_user.id != client.me.id:
        ex = await message.reply("`UnGbanning...`")
    else:
        ex = await message.edit("`UnGbanning....`")
    if not user_id:
        return await ex.edit("pengguna tidak ditemukan.")
    if user_id:
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await ex.edit("`berikan pengguna dengan benar!`")

    try:
        if not (await Geez.gban_info(user.id)):
            return await ex.edit("`Pengguna sudah di ungban`")
        ung_chats = await get_ub_chats(client)
        ok.remove(user.id)
        if not ung_chats:
            return await ex.edit("**tidak ada group sebagai admin**")
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


@geez("listgban", cmds)
async def gbanlist(client: Client, message: Message):
    users = (await Geez.gban_list())
    oof = "**#GBanned Users:**\n"
    ex = await message.edit_text("`mencari...`")
    list_ = await Geez.gban_list()
    if len(list_) == 0:
        await ex.edit("**Anak baik, belom gban orang**")
        return
    for lit in list_:
        oof += f"**User :** `{lit['user']}` \n**Alasan :** `{lit['reason']}` \n\n"
    return await ex.edit(oof)


add_command_help(
    "globals",
    [
        [f"{cmds}gban <reply/username/userid>","Global Banning.",],
        [f"{cmds}ungban <reply/username/userid>", "membatalkan Global Banned."],
        [f"{cmds}listgban", "list Global banning."],
    ],
)
