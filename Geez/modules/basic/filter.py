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

import re
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton as Ikb
from geezlibs import BL_GCAST
from geezlibs.geez import geez
from geezlibs.geez.database import delete_filter, get_filter, get_filters_names, save_filter
from geezlibs.geez.filter import *
from Geez.modules.basic.help import add_command_help
from Geez import cmds

@geez("savefilter", cmds) #lu gay
async def save_filters(_, message):
    if len(message.command) < 2 or not message.reply_to_message:
        return await message.reply_text(
            f"**Penggunaan:**\nbalas kepesan atau sticker {cmds}savefilter [nama filternya] untuk save filter."
        )
    if (
        not message.reply_to_message.text
        and not message.reply_to_message.sticker
    ):
        return await message.reply_text(
            "__**hanya bisa save text atau sticker.**__"
        )
    name = message.text.split(None, 1)[1].strip()
    if not name:
        return await message.reply_text(
            f"**Penggunaan:**\n__{cmds}filter [nama filternya]__"
        )
    chat_id = message.chat.id
    if message.chat.id in BL_GCAST:
        await message.edit("Filter tidak diperkenankan di group support")
        return
    _type = "text" if message.reply_to_message.text else "sticker"
    _filter = {
        "type": _type,
        "data": message.reply_to_message.text.markdown
        if _type == "text"
        else message.reply_to_message.sticker.file_id,
    }
    await save_filter(chat_id, name, _filter)
    await message.reply_text(f"__**filter {name} disimpan!.**__")

@geez("filters", cmds) #lu gay
async def get_filterss(_, message):
    _filters = await get_filters_names(message.chat.id)
    if not _filters:
        return await message.reply_text("**tidak ada filter tersimpan di group ini.**")
    _filters.sort()
    msg = f"daftar filter tersimpan di {message.chat.title}\n"
    for _filter in _filters:
        msg += f"**-** `{_filter}`\n"
    await message.reply_text(msg)

@geez("stopfilter", cmds) #lu gay
async def del_filter(_, message):
    if len(message.command) < 2:
        return await message.reply_text(f"**Penggunaan:**\n__{cmds}stopfilter [nama filternya]__")
    name = message.text.split(None, 1)[1].strip()
    if not name:
        return await message.reply_text(f"**Penggunaan:**\n__{cmds}stopfilter [nama filternya]__")
    chat_id = message.chat.id
    deleted = await delete_filter(chat_id, name)
    if deleted:
        await message.reply_text(f"*filter {name} berhasil dihapus.**")
    else:
        await message.reply_text("**filter tidak ditemukan.**")

@Client.on_message(filters.text & ~filters.private & ~filters.via_bot & ~filters.forwarded,group=chat_filters_group,)
async def filters_re(_, message):
    text = message.text.lower().strip()
    if not text:
        return
    chat_id = message.chat.id
    list_of_filters = await get_filters_names(chat_id)
    for word in list_of_filters:
        pattern = r"( |^|[^\w])" + re.escape(word) + r"( |$|[^\w])"
        if re.search(pattern, text, flags=re.IGNORECASE):
            _filter = await get_filter(chat_id, word)
            data_type = _filter["type"]
            data = _filter["data"]
            if data_type == "text":
                keyb = None
                if re.findall(r"\[.+\,.+\]", data):
                    keyboard = extract_text_and_keyb(ikb, data)
                    if keyboard:
                        data, keyb = keyboard

                if message.reply_to_message:
                    await message.reply_to_message.reply_text(
                        data,
                        reply_markup=keyb,
                        disable_web_page_preview=True,
                    )

                    if text.startswith("~"):
                        await message.delete()
                    return

                return await message.reply_text(
                    data,
                    reply_markup=keyb,
                    disable_web_page_preview=True,
                )
            if message.reply_to_message:
                await message.reply_to_message.reply_sticker(data)

                if text.startswith("~"):
                    await message.delete()
                return
            return await message.reply_sticker(data)
        
add_command_help(
    "fakeadmin",
    [
        [f"{cmds}savefilters <balas ke pesan atau sticker> <triger/nama filer>", "save filters."],
        [f"{cmds}stopfilter <triger/nama filter>", "menghapus filter."],
        [f"{cmds}filters", "melihat list filter."],
    ],
)