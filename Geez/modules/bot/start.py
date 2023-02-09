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
from Geez import app
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from config import OWNER_ID

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
    caption = "Yoo, saya geez Pyro Assistant, gada yang spesial dari saya\n tapi boong..."
    reply_markup = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Support", url="https://t.me/GeezRam"),
            InlineKeyboardButton("Repo", url="https://github.com/hitokizzy/Geez/Pyro"),
        ],
        [
            InlineKeyboardButton("PM Owner", callback_data="pmowner"),
        ],
    ])

    await app.send_photo(chat_id, file_id, caption=caption, reply_markup=reply_markup)
