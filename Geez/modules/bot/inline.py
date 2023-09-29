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
import random
import time
import traceback
from sys import version as pyver
from datetime import datetime

from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pyrogram.enums import ParseMode
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineQueryResultPhoto,
    Message,
)
from geezlibs.geez.helper.data import Data
from geezlibs.geez.helper.inline import inline_wrapper, paginate_help
from geezlibs import BOT_VER, __version__ as gver
from Geez import CMD_HELP, StartTime, app
from config import OWNER_ID


geezlogo = [
    "https://telegra.ph/file/d03ce0fb84f81be3aeb09.png",
    "https://telegra.ph/file/200355acbe58c46400f5b.png",
    "https://telegra.ph/file/c78bb1efdeed38ee16eb2.png",
    "https://telegra.ph/file/4143843c984a8ecdc813e.png"
]

async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


async def alive_function(message: Message, answers):
    uptime = await get_readable_time((time.time() - StartTime))
    msg = f"""
<b> Geez-Pyro™ </b>

<b> • User :</b> {message.from_user.mention}
<b> • Plugins :</b> <code>{len(CMD_HELP)} Modules</code>
<b> • Python Version :</b> <code>{pyver.split()[0]}</code>
<b> • Pyrogram Version :</b> <code>{pyrover}</code>
<b> • Geezlibs Version :</b> <code>{gver}</code>
<b> • Bot Uptime :</b> <code>{uptime}</code>
<b> • Bot version:</b> <code>{BOT_VER}</code>
"""
    answers.append(
        InlineQueryResultArticle(
            title="Alive",
            description="Check Bot's Stats",
            thumb_url="https://telegra.ph/file/c78bb1efdeed38ee16eb2.png",
            input_message_content=InputTextMessageContent(
                msg, parse_mode=ParseMode.HTML, disable_web_page_preview=True
            ),
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("ʜᴇʟᴘ", callback_data="helper")]]
            ),
        )
    )
    return answers


async def ping_function(message: Message, answers):
    start = datetime.now()
    uptime = await get_readable_time((time.time() - StartTime))
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    msg = (
        f"<b>Geez - Pyro!!🎈</b>\n\n"
        f"ping :</b> <code>{duration}ms</code>\n"
        f"uptime :</b> <code>{uptime}</code>"
    )
    answers.append(
        InlineQueryResultArticle(
            title="ping",
            description="Check Bot's Stats",
            thumb_url="https://telegra.ph/file/c78bb1efdeed38ee16eb2.png",
            input_message_content=InputTextMessageContent(
                msg, parse_mode=ParseMode.HTML, disable_web_page_preview=True
            ),
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Support", url="t.me/GeezRam")]]
            ),
        )
    )
    return answers

async def help_function(answers):
    bttn = paginate_help(0, CMD_HELP, "helpme")
    photo_url = random.choice(geezlogo)
    answers.append(
        InlineQueryResultArticle(
            title="Help Article!",
            thumb_url=photo_url,
            input_message_content=InputTextMessageContent(
                Data.text_help_menu.format(len(CMD_HELP))
            ),
            reply_markup=InlineKeyboardMarkup(bttn),
        )
    )
    return answers

@app.on_callback_query()
def pmowner(client, callback_query):
    user_id = OWNER_ID
    message = "saya ingin bertanya kak"
    client.send_message(user_id, message)
    client.answer_callback_query(callback_query.id, text="Message sent")

@app.on_inline_query()
@inline_wrapper
async def inline_query_handler(client: Client, query):
    try:
        text = query.query.strip().lower()
        string_given = query.query.lower()
        answers = []
        if text.strip() == "":
            return
        elif text.split()[0] == "alive":
            answerss = await alive_function(query, answers)
            await client.answer_inline_query(query.id, results=answerss, cache_time=5)
        elif string_given.startswith("helper"):
            answers = await help_function(answers)
            await client.answer_inline_query(query.id, results=answers, cache_time=5)
        elif string_given.startswith("ping"):
            answers = await ping_function(query, answers)
            await client.answer_inline_query(query.id, results=answers, cache_time=5)
    except Exception as e:
        e = traceback.format_exc()
        print(e, "InLine")
