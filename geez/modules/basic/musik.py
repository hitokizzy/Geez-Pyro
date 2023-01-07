import os
import json
import shutil
from config import config
from geez.core.song import Song
from pyrogram.types import Message
from pytgcalls.types import Update
from pyrogram import enums, filters
from pyrogram import Client as gez
from pyrogram import Client
from pytgcalls.exceptions import GroupCallNotFound, NoActiveGroupCall
from pytgcalls.types.stream import StreamAudioEnded, StreamVideoEnded
from geez.core.decorators import *
from geez.core import *



if config.BOT_TOKEN:
    bot = Client(
        "Geez-Pyro",
        api_id=config.API_ID,
        api_hash=config.API_HASH,
        bot_token=config.BOT_TOKEN,
    )
    client = bot
else:
    client = app


@gez.on_message(
    filters.command(["p", "play"], config.PREFIXES) & ~filters.private & ~filters.edited
)
async def play_stream(_, message: Message, lang):
    chat_id = message.chat.id
    group = get_group(chat_id)
    if group["admins_only"]:
        check = await is_admin(message)
        if not check:
            k = await message.reply_text(lang["notAllowed"])
            return await delete_messages([message, k])
    song = await search(message)
    if song is None:
        k = await message.reply_text(lang["notFound"])
        return await delete_messages([message, k])
    ok, status = await song.parse()
    if not ok:
        raise Exception(status)
    if not group["is_playing"]:
        set_group(chat_id, is_playing=True, now_playing=song)
        await start_stream(song, lang)
        await delete_messages([message])
    else:
        queue = get_queue(chat_id)
        await queue.put(song)
        k = await message.reply_text(
            lang["addedToQueue"] % (song.title, song.source, len(queue)),
            disable_web_page_preview=True,
        )
        await delete_messages([message, k])


@gez.on_message(
    filters.command(["sk", "skip"], config.PREFIXES)
    & ~filters.private
    & ~filters.edited
)
async def skip_track(_, message: Message, lang):
    chat_id = message.chat.id
    group = get_group(chat_id)
    if group["loop"]:
        await skip_stream(group["now_playing"], lang)
    else:
        queue = get_queue(chat_id)
        if len(queue) > 0:
            next_song = await queue.get()
            if not next_song.parsed:
                ok, status = await next_song.parse()
                if not ok:
                    raise Exception(status)
            set_group(chat_id, now_playing=next_song)
            await skip_stream(next_song, lang)
            await delete_messages([message])
        else:
            set_group(chat_id, is_playing=False, now_playing=None)
            await set_title(message, "")
            try:
                await pytgcalls.leave_group_call(chat_id)
                k = await message.reply_text(lang["queueEmpty"])
            except (NoActiveGroupCall, GroupCallNotFound):
                k = await message.reply_text(lang["notActive"])
            await delete_messages([message, k])


@gez.on_message(
    filters.command(["m", "mute"], config.PREFIXES) & ~filters.private & ~filters.edited
)
async def mute_vc(_, message: Message, lang):
    chat_id = message.chat.id
    try:
        await pytgcalls.mute_stream(chat_id)
        k = await message.reply_text(lang["muted"])
    except (NoActiveGroupCall, GroupCallNotFound):
        k = await message.reply_text(lang["notActive"])
    await delete_messages([message, k])


@gez.on_message(
    filters.command(["um", "unmute"], config.PREFIXES)
    & ~filters.private
    & ~filters.edited
)
async def unmute_vc(_, message: Message, lang):
    chat_id = message.chat.id
    try:
        await pytgcalls.unmute_stream(chat_id)
        k = await message.reply_text(lang["unmuted"])
    except (NoActiveGroupCall, GroupCallNotFound):
        k = await message.reply_text(lang["notActive"])
    await delete_messages([message, k])


@gez.on_message(
    filters.command(["ps", "pause"], config.PREFIXES)
    & ~filters.private
    & ~filters.edited
)
async def pause_vc(_, message: Message, lang):
    chat_id = message.chat.id
    try:
        await pytgcalls.pause_stream(chat_id)
        k = await message.reply_text(lang["paused"])
    except (NoActiveGroupCall, GroupCallNotFound):
        k = await message.reply_text(lang["notActive"])
    await delete_messages([message, k])


@gez.on_message(
    filters.command(["rs", "resume"], config.PREFIXES)
    & ~filters.private
    & ~filters.edited
)
async def resume_vc(_, message: Message, lang):
    chat_id = message.chat.id
    try:
        await pytgcalls.resume_stream(chat_id)
        k = await message.reply_text(lang["resumed"])
    except (NoActiveGroupCall, GroupCallNotFound):
        k = await message.reply_text(lang["notActive"])
    await delete_messages([message, k])


@gez.on_message(
    filters.command(["end", "stop"], config.PREFIXES)
    & ~filters.private
    & ~filters.edited
)
async def leave_vc(_, message: Message, lang):
    chat_id = message.chat.id
    set_group(chat_id, is_playing=False, now_playing=None)
    await set_title(message, "")
    clear_queue(chat_id)
    try:
        await pytgcalls.leave_group_call(chat_id)
        k = await message.reply_text(lang["leaveVC"])
    except (NoActiveGroupCall, GroupCallNotFound):
        k = await message.reply_text(lang["notActive"])
    await delete_messages([message, k])


@gez.on_message(
    filters.command(["list", "queue"], config.PREFIXES)
    & ~filters.private
    & ~filters.edited
)
async def queue_list(_, message: Message, lang):
    chat_id = message.chat.id
    queue = get_queue(chat_id)
    if len(queue) > 0:
        k = await message.reply_text(str(queue), disable_web_page_preview=True)
    else:
        k = await message.reply_text(lang["queueEmpty"])
    await delete_messages([message, k])
    

