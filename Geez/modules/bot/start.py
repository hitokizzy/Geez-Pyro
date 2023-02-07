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
import random
import asyncio
from prettytable import PrettyTable
from Geez import app, CMD_HELP, cmds
from pyrogram import filters, Client,enums
from geezlibs.geez.helper.PyroHelpers import ReplyCheck
from geezlibs.geez.helper.utility import split_list
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from config import BOTLOG_CHATID, OWNER_ID
from Geez.modules.basic.help import edit_or_reply

@app.on_callback_query()
def pmowner(client, callback_query):
    user_id = OWNER_ID
    message = "saya ingin bertanya kak"
    client.send_message(user_id, message)
    client.answer_callback_query(callback_query.id, text="Message sent")

geezlogo = [
    "https://telegra.ph/file/d03ce0fb84f81be3aeb09.png",
    "https://telegra.ph/file/200355acbe58c46400f5b.png",
    "https://telegra.ph/file/c78bb1efdeed38ee16eb2.png",
    "https://telegra.ph/file/4143843c984a8ecdc813e.png"
]

alive_logo = random.choice(geezlogo)

@app.on_message(filters.command("start") & filters.private)
async def start(app, message):
   chat_id = message.chat.id
   file_id = alive_logo
   caption = "Yoo, saya geez Pyro Assistant, gada yang spesial dari saya/n tapi boong..."
   reply_markup = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Support", url="https://t.me/GeezRam"),
            InlineKeyboardButton("Repo", url="https://github.com/hitokizzy/Geez/Pyro"),
        ],
    ])
   await app.send_photo(chat_id, file_id, caption=caption, reply_markup=reply_markup)

@app.on_message(filters.command("help") & filters.private)
async def help(app, message):
    cmd = message.command
    help_arg = ""
    if len(cmd) > 1:
        help_arg = " ".join(cmd[1:])
    elif not message.reply_to_message and len(cmd) == 1:
        try:
            nice = await app.get_inline_bot_results(query="helper")
            await asyncio.gather(
                message.delete(),
                app.send_inline_bot_result(
                    message.chat.id, nice.query_id, nice.results[0].id
                ),
            )
        except BaseException as e:
            print(f"{e}")
            ac = PrettyTable()
            ac.header = False
            ac.title = "Geez Pyro Plugins"
            ac.align = "l"
            for x in split_list(sorted(CMD_HELP.keys()), 2):
                ac.add_row([x[0], x[1] if len(x) >= 2 else None])
            xx = await app.send_message(
                message.chat.id,
                f"```{str(ac)}```\n• @GeezRam >< @UserbotCh •",
                reply_to_message_id=ReplyCheck(message),
            )
            await xx.reply(
                f"**Usage:** `{cmds}help broadcast` **To View Module Information**"
            )
            return

    if help_arg:
        if help_arg in CMD_HELP:
            commands: dict = CMD_HELP[help_arg]
            this_command = f"**Help For {str(help_arg).upper()}**\n\n"
            for x in commands:
                this_command += f"**Command:** `{str(x)}`\n  ∟ **Function:** `{str(commands[x])}`\n\n"
            this_command += "© @GeezRam >< @UserbotCh"
            await edit_or_reply(
                message, this_command, parse_mode=enums.ParseMode.MARKDOWN
            )
        else:
            await edit_or_reply(
                message,
                f"`{help_arg}` **tidak ada dalam list modul.**",
            )