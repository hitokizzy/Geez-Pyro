import os
import math
import os
import shlex
import time
from math import ceil
import logging
import ffmpeg
from geez import app
from pyrogram import Client, filters
from pyrogram import Client as gez
from pyrogram.types import Message

import functools
import threading
from concurrent.futures import ThreadPoolExecutor
from pyrogram.errors import FloodWait, MessageNotModified
import multiprocessing
import time
import calendar
from geez.helper.tools import *
from geez.modules.help.help import *
from pytgcalls import GroupCallFactory, GroupCallFileAction
import signal
import random
import string
import asyncio
import os
import time
import requests
import datetime
from yt_dlp import YoutubeDL
from youtubesearchpython import SearchVideos

s_dict = {}
GPC = {}

@gez.on_message(filters.command(["playlist"], ".") & filters.me
)
async def pl(client, message):
    group_call = GPC.get((message.chat.id, client.me.id))
    play = await edit_or_reply(message, "`Bentar Cuk!`")
    song = f"**📋 Daftar Menu {message.chat.title} :** \n"
    s = s_dict.get((message.chat.id, client.me.id))
    if not group_call:
        return await play.edit("`Minimal Buka Os Lag`")
    if not s:
        if group_call.is_connected:
            return await play.edit(f"**📀 Sedang diputar :** `{group_call.song_name}`")
        else:
            return await play.edit("`Minimal Buka Os Lag`")
    if group_call.is_connected:
        song += f"**📀 Sedang diputar :** `{group_call.song_name}` \n\n"
    for sno, i in enumerate(s, start=1):
        song += f"**{sno} 🎧** [{i['song_name']}]({i['url']}) `| {i['singer']} | {i['dur']}` \n\n"
    await play.edit(song, disable_web_page_preview=True)
    
async def get_chat_(client, chat_):
    chat_ = str(chat_)
    if chat_.startswith("-100"):
        try:
            return (await client.get_chat(int(chat_))).id
        except ValueError:
            chat_ = chat_.split("-100")[1]
            chat_ = '-' + str(chat_)
            return int(chat_)
        
async def playout_ended_handler(group_call, filename):
    client_ = group_call.client
    chat_ = await get_chat_(client_, f"-100{group_call.full_chat.id}")
    chat_ = int(chat_)
    s = s_dict.get((chat_, client_.me.id))
    if os.path.exists(group_call.input_filename):
        os.remove(group_call.input_filename)
    if not s:
        await group_call.stop()
        del GPC[(chat_, client.me.id)]
        return
    name_ = s[0]['song_name']
    singer_ = s[0]['singer']
    dur_ = s[0]['dur']
    raw_file = s[0]['raw']
    link = s[0]['url']
    file_size = humanbytes(os.stat(raw_file).st_size)
    song_info = f'<u><b>📀 Sedang dimainkan</b></u> \n<b>🎵 Lagu :</b> <a href="{link}">{name_}</a> \n<b>🎸 Artis :</b> <code>{singer_}</code> \n<b>⏲️ Waktu :</b> <code>{dur_}</code> \n<b>📂 Ukuran :</b> <code>{file_size}</code>'
    await client_.send_message(
        chat_, 
        song_info,
        disable_web_page_preview=True,
    )
    s.pop(0)
    logging.debug(song_info)
    group_call.song_name = name_
    group_call.input_filename = raw_file

@gez.on_message(filters.command(["skip"], ".") & filters.me
)
async def ski_p(client, message):
    m_ = await edit_or_reply(message, "`Bentar Cuk!`")
    no_t_s = get_text(message)
    group_call = GPC.get((message.chat.id, client.me.id))
    s = s_dict.get((message.chat.id, client.me.id))
    if not group_call:
        await m_.edit("`Yang Bener Lah...`")
        return 
    if not group_call.is_connected:
        await m_.edit("`Yang Bener Lah...`")
        return 
    if not no_t_s:
        return await m_.edit("`Yang Bener Dikit Lah...`")
    if no_t_s == "current":
        if not s:
            return await m_.edit("`Lah tau yaaa`")
        next_s = s[0]['raw']
        name = str(s[0]['song_name'])
        s.pop(0)
        prev = group_call.song_name
        group_call.input_filename = next_s
        return await m_.edit(f"`Ganti Lagu {prev}📀 Sedang dimainkan {name}!`")       
    else:
        if not s:
            return await m_.edit("`Laah kaga tau bujet !`")
        if not no_t_s.isdigit():
            return await m_.edit("`Kasih angka anjay...`")
        no_t_s = int(no_t_s)
        if int(no_t_s) == 0:
            return await m_.edit("`0? Lah tau yaaaa?`")
        no_t_s = int(no_t_s - 1)
        try:
            s_ = s[no_t_s]['song_name']
            s.pop(no_t_s)
        except:
            return await m_.edit("`Buset dah luh.`")
        return await m_.edit(f"`Ganti Lagu : {s_} At Posisi #{no_t_s}`")
   
                
