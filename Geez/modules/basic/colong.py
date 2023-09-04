import asyncio
from pyrogram.enums import MessagesFilter
from geezlibs.geez import geez
from Geez import cmds
from Geez.modules.basic import add_command_help



@geez(["colong"], cmds)
async def _(client, message):
    results = {
        "photo": MessagesFilter.PHOTO,
        "audio": MessagesFilter.AUDIO,
        "video": MessagesFilter.VIDEO,
        "dokumen": MessagesFilter.DOCUMENT,
    }
    meira = await message.reply("Tunggu Sebentar")
    if len(message.command) < 3:
        return await meira.edit(
            f"<code><b>{message.text} from_chat msg_filter msg_limit to_chat</code></b>"
        )
    if message.command[2] in results:
        msg_ = results[message.command[2]]
    else:
        return await meira.edit(
            f" msg_filter {message.command[2]} tidak bisa diproses\n\n msg_filter yang tersedia adalah: <code>dokumen</code> <code>photo</code> <code>audio</code> <code>video</code>"
        )
    await meira.edit("Sedang Memproses")
    try:
        done = 0
        async for msg in client.search_messages(
            message.command[1], filter=msg_, limit=int(message.command[3])
        ):
            await msg.copy(message.command[4])
            done += 1
            await asyncio.sleep(3)
    except Exception as error:
        return await meira.edit(error)
    await meira.delete()
    return await message.reply(
        f" {done}/{message.command[3]} {message.command[2]} telah berhasil diambil"
    )

add_command_help(
    "colong",
    [
        [f"{cmds}colong[ch/gc] [photo/video] [jumlah]", "ayo tebak ini apa..."],
    ],
)