@gez.on_message(
    filters.command(["mode", "switch"], config.PREFIXES)
    & ~filters.private
    & ~filters.edited
)
async def switch_mode(_, message: Message, lang):
    chat_id = message.chat.id
    group = get_group(chat_id)
    if group["stream_mode"] == "audio":
        set_group(chat_id, stream_mode="video")
        k = await message.reply_text(lang["videoMode"])
    else:
        set_group(chat_id, stream_mode="audio")
        k = await message.reply_text(lang["audioMode"])
    await delete_messages([message, k])


@gez.on_message(
    filters.command(["admins", "adminsonly"], config.PREFIXES)
    & ~filters.private
    & ~filters.edited
)
async def admins_only(_, message: Message, lang):
    chat_id = message.chat.id
    group = get_group(chat_id)
    if group["admins_only"]:
        set_group(chat_id, admins_only=False)
        k = await message.reply_text(lang["adminsOnly"] % "Disabled")
    else:
        set_group(chat_id, admins_only=True)
        k = await message.reply_text(lang["adminsOnly"] % "Enabled")
    await delete_messages([message, k])


@gez.on_message(
    filters.command(["pl", "playlist"], config.PREFIXES)
    & ~filters.private
    & ~filters.edited
)
async def import_playlist(_, message: Message, lang):
    chat_id = message.chat.id
    group = get_group(chat_id)
    if group["admins_only"]:
        check = await is_admin(message)
        if not check:
            k = await message.reply_text(lang["notAllowed"])
            return await delete_messages([message, k])
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:
        text = extract_args(message.text)
    if text == "":
        k = await message.reply_text(lang["notFound"])
        return await delete_messages([message, k])
    if "youtube.com/playlist?list=" in text:
        try:
            temp_queue = get_youtube_playlist(text, message)
        except BaseException:
            k = await message.reply_text(lang["notFound"])
            return await delete_messages([message, k])
    elif "open.spotify.com/playlist/" in text:
        if not config.SPOTIFY:
            k = await message.reply_text(lang["spotifyNotEnabled"])
            return await delete_messages([message, k])
        try:
            temp_queue = get_spotify_playlist(text, message)
        except BaseException:
            k = await message.reply_text(lang["notFound"])
            return await delete_messages([message, k])
    else:
        k = await message.reply_text(lang["invalidFile"])
        return await delete_messages([message, k])
    queue = get_queue(chat_id)
    if not group["is_playing"]:
        song = await temp_queue.__anext__()
        set_group(chat_id, is_playing=True, now_playing=song)
        ok, status = await song.parse()
        if not ok:
            raise Exception(status)
        await start_stream(song, lang)
        async for _song in temp_queue:
            await queue.put(_song)
        queue.get_nowait()
    else:
        async for _song in temp_queue:
            await queue.put(_song)
    k = await message.reply_text(lang["queueImported"] % len(group["queue"]))
    await delete_messages([message, k])


@pytgcalls.on_stream_end()
async def stream_end(_, update: Update, lang):
    if isinstance(update, StreamAudioEnded) or isinstance(update, StreamVideoEnded):
        chat_id = update.chat_id
        group = get_group(chat_id)
        if group["loop"]:
            await skip_stream(group["now_playing"], lang)
        else:
            queue = get_queue(chat_id)
            if len(queue) > 0:
                next_song = await queue.get()
                if not next_song.parsed:
                    ok, status = await next_song.parse()
                    if not ok:
                        raise Exception(status)
                set_group(chat_id, now_playing=next_song)
                await skip_stream(next_song, lang)
            else:
                if safone.get(chat_id) is not None:
                    try:
                        await safone[chat_id].delete()
                    except BaseException:
                        pass
                await set_title(chat_id, "", client=app)
                set_group(chat_id, is_playing=False, now_playing=None)
                await pytgcalls.leave_group_call(chat_id)


@pytgcalls.on_closed_voice_chat()
async def closed_vc(_, chat_id: int):
    if chat_id not in all_groups():
        if safone.get(chat_id) is not None:
            try:
                await safone[chat_id].delete()
            except BaseException:
                pass
        await set_title(chat_id, "", client=app)
        set_group(chat_id, now_playing=None, is_playing=False)
        clear_queue(chat_id)


@pytgcalls.on_kicked()
async def kicked_vc(_, chat_id: int):
    if chat_id not in all_groups():
        if safone.get(chat_id) is not None:
            try:
                await safone[chat_id].delete()
            except BaseException:
                pass
        await set_title(chat_id, "", client=app)
        set_group(chat_id, now_playing=None, is_playing=False)
        clear_queue(chat_id)


@pytgcalls.on_left()
async def left_vc(_, chat_id: int):
    if chat_id not in all_groups():
        if safone.get(chat_id) is not None:
            try:
                await safone[chat_id].delete()
            except BaseException:
                pass
        await set_title(chat_id, "", client=app)
        set_group(chat_id, now_playing=None, is_playing=False)
        clear_queue(chat_id)


client.start()
pytgcalls.run()



add_command_help(
    "Musik",
    [
        [
            "play | p <judul lagu>",
            "Play Musik Dengan Judul Lagu",
        ],
        ["skip | sk", "Skip Lagu."],
        ["pause | ps", "Pause Musik."],
        ["stop | end", "Stop Musik."],
        ["mute | mt", "Mute Musik."],
        ["unmute | um", "Unmute Musik."],
        ["list | queu", "Playlist Musik."],
        ["playlist | pl", "Play Playlist Musik."],
    ],
)