@gez.on_message(filters.command(["play"], ".") & filters.me
)
async def play_m(client, message):
    group_call = GPC.get((message.chat.id, client.me.id))
    u_s = await edit_or_reply(message, "`Processing..`")
    input_str = get_text(message)
    if not input_str:
        if not message.reply_to_message:
            return await u_s.edit_text("`Minimal kasih judul lah....`")
        if not message.reply_to_message.audio:
            return await u_s.edit("`Minimal kasih judul lah....`")
        await u_s.edit_text("`Bentar cuy otw...`")
        audio = message.reply_to_message.audio
        audio_original = await message.reply_to_message.download()
        vid_title = audio.title or audio.file_name
        uploade_r = message.reply_to_message.audio.performer or "Unknown Artist."
        dura_ = message.reply_to_message.audio.duration
        dur = datetime.timedelta(seconds=dura_)
        raw_file_name = (
            ''.join(random.choice(string.ascii_lowercase) for i in range(5))
            + ".raw"
        )

        url = message.reply_to_message.link
    else:
        search = SearchVideos(str(input_str), offset=1, mode="dict", max_results=1)
        rt = search.result()
        result_s = rt.get("search_result")
        if not result_s:
           return await u_s.edit(f"`Lah tau ya kaga nemu - {input_str}, Judul yang bener banh....`")
        url = result_s[0]["link"]
        dur = result_s[0]["duration"]
        vid_title = result_s[0]["title"]
        yt_id = result_s[0]["id"]
        uploade_r = result_s[0]["channel"]
        start = time.time()
        try:
           audio_original = await yt_dl(url, client, message, start)
        except BaseException as e:
           return await u_s.edit(f"**Lah bujet gagal** \n**Error :** `{str(e)}`")
        raw_file_name = (
            ''.join(random.choice(string.ascii_lowercase) for i in range(5))
            + ".raw"
        )

    try:
        raw_file_name = await convert_to_raw(audio_original, raw_file_name)
    except BaseException as e:
        return await u_s.edit(f"`Lah tau ngapa ini...` \n**Error :** `{e}`")
    if os.path.exists(audio_original):
        os.remove(audio_original)
    if not group_call:
        group_call = GroupCallFactory(client).get_file_group_call()
        group_call.song_name = vid_title
        GPC[(message.chat.id, client.me.id)] = group_call
        try:
            await group_call.start(message.chat.id)
        except BaseException as e:
            return await u_s.edit(f"**Lah ngapa dah...:** `{e}`")
        group_call.add_handler(playout_ended_handler, GroupCallFileAction.PLAYOUT_ENDED)
        group_call.input_filename = raw_file_name
        return await u_s.edit(f"📀 Sedang memainkan `{vid_title}` di `{message.chat.title}`!")
    elif not group_call.is_connected:
        try:
            await group_call.start(message.chat.id)
        except BaseException as e:
            return await u_s.edit(f"**Ngapa yaa...:** `{e}`")
        group_call.add_handler(playout_ended_handler, GroupCallFileAction.PLAYOUT_ENDED)
        group_call.input_filename = raw_file_name
        group_call.song_name = vid_title
        return await u_s.edit(f"📀 Sedang memainkan `{vid_title}` di `{message.chat.title}`!")
    else:
        s_d = s_dict.get((message.chat.id, client.me.id))
        f_info = {"song_name": vid_title,
                  "raw": raw_file_name,
                  "singer": uploade_r,
                  "dur": dur,
                  "url": url
                 }
        if s_d:
            s_d.append(f_info)
        else:
            s_dict[(message.chat.id, client.me.id)] = [f_info]
        s_d = s_dict.get((message.chat.id, client.me.id))
        return await u_s.edit(f"✚ Ditambahkan 🎵 `{vid_title}` Di posisi `#{len(s_d)+1}`!")
    
