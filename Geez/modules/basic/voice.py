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
import os

from gtts import gTTS
from pyrogram import Client, filters
from pyrogram.raw import functions
from pyrogram.types import Message
from datetime import datetime


from Geez import *
from geezlibs.geez.helper.basic import *
from geezlibs.geez.utils.misc import *
from geezlibs.geez.utils.tools import *
from Geez.modules.basic import add_command_help, DEVS

lang = "id"  # Default Language for voice


@Client.on_message(filters.me & filters.command(["voice", "tts"], cmds))
async def voice(client: Client, message):
    global lang
    cmd = message.command
    if len(cmd) > 1:
        v_text = " ".join(cmd[1:])
    elif message.reply_to_message and len(cmd) == 1:
        v_text = message.reply_to_message.text
    elif not message.reply_to_message and len(cmd) == 1:
        await edit_or_reply(
            message,
            "**Balas ke pesan atau kirim argumen teks untuk mengonversi ke suara**",
        )
        return
    await client.send_chat_action(message.chat.id, enums.ChatAction.RECORD_AUDIO)
    # noinspection PyUnboundLocalVariable
    tts = gTTS(v_text, lang=lang)
    tts.save("voice.mp3")
    if message.reply_to_message:
        await asyncio.gather(
            message.delete(),
            client.send_voice(
                message.chat.id,
                voice="voice.mp3",
                reply_to_message_id=message.reply_to_message.id,
            ),
        )
    else:
        await client.send_voice(message.chat.id, enums.ChatAction.RECORD_AUDIO)
    await client.send_chat_action(message.chat.id, enums.ChatAction.CANCEL)
    os.remove("voice.mp3")


@Client.on_message(filters.me & filters.command(["voicelang"], cmds))
async def voicelang(client: Client, message: Message):
    global lang
    temp = lang
    lang = message.text.split(None, 1)[1]
    try:
        gTTS("tes", lang=lang)
    except Exception:
        await edit_or_reply(message, "`Mohon masukan kode bahasa`")
        lang = temp
        return
    await edit_or_reply(
        message, "**Bahasa untuk Voice Google diganti menjadi** `{}`".format(lang)
    )


add_command_help(
    "Voice",
    [
        [f"voice atau {cmds}tts [reply]", "Ubah teks menjadi suara oleh google."],
        [
            f"{cmds}voicelang (lang_id) ",
            "Setel bahasa suara anda\n\nBeberapa Bahasa Suara yang Tersedia:"
            "\nID| Language  | ID| Language\n"
            "af: Afrikaans | ar: Arabic\n"
            "cs: Czech     | de: German\n"
            "el: Greek     | en: English\n"
            "es: Spanish   | fr: French\n"
            "hi: Hindi     | id: Indonesian\n"
            "is: Icelandic | it: Italian\n"
            "ja: Japanese  | jw: Javanese\n"
            "ko: Korean    | la: Latin\n"
            "my: Myanmar   | ne: Nepali\n"
            "nl: Dutch     | pt: Portuguese\n"
            "ru: Russian   | su: Sundanese\n"
            "sv: Swedish   | th: Thai\n"
            "tl: Filipino  | tr: Turkish\n"
            "vi: Vietname  |\n"
            "zh-cn: Chinese (Mandarin/China)\n"
            "zh-tw: Chinese (Mandarin/Taiwan)",
        ],
    ],
)
