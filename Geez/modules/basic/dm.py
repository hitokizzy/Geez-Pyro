from pyrogram import Client
from pyrogram.types import Message
from Geez.modules.basic import add_command_help
from Geez import cmds

@Client.on_message(filters.command(["directmessage", "dm"], cmd) & filters.me)
async def dm(coli: Client, memek: Message):
    geez = await memek.reply_text("⚡ Proccessing.....")
    quantity = 1
    inp = memek.text.split(None, 2)[1]
    user = await coli.get_chat(inp)
    spam_text = ' '.join(memek.command[2:])
    quantity = int(quantity)

    if memek.reply_to_message:
        reply_to_id = memek.reply_to_message.message_id
        for _ in range(quantity):
            await geez.edit("Message Sended Successfully 😘")
            await coli.send_message(user.id, spam_text,
                                      reply_to_messsge_id=reply_to_id)
            await asyncio.sleep(0.15)
        return

    for _ in range(quantity):
        await coli.send_message(user.id, spam_text)
        await geez.edit("Message Sended Successfully 😘")
        await asyncio.sleep(0.15)


add_command_help(
    "directmessage",
    [
        [f"{cmds}dm @username / {cmds}directmessage @username", "Untuk Mengirim Pesan Tanpa Harus Kedalam Roomchat.",],
    ],
)