@run_in_exc      
def convert_to_raw(audio_original, raw_file_name):
    ffmpeg.input(audio_original).output(raw_file_name, format="s16le", acodec="pcm_s16le", ac=2, ar="48k", loglevel="error").overwrite_output().run()
    return raw_file_name

def edit_msg(client, message, to_edit):
    try:
        client.loop.create_task(message.edit(to_edit))
    except MessageNotModified:
        pass
    except FloodWait as e:
        client.loop.create_task(asyncio.sleep(e.x))
    except TypeError:
        pass
    
def download_progress_hook(d, message, client, start):
    if d['status'] == 'downloading':
        current = d.get("_downloaded_bytes_str") or humanbytes(d.get("downloaded_bytes", 1))
        total = d.get("_total_bytes_str") or d.get("_total_bytes_estimate_str")
        file_name = d.get("filename")
        eta = d.get('_eta_str', "N/A")
        percent = d.get("_percent_str", "N/A")
        speed = d.get("_speed_str", "N/A")
        to_edit = f"<b><u>🖇 Mengunduh File</b></u> \n<b>🏷 Nama file :</b> <code>{file_name}</code> \n<b>🗂 Ukuran file :</b> <code>{total}</code> \n<b>⚡Speed :</b> <code>{speed}</code> \n<b>ETA :</b> <code>{eta}</code> \n<i>🕹️ Unduh {current} out of {total}</i> (__{percent}__)"
        threading.Thread(target=edit_msg, args=(client, message, to_edit)).start()

@run_in_exc
def yt_dl(url, client, message, start):
    opts = {
             "format": "bestaudio",
             "addmetadata": True,
             "key": "FFmpegMetadata",
             "prefer_ffmpeg": True,
             "geo_bypass": True,
             "progress_hooks": [lambda d: download_progress_hook(d, message, client, start)],
             "nocheckcertificate": True,
             "postprocessors": [
                 {
                     "key": "FFmpegExtractAudio",
                     "preferredcodec": "mp3"
                 }
             ],
             "outtmpl": "%(id)s.mp3",
             "quiet": True,
             "logtostderr": False,
         }
    with YoutubeDL(opts) as ytdl:
        ytdl_data = ytdl.extract_info(url, download=True)
    return str(ytdl_data['id']) + ".mp3"

RD_ = {}
FFMPEG_PROCESSES = {}
 
@gez.on_message(filters.command(["pause"], ".") & filters.me
)
async def no_song_play(client, message):
    group_call = GPC.get((message.chat.id, client.me.id))
    if not group_call:
        await edit_or_reply(message, "`Lah tau yaaaa`")
        return
    if not group_call.is_connected:
        await edit_or_reply(message, "`Lah tau yaaaa`")
        return    
    await edit_or_reply(message, f"`⏸ Dijeda {str(group_call.input_filename).replace('.raw', '')}.`")
    group_call.pause_playout()
    
    
@gez.on_message(filters.command(["resume"], ".") & filters.me
)
async def wow_dont_stop_songs(client, message):
    group_call = GPC.get((message.chat.id, client.me.id))
    if not group_call:
        await edit_or_reply(message, "`Lah tau yaaaa`")
        return    
    if not group_call.is_connected:
        await edit_or_reply(message, "`Lah tau yaaaa`")
        return    
    group_call.resume_playout()
    await edit_or_reply(message, f"`▶️ Dilanjutkan.`")
        

@gez.on_message(filters.command(["end"], ".") & filters.me
)
async def leave_vc_test(client, message):
    group_call = GPC.get((message.chat.id, client.me.id))
    if not group_call:
        await edit_or_reply(message, "`Lah tau yaaaa`")
        return
    if not group_call.is_connected:
        await edit_or_reply(message, "`Lah tau yaaaa`")
        return
    if os.path.exists(group_call.input_filename):
        os.remove(group_call.input_filename)
    await group_call.stop()
    await edit_or_reply(message, f"`❌ Turun dulu cuyyy : {message.chat.title} - Vc`")
    del GPC[(message.chat.id, client.me.id)]
    
add_command_help(
    "Musik",
    [
        [
            "play",
            "Play Musik & Video Dengan Judul Lagu",
        ],
        ["skip", "Skip Lagu."],
        ["pause", "Pause Musik."],
        ["resume", "Resume Musik."],
        ["end", "Stop Musik."],
        ["playlist", "Play Playlist Musik."],
    ],
)
