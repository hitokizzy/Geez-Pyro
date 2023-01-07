import asyncio
import os
import time

import wget
from pyrogram import Client, filters
from pyrogram.types import Message
from youtubesearchpython import SearchVideos
from yt_dlp import YoutubeDL
from pyrogram import Client as gez

from geez.modules.help import add_command_help


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


@gez.on_message(
    filters.command(["vid", "video"], ".") & filters.me
)
async def yt_vid(client: Client, message: Message):
    input_st = message.text
    input_str = input_st.split(" ", 1)[1]
    geez = await message.reply("`Bentar...`")
    if not input_str:
        await geez.edit_text(
            "`Lah au yaaa`"
        )
        return
    await geez.edit_text(f"`Otw nyari {input_str} dari anu...`")
    search = SearchVideos(str(input_str), offset=1, mode="dict", max_results=1)
    rt = search.result()
    result_s = rt["search_result"]
    url = result_s[0]["link"]
    vid_title = result_s[0]["title"]
    yt_id = result_s[0]["id"]
    uploade_r = result_s[0]["channel"]
    thumb_url = f"https://img.youtube.com/vi/{yt_id}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    downloaded_thumb = wget.download(thumb_url)
    opts = {
        "format": "best",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
        "outtmpl": "%(id)s.mp4",
        "logtostderr": False,
        "quiet": True,
    }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url, download=True)
    except Exception as e:
        await geez.edit_text(f"**Bloon amat si** \n**Error :** `{str(e)}`")
        return
    time.time()
    file_path = f"{ytdl_data['id']}.mp4"
    capy = f"🏷 **Video Name ►** `{vid_title}` \n🧸 **Requested For ►** `{input_str}` \n💌 **Channel ►** `{uploade_r}` \n**Link ►** `{url}`"
    await client.send_video(
        message.chat.id,
        video=open(file_path, "rb"),
        duration=int(ytdl_data["duration"]),
        file_name=str(ytdl_data["title"]),
        thumb=downloaded_thumb,
        caption=capy,
        supports_streaming=True,
    )
    await geez.delete()
    for files in (downloaded_thumb, file_path):
        if files and os.path.exists(files):
            os.remove(files)


@gez.on_message(filters.command("lagu", ".") & filters.me)
async def song(client: Client, message: Message):
    input_str = get_text(message)
    rep = await message.reply("`Bentar...`")
    if not input_str:
        await rep.edit(
            "`Lah au yaaa`"
        )
        return
    await rep.edit(f"`Otw nyari {input_str} dari anu....`")
    search = SearchVideos(str(input_str), offset=1, mode="dict", max_results=1)
    rt = search.result()
    result_s = rt["search_result"]
    url = result_s[0]["link"]
    vid_title = result_s[0]["title"]
    yt_id = result_s[0]["id"]
    uploade_r = result_s[0]["channel"]
    thumb_url = f"https://img.youtube.com/vi/{yt_id}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    downloaded_thumb = wget.download(thumb_url)
    opts = {
        "format": "bestaudio",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "writethumbnail": True,
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "720",
            }
        ],
        "outtmpl": "%(id)s.mp3",
        "quiet": True,
        "logtostderr": False,
    }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url, download=True)
    except Exception as e:
        await rep.edit(f"**Bloon amat si** \n**Error :** `{str(e)}`")
        return
    time.time()
    file_sung = f"{ytdl_data['id']}.mp3"
    capy = f"**🏷 Song Name ►** `{vid_title}` \n🧸 **Requested For ►** `{input_str}` \n💌 **Channel ►** `{uploade_r}` \n📎 **Link ►** `{url}`"
    await client.send_audio(
        message.chat.id,
        audio=open(file_sung, "rb"),
        title=str(ytdl_data["title"]),
        performer=str(ytdl_data["uploader"]),
        thumb=downloaded_thumb,
        caption=capy,
    )
    await rep.delete()
    for files in (downloaded_thumb, file_sung):
        if files and os.path.exists(files):
            os.remove(files)


add_command_help(
    "Youtube",
    [
        [".lagu <title>", "Download Audio From YouTube."],
        [".video <title>", "Download Video from YouTube."],
        [".tt <link>", "Download Video Tiktok tanpa Watermark."],
    ],
)
