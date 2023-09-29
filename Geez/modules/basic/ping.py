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
import time
import random
import speedtest
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.raw.functions import Ping
from datetime import datetime
from geezlibs import DEVS
from geezlibs.geez import geez, devs
from geezlibs.geez.helper import SpeedConvert
from Geez import StartTime, SUDO_USER
from Geez import app, cmds, START_TIME
from Geez.modules.bot.inline import get_readable_time
from Geez.modules.basic import add_command_help
from config import ALIVE_PIC

TIME_DURATION_UNITS = (
    ("w", 60 * 60 * 24 * 7),
    ("d", 60 * 60 * 24),
    ("h", 60 * 60),
    ("m", 60),
    ("s", 1),
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append(f'{amount}{unit}{"" if amount == 1 else ""}')
    return ":".join(parts)

class WWW:
    SpeedTest = (
        "Speedtest started at `{start}`\n"
        "Ping ➠ `{ping}` ms\n"
        "Download ➠ `{download}`\n"
        "Upload ➠ `{upload}`\n"
        "ISP ➠ __{isp}__"
    )

    NearestDC = "Country: `{}`\n" "Nearest Datacenter: `{}`\n" "This Datacenter: `{}`"

@geez("speedtest", cmds)
async def speed_test(client: Client, message: Message):
    new_msg = await message.reply_text("`Running speed test . . .`")
    try:
       await message.delete()
    except:
       pass
    spd = speedtest.Speedtest()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "`Getting best server based on ping . . .`"
    )
    spd.get_best_server()

    new_msg = await new_msg.edit(f"`{new_msg.text}`\n" "`Testing download speed . . .`")
    spd.download()

    new_msg = await new_msg.edit(f"`{new_msg.text}`\n" "`Testing upload speed . . .`")
    spd.upload()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "`Getting results and preparing formatting . . .`"
    )
    results = spd.results.dict()

    await new_msg.edit(
        WWW.SpeedTest.format(
            start=results["timestamp"],
            ping=results["ping"],
            download=SpeedConvert(results["download"]),
            upload=SpeedConvert(results["upload"]),
            isp=results["client"]["isp"],
        )
    )

kopi = [
    "**Hadir Bang** 😁",
    "**Mmuaahh** 😉",
    "**Hadir dong** 😁",
    "**Hadir ganteng** 🥵",
    "**Hadir bro** 😎",
    "**Hadir kak maap telat** 🥺",
]

@devs("absen")
async def absen(client: Client, message: Message):
    await message.reply_text(random.choice(kopi))


@Client.on_message(filters.command("gping", "*") & filters.user(DEVS))
async def cpingme(client: Client, message: Message):
    """Ping the assistant"""
    mulai = time.time()
    gez = await message.reply_text("...")
    akhir = time.time()
    await gez.edit_text(f"**🏓 Pong!**\n`{round((akhir - mulai) * 1000)}ms`")


@geez("pink", cmds)
async def pingme(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await message.reply_text("**Pinging.**")
    end = datetime.now()
    await asyncio.sleep(1)
    try:
       await message.delete()
    except:
       pass
    duration = (end - start).microseconds / 1000
    await xx.edit("**Pinging..**")
    await xx.edit("**Pinging...**")
    await xx.edit("**Pinging....**")
    await asyncio.sleep(1)
    await xx.edit(f"**Geez - Pyro!!🎈**\n**Pinger** : %sms\n**Bot Uptime** : {uptime}🕛" % (duration))

@Client.on_message(filters.command("ping", "!") & SUDO_USER)
@geez("ping", cmds)
async def pings(client, message):
    start = time.time()
    current_time = datetime.now()
    await client.invoke(Ping(ping_id=random.randint(0, 2147483647)))
    delta_ping = round((time.time() - start) * 1000, 3)
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    _ping = f"""
    <b>Geez - Pyro!!🎈</b>
    <i> Ping:</i> `{delta_ping} ms`
    <i> Uptime:</i> `{uptime}`
    """
    await message.reply(_ping)

@geez("ppink", cmds)
async def ppingme(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await message.reply_text("**0% ▒▒▒▒▒▒▒▒▒▒**")
    try:
       await message.delete()
    except:
       pass
    await xx.edit("**20% ██▒▒▒▒▒▒▒▒**")
    await xx.edit("**40% ████▒▒▒▒▒▒**")
    await xx.edit("**60% ██████▒▒▒▒**")
    await xx.edit("**80% ████████▒▒**")
    await xx.edit("**100% ██████████**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xx.edit(
        f"❏ **𝗣𝗢𝗡𝗚**\n"
        f"├•  - `%sms`\n"
        f"├•  `{uptime}` \n"
        f"└•  {client.me.mention}" % (duration)
    )


add_command_help(
    "ping",
    [
        [f"{cmds}ping", "Check bot alive or not."],
        [f"{cmds}pping", "Check bot alive or not."],
    ],
)
add_command_help(
    "alive",
    [
        [f"{cmds}alive", "Check bot alive or not."],
        [f"{cmds}geez", "Check bot alive or not."],
    ],
)
