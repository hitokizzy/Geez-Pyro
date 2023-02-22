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

from pyrogram import Client
from pyrogram.types import Message
from geezlibs.geez import geez
from geezlibs.geez.database import add_sudo, get_sudoers, remove_sudo
from Geez import cmds, SUDOERS
from Geez.modules.basic.help import add_command_help
from config import OWNER_ID

@geez("addsudo", cmds)
async def useradd(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.edit("Reply to someone's message to add him to sudoers.",)
    user_id = message.reply_to_message.from_user.id
    umention = (await client.get_users(user_id)).mention
    sudoers = await get_sudoers()

    if user_id in sudoers:
        return await message.edit(f"{umention} is already in sudoers.")
    if user_id == OWNER_ID:
        return await message.edit("You can't add your self in sudoers.")

    await add_sudo(user_id)

    if user_id not in SUDOERS:
        SUDOERS.add(user_id)

    await message.edit(f"Successfully added {umention} in sudoers.")

@geez("rmsudo", cmds)
async def rmsudo(client: Client, message: Message):
    if not message.reply_to_message:
        return await message.edit("Reply to someone's message to remove him to sudoers.")
    user_id = message.reply_to_message.from_user.id
    umention = (await client.get_users(user_id)).mention

    if user_id not in await get_sudoers():
        return await message.edit(f"{umention} is not in sudoers.")

    await remove_sudo(user_id)

    if user_id in SUDOERS:
        SUDOERS.remove(user_id)

    await message.edit(f"Successfully removed {umention} from sudoers.")

@geez("listsudo", cmds)
async def sudoers_list(client: Client, message: Message):
    sudoers = await get_sudoers()
    text = ""
    j = 0
    for user_id in sudoers:
        try:
            user = await client.get_users(user_id)
            user = user.first_name if not user.mention else user.mention
            j += 1
        except Exception:
            continue
        text += f"{j}. {user}\n"
    if text == "":
        return await message.edit("No sudoers found.")
    await message.reply(text)

add_command_help(
    "Sudo",
    [
        [f"{cmds}addsudo <reply/berikan id>", "menambahkan sudo user."],
        [f"{cmds}rmsudo", "menghapus sudo user."],
        [f"{cmds}listsudo", "melihat daftar sudo user."],
    ],
)