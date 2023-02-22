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

import asyncio
import os
import speech_recognition as sr
import ffmpeg
from gtts import gTTS
from pyrogram import Client, filters
from pyrogram.types import Message
from geezlibs.geez.utils.tools import run_in_exc
from geezlibs import logging
from Geez import cmds
from geezlibs.geez import geez
from geezlibs.geez.helper.basic import *
from geezlibs.geez.utils.misc import *
from geezlibs.geez.utils.tools import *
from Geez.modules.basic import add_command_help

lang = "id"  # Default Language for voice


@geez(["voice", "tts"], cmds)
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


@geez("voicelang", cmds)
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

@geez("stt", cmds)
async def speech_to_text(client: Client, message: Message):
    reply = message.reply_to_message
    if not (reply and reply.voice):
        return await message.edit("Please reply to a voice message")
    await message.edit("processing...")
    voice_file = await client.download_media(message=reply, file_name='downloads/voice.ogg')

    @run_in_exc
    def convert_to_raw(audio_original, raw_file_name):
        stream = ffmpeg.input(audio_original)
        stream = ffmpeg.output(stream, raw_file_name, format="wav", acodec="pcm_s16le", ac=2, ar="48k", loglevel="error").overwrite_output().run()
        return raw_file_name

    # kata piki LU BABI !!!
    recognizer = sr.Recognizer()
    wav_file = await convert_to_raw(voice_file, 'downloads/voice.wav')
    with sr.AudioFile(wav_file) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio, language="id-ID")
    except sr.UnknownValueError:
        return await message.edit("Suara tidak jelas...")
    except sr.RequestError as e:
        return await message.edit("Error, service tidak tersedia sementara waktu; {0}".format(e))
    await message.reply_text(
        text=text
    )
    
    # kata rama LU KONTOL !!!
    os.remove(wav_file)
    os.remove(voice_file)


add_command_help(
    "voice",
    [
        [f"{cmds}tts [reply]", "Ubah teks menjadi suara oleh google."],
        [f"{cmds}stt [reply]", "ubah Voice Note menjadi text (default bahasa : Indonesia)."],
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
