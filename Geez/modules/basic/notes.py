"""
if you can read this, this meant you use code from Geez | Ram Project
this code is from somewhere else
please dont hestitate to steal it
because Geez and Ram doesn't care about credit
at least we are know as well
who Geez and Ram is


kopas repo dan hapus credit, ga akan jadikan lu seorang developer

YANG NYOLONG REPO INI TRUS DIJUAL JADI PREM, LU GAY...
©2023 Geez | Ram Team
"""
from pyrogram.types import Message
from geezlibs.geez.database import get_note, get_note_names, save_note, delete_note
from geezlibs.geez import geez
from Geez.modules.basic import add_command_help
from Geez import cmds

@geez("notes", cmds)
async def get_notes(_, message: Message):
    chat_id = message.chat.id
    _notes = await get_note_names(chat_id)
    if not _notes:
        return await message.edit("**Tidak menyimpan notes disini.**")
    _notes.sort()
    msg = f"List of notes in {message.chat.title}\n"
    for note in _notes:
        msg += f"**-** `{note}`\n"
    await message.edit(msg)

@geez("savenote", cmds)
async def notes(client, message: Message):
    if len(message.command) < 2 or not message.reply_to_message:
        await message.edit("**balas ke pesan atau stiker untuk save.**")
    #kata piki sama rama LU BABI !!!!
    elif (not message.reply_to_message.text and not message.reply_to_message.sticker):
        await message.edit("**hanya bisa menyimpan catatan dan sticker.**",)
    else:
        name = message.text.split(None, 1)[1].strip()
        if not name:
            return await message.edit(f"contoh: {cmds}savenote <nama note>")
        _type = "text" if message.reply_to_message.text else "sticker"
        note = {
            "type": _type,
            "data": message.reply_to_message.text.markdown
            if _type == "text"
            else message.reply_to_message.sticker.file_id,}
        #kata izzy SUKA SUKA LU AJA TONG !!!
        chat_id = message.chat.id
        await save_note(chat_id, name, note)
        await message.edit(f"__**Saved note {name}.**__")

@geez("delnote", cmds)
async def del_note(_, message):
    if len(message.command) < 2:
        return await message.edit(f"gunakan {cmds}delnote <nama note>")
    name = message.text.split(None, 1)[1].strip()
    if not name:
        return await message.edit(f"gunakan {cmds}delnote <nama note>")
    chat_id = message.chat.id
    deleted = await delete_note(chat_id, name)
    if deleted:
        await message.edit(f"**{name} berhasil dihapus.**")
    else:
        await message.edit("**Tidak ada notes tersimpan.**")

@geez("get", cmds)
async def get_one_note_userbot(_, message):
    if len(message.text.split()) < 2:
        return await message.edit("argument tidak valid")
    name = message.text.split(None, 1)[1]
    _note = await get_note(message.chat.id, name)
    if not _note:
        return await message.edit("notes tidak ditemukan.")
    if _note["type"] == "text":
        data = _note["data"]
        await message.edit(data,
            disable_web_page_preview=True,
        )
    else:
        await message.reply_sticker(_note["data"])

add_command_help(
    "notes",
    [
        [f"{cmds}notes", "Melihat catatan tersimpan."],
        [f"{cmds}savenote <nama catatan>", "menyimpan catatan atau sticker di group."],
        [f"{cmds}delnote <nama catatan>", "menghapus catatan atau sticker di group."],
        [f"{cmds}get <nama catatan>", "mengambil catatan atau sticker di group."],
    ],
)