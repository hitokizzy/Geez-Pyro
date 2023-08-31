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
import requests
import wget
from functools import partial
from geezlibs.geez.helper import ReplyCheck
from geezlibs.geez.utils.tools import get_arg
from geezlibs.geez import geez
from pyrogram import Client, enums
from pyrogram.types import Message
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL
from pyrogram.errors import YouBlockedUser
from Geez.modules.basic import add_command_help
from Geez import cmds

async def tiktok_downloader(tiktok):
        url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"
        querystring = {"url":tiktok}
        headers = {
        "X-RapidAPI-Key": "3c7ace35d5mshd5223e5fc185146p1e2d15jsn3f9f0a73128c",
        "X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"
        }
        response = requests.get(url, headers=headers, params=querystring).json()["video"][0]
        return response

def run_sync(func, *args, **kwargs):
    return asyncio.get_event_loop().run_in_executor(None, partial(func, *args, **kwargs))

def get_text(message: Message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


@geez("vid", cmds)
async def yt_video(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "<b>Video not found,</b>\ntry another query.",
        )
    infomsg = await message.reply_text("<b>searching...</b>", quote=False)
    try:
        search = SearchVideos(str(message.text.split(None, 1)[1]), offset=1, mode="dict", max_results=1).result().get("search_result")
        link = f"https://youtu.be/{search[0]['id']}"
    except Exception as error:
        return await infomsg.edit(f"<b>searching...\n\nError: {error}</b>")
    ydl = YoutubeDL(
        {
            "quiet": True,
            "no_warnings": True,
            "format": "(bestvideo[height<=?720][width<=?1280][ext=mp4])+(bestaudio[ext=m4a])",
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "nocheckcertificate": True,
            "geo_bypass": True,
        }
    )
    await infomsg.edit(f"<b>Downloading...</b>")
    try:
        ytdl_data = await run_sync(ydl.extract_info, link, download=True)
        file_path = ydl.prepare_filename(ytdl_data)
        videoid = ytdl_data["id"]
        title = ytdl_data["title"]
        url = f"https://youtu.be/{videoid}"
        duration = ytdl_data["duration"]
        channel = ytdl_data["uploader"]
        views = f"{ytdl_data['view_count']:,}".replace(",", ".")
        thumbs = f"https://img.youtube.com/vi/{videoid}/hqdefault.jpg" 
    except Exception as error:
        return await infomsg.edit(f"<b>Downloader...\n\nError: {error}</b>")
    thumbnail = wget.download(thumbs)
    await client.send_video(
        message.chat.id,
        video=file_path,
        thumb=thumbnail,
        file_name=title,
        duration=duration,
        supports_streaming=True,
        caption="<b>Informasi :</b>\n\n<b>Nama:</b> {}\n<b>Durasi:</b> {}\n<b>Dilihat:</b> {}\n<b>Channel:</b> {}\n<b>Tautan:</b> <a href={}>Youtube</a>\n\n<b>Powered By Geez|Ram".format(
            title,
            duration,
            views,
            channel,
            url,
        ),
        reply_to_message_id=message.id,
    )
    await infomsg.delete()
    for files in (thumbnail, file_path):
        if files and os.path.exists(files):
            os.remove(files)


@geez("song", cmds)
async def yt_audio(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "<b>Song not found,</b>\nplease try another query.",
        )
    infomsg = await message.reply_text("<b>Searching...</b>", quote=False)
    try:
        search = SearchVideos(str(message.text.split(None, 1)[1]), offset=1, mode="dict", max_results=1).result().get("search_result")
        link = f"https://youtu.be/{search[0]['id']}"
    except Exception as error:
        return await infomsg.edit(f"<b>Searching...\n\nError: {error}</b>")
    ydl = YoutubeDL(
        {
            "quiet": True,
            "no_warnings": True,
            "format": "bestaudio[ext=m4a]",
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "nocheckcertificate": True,
            "geo_bypass": True,
        }
    )
    await infomsg.edit(f"<b>Downloading...</b>")
    try:
        ytdl_data = await run_sync(ydl.extract_info, link, download=True)
        file_path = ydl.prepare_filename(ytdl_data)
        videoid = ytdl_data["id"]
        title = ytdl_data["title"]
        url = f"https://youtu.be/{videoid}"
        duration = ytdl_data["duration"]
        channel = ytdl_data["uploader"]
        views = f"{ytdl_data['view_count']:,}".replace(",", ".")
        thumbs = f"https://img.youtube.com/vi/{videoid}/hqdefault.jpg" 
    except Exception as error:
        return await infomsg.edit(f"<b>Downloader...\n\nError: {error}</b>")
    thumbnail = wget.download(thumbs)
    await client.send_audio(
        message.chat.id,
        audio=file_path,
        thumb=thumbnail,
        file_name=title,
        duration=duration,
        caption="<b>Informasi :</b>\n\n<b>Nama:</b> {}\n<b>Durasi:</b> {}\n<b>Dilihat:</b> {}\n<b>Channel:</b> {}\n<b>Tautan:</b> <a href={}>Youtube</a>\n\n<b>Powered By Geez|Ram".format(
            title,
            duration,
            views,
            channel,
            url,
        ),
        reply_to_message_id=message.id,
    )
    await infomsg.delete()
    for files in (thumbnail, file_path):
        if files and os.path.exists(files):
            os.remove(files)
            
            
@geez("sosmed", cmds)
async def sosmed(client: Client, message: Message):
    prik = await message.edit("`Processing . . .`")
    link = get_arg(message)
    bot = "thisvidbot"
    if link:
        try:
            tuyul = await client.send_message(bot, link)
            await asyncio.sleep(5)
            await tuyul.delete()
        except YouBlockedUser:
            await client.unblock_user(bot)
            tuyul = await client.send_message(bot, link)
            await asyncio.sleep(10)
            await tuyul.delete()
    async for sosmed in client.search_messages(
        bot, filter=enums.MessagesFilter.VIDEO, limit=1
    ):
        await asyncio.gather(
            prik.delete(),
            client.send_video(
                message.chat.id,
                sosmed.video.file_id,
                caption=f"**Upload by:** {client.me.mention}",
                reply_to_message_id=ReplyCheck(message),
            ),
        )
        await client.delete_messages(bot, 2)

@geez("tt", cmds)
async def tiktok_dl(client: Client, message: Message):
    try:
        mess = await message.reply("Processing...")
        split_result = message.text.split(" ", 1)
        
        if len(split_result) < 2:
            await message.reply("Berikan link TikTok")
            return True

        tiktok = split_result[1].strip()
        if not tiktok:
            return await mess.edit("Berikan link TikTok untuk download!")

        tiktoker = await tiktok_downloader(tiktok)
        try:
            await client.send_video(
                chat_id=message.chat.id,
                video=tiktoker,
                caption=f"Powered by {client.me.mention}",
                reply_to_message_id=message.id
            )
            await mess.delete()
        except Exception as e:
            await mess.edit("Error: " + str(e))
    except Exception as e:
        await message.reply("An error occurred: " + str(e))


add_command_help(
    "youtube",
    [
        [f"{cmds}song <title>", "Download Audio From YouTube."],
        [f"{cmds}vid <title>", "Download Video from YouTube."],
    ],
)

add_command_help(
    "sosmed",
    [
        [f"{cmds}sosmed <link>",
            "Untuk Mendownload Media Dari Facebook / Tiktok / Instagram / Twitter / YouTube."],
        [f"{cmds}copy <link telegram>", "Download media dari channel atau group"],
        [f"{cmds}tt <link tiktok>", "Mendowload media dari tiktok"]
    ],
)
