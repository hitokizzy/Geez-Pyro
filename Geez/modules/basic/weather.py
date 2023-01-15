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
import aiohttp
from html import escape
from pyrogram import filters, Client 
from pyrogram.types import Message
from Geez.modules.basic import add_command_help
from pyrogram import enums

@Client.on_message(filters.command(["weather", "w"], ".") & filters.me)
async def get_weather(bot: Client, message: Message):
    if len(message.command) == 1:
        await message.edit("Usage: `.weather Maldives`")
        await asyncio.sleep(3)
        await message.delete()

    if len(message.command) > 1:
        location = message.command[1]
        headers = {"user-agent": "httpie"}
        url = f"https://wttr.in/{location}?mnTC0&lang=en"
        try:
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.get(url) as resp:
                    data = await resp.text()
        except Exception:
            await message.edit("Failed to get the weather forecast")

        if "we processed more than 1M requests today" in data:
            await message.edit("`Sorry, we cannot process this request today!`")
        else:
            weather = f"<code>{escape(data.replace('report', 'Report'))}</code>"
            await message.edit(weather, parse_mode=enums.ParseMode.MARKDOWN)


add_command_help(
    "weather",
    [
        [".weather", "Gets weather information for provided location."],
    ],
)
