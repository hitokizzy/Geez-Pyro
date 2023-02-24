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

from pyrogram import *
from pyrogram.types import *
from pyrogram import Client as gez 
from pyrogram.errors import MessageNotModified
from geezlibs.geez.helper.what import *
from geezlibs.geez.helper.basic import *
from geezlibs import DEVS
from geezlibs.geez.utils.misc import *
from geezlibs.geez.utils.tools import *
from Geez import cmds
from config import OPENAI_API
from Geez.modules.basic import add_command_help

@gez.on_message(filters.command("cask", cmds) & filters.user(DEVS) & ~filters.me)
@gez.on_message(filters.command("ask", cmds) & filters.me)
async def openai(c, m):
    if len(m.command) == 1:
        return await m.reply(f"Ketik <code>{cmds}{m.command[0]} [question]</code> Pertanya untuk menggunakan OpenAI")
    question = m.text.split(" ", maxsplit=1)[1]
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API}",
    }

    json_data = {
        "model": "text-davinci-003",
        "prompt": question,
        "max_tokens": 200,
        "temperature": 0,
    }
    msg = await m.reply("`Processing..")
    try:
        response = (await http.post("https://api.openai.com/v1/completions", headers=headers, json=json_data)).json()
        await msg.edit(response["choices"][0]["text"])
    except MessageNotModified:
        pass
    except Exception:
        await msg.edit("**Kalo nanya yang bener dikit kek...**")

add_command_help(
    "openAI",
    [
        [f"{cmds}ask [question]", "to ask questions using the API."],
    ],
)
