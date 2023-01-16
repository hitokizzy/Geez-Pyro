# if you can read this, this meant you use code from Geez Ram Project
# this code is from somewhere else
# please dont hestitate to steal it
# because Geez and Ram doesn't care about credit
# at least we are know as well
# who Geez and Ram is
#
#
# kopas repo dan hapus credit, ga akan jadikan lu seorang developer
# ©2023 Geez & Ram Team
import asyncio
from pyrogram.errors import FloodWait
from pyrogram import Client, errors, filters
from pyrogram.types import ChatPermissions, Message
from geezlibs import DEVS, BL_GEEZ
from geezlibs.geez.database import gmutedb as Gmute
from geezlibs.geez.database import (add_banned_user,
                                       get_banned_count,
                                       get_banned_users,
                                       get_served_chats,
                                       is_banned_user,
                                       remove_banned_user)
from Geez.modules.basic.profile import extract_user, extract_user_and_reason
from Geez.modules.basic import add_command_help
from Geez.modules.bot.inline import get_readable_time

ok = []

@Client.on_message(
    filters.command("ggban", ["."]) & filters.user(DEVS) & ~filters.via_bot
)
@Client.on_message(filters.command("gban", ".") & filters.me)
async def gbanuser(client: Client, message: Message):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text("Balas pesan pengguna atau berikan nama pengguna/id_pengguna")
        user = message.text.split(None, 1)[1]
        user = await client.get_users(user)
        user_id = user.id
        mention = user.mention
    else:
        user_id = message.reply_to_message.from_user.id
        mention = message.reply_to_message.from_user.mention
    if user_id == message.from_user.id:
        return await message.reply_text("Lu mau gban diri sendiri? Tolol!")
    elif user_id == client.me.id:
        return await message.reply_text("Haruskah saya memblokir diri saya sendiri? Lol")
    elif user_id in DEVS:
        return await message.reply_text("Lah ngapa yaaaa?")
    is_gbanned = await is_banned_user(user_id)
    if is_gbanned:
        return await message.reply_text(["{0} sudah **gbanned** dari bot."].format(mention))
    if user_id not in BL_GEEZ:
        BL_GEEZ.add(user_id)
    served_chats = []
    chats = await get_served_chats()
    for chat in chats:
        served_chats.append(int(chat["chat_id"]))
    time_expected = len(served_chats)
    time_expected = get_readable_time(time_expected)
    mystic = await message.reply_text(
        ["**Menginisialisasi Larangan Global pada {0}**\n\nWaktu yang Diharapkan : {1}."].format(mention, time_expected)
    )
    number_of_chats = 0
    for chat_id in served_chats:
        try:
            await Client.ban_chat_member(chat_id, user_id)
            number_of_chats += 1
        except FloodWait as e:
            await asyncio.sleep(int(e.x))
        except Exception:
            pass
    await add_banned_user(user_id)
    await message.reply_text(
        ["**Berhasil Dibanned**\n\nBanned **{0}** dari **{1}** chat."].format(mention, number_of_chats)
    )
    await mystic.delete()


@Client.on_message(
    filters.command("gungban", ["."]) & filters.user(DEVS) & ~filters.via_bot
)
@Client.on_message(filters.command("ungban", ".") & filters.me)
async def gungabn(client: Client, message: Message):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text("Balas pesan pengguna atau berikan nama pengguna/id_pengguna")
        user = message.text.split(None, 1)[1]
        user = await Client.get_users(user)
        user_id = user.id
        mention = user.mention
    else:
        user_id = message.reply_to_message.from_user.id
        mention = message.reply_to_message.from_user.mention
    is_gbanned = await is_banned_user(user_id)
    if not is_gbanned:
        return await message.reply_text(["{0} belum **gbanned **belum dari bot."].format(mention))
    if user_id in BL_GEEZ:
        BL_GEEZ.remove(user_id)
    served_chats = []
    chats = await get_served_chats()
    for chat in chats:
        served_chats.append(int(chat["chat_id"]))
    time_expected = len(served_chats)
    time_expected = get_readable_time(time_expected)
    mystic = await message.reply_text(
        ["**Membatalkan pemblokiran {0}**\n\nWaktu yang Diharapkan : {1}."].format(mention, time_expected)
    )
    number_of_chats = 0
    for chat_id in served_chats:
        try:
            await Client.unban_chat_member(chat_id, user_id)
            number_of_chats += 1
        except FloodWait as e:
            await asyncio.sleep(int(e.x))
        except Exception:
            pass
    await remove_banned_user(user_id)
    await message.reply_text(
        ["**UnGbanned Berhasil**\n\nUnbanned **{0}** di **{1}** chat."].format(mention, number_of_chats)
    )
    await mystic.delete()


@Client.on_message(filters.command("listgban", ".") & filters.me)
async def gbanned_list(client: Client, message: Message):
    counts = await get_banned_count()
    if counts == 0:
        return await message.reply_text("tidak menemukan user dalam listgban")
    mystic = await message.reply_text("Harap tunggu sebentar.. Mengambil daftar pengguna Gbanned")
    msg = "Gbanned Users:\n\n"
    count = 0
    users = await get_banned_users()
    for user_id in users:
        count += 1
        try:
            user = await client.get_users(user_id)
            user = (
                user.first_name if not user.mention else user.mention
            )
            msg += f"{count}➤ {user}\n"
        except Exception:
            msg += f"{count}➤ [Unfetched User]{user_id}\n"
            continue
    if count == 0:
        return await mystic.edit_text("Tidak Ditemukan Pengguna yang Di-Gban.")
    else:
        return await mystic.edit_text(msg)


@Client.on_message(filters.command("gmute", ".") & filters.me)
async def gmute_user(client: Client, message: Message):
    args = await extract_user(message)
    reply = message.reply_to_message
    ex = await message.edit_text(message, "`Processing...`")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            await ex.edit(f"`Please specify a valid user!`")
            return
    elif reply:
        user_id = reply.from_user.id
        user = await client.get_users(user_id)
    else:
        await ex.edit(f"`Please specify a valid user!`")
        return
    if user.id == client.me.id:
        return await ex.edit("**Okay Sure.. 🐽**")
    if user.id in DEVS:
        return await ex.edit("**LAh auyaaa**")
    try:
        replied_user = reply.from_user
        if replied_user.is_self:
            return await ex.edit("`Calm down anybob, you can't gmute yourself.`")
    except BaseException:
        pass

    try:
        if (await Gmute.is_gmuted(user.id)):
            return await ex.edit("`User already gmuted`")
        await Gmute.gmute(user.id)
        ok.append(user.id)
        await ex.edit(f"[{user.first_name}](tg://user?id={user.id}) globally gmuted!")
        try:
            common_chats = await client.get_common_chats(user.id)
            for i in common_chats:
                await i.restrict_member(user.id, ChatPermissions())
        except BaseException:
            pass
    
    except Exception as e:
        await ex.edit(f"**ERROR:** `{e}`")
        return


@Client.on_message(filters.command("ungmute", ".") & filters.me)
async def ungmute_user(client: Client, message: Message):
    args = await extract_user(message)
    reply = message.reply_to_message
    ex = await message.edit_text("`Processing...`")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            await ex.edit(f"`Please specify a valid user!`")
            return
    elif reply:
        user_id = reply.from_user.id
        user = await client.get_users(user_id)
    else:
        await ex.edit(f"`Please specify a valid user!`")
        return

    try:
        replied_user = reply.from_user
        if replied_user.is_self:
            return await ex.edit("`Calm down anybob, you can't ungmute yourself.`")
    except BaseException:
        pass

    try:
        if not (await Gmute.is_gmuted(user.id)):
            return await ex.edit("`User already ungmuted`")
        await Gmute.ungmute(user.id)
        ok.remove(user.id)
        try:
            common_chats = await client.get_common_chats(user.id)
            for i in common_chats:
                await i.unban_member(user.id)
        except BaseException:
            pass
        await ex.edit(
            f"[{user.first_name}](tg://user?id={user.id}) globally ungmuted!"
        )
    except Exception as e:
        await ex.edit(f"**ERROR:** `{e}`")
        return


@Client.on_message(filters.command("listgmute", ".") & filters.me)
async def gmutelist(client: Client, message: Message):
    users = (await Gmute.gmute_list())
    ex = await message.edit_text("`Processing...`")
    if not users:
        return await ex.edit("There are no Muted Users yet")
    gmute_list = "**GMuted Users:**\n"
    count = 0
    for i in users:
        count += 1
        gmute_list += f"**{count} -** `{i.sender}`\n"
    return await ex.edit(gmute_list)

if ok:
 @Client.on_message(filters.incoming & filters.group)
 async def globals_check(client: Client, message: Message):
    if not message:
        return
    if not message.from_user:
        return
    user_id = message.from_user.id
    chat_id = message.chat.id
    if not user_id:
        return
    if (await Geez.gban_info(user_id)):
        try:
            await client.ban_chat_member(chat_id, user_id)
        except BaseException:
            pass

    if (await Gmute.is_gmuted(user_id)):
        try:
            await message.delete()
        except errors.RPCError:
            pass
        try:
            await client.restrict_chat_member(chat_id, user_id, ChatPermissions())
        except BaseException:
            pass

    message.continue_propagation()


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
