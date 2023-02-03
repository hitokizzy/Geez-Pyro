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
from collections import deque
from random import randint

from pyrogram import filters, Client
from pyrogram.types import Message
from Geez import cmds

from Geez.modules.basic import add_command_help

emojis = {
    "moon": list("🌗🌘🌑🌒🌓🌔🌕🌖"),
    "clock": list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"),
    "thunder": list("☀️🌤️⛅🌥️☁️🌩️🌧️⛈️⚡🌩️🌧️🌦️🌥️⛅🌤️☀️"),
    "earth": list("🌏🌍🌎🌎🌍🌏🌍🌎"),
    "heart": list("❤️🧡💛💚💙💜🖤"),
}
emoji_commands = [x for x in emojis]


@Client.on_message(filters.command(emoji_commands, cmds) & filters.me)
async def emoji_cycle(bot: Client, message: Message):
    deq = deque(emojis[message.command[0]])
    try:
        for _ in range(randint(16, 32)):
            await asyncio.sleep(0.3)
            await message.edit("".join(deq), parse_mode=None)
            deq.rotate(1)
    except Exception:
        await message.delete()


special_emojis_dict = {
    "target": {"emoji": "🎯", "help": "The special target emoji"},
    "dice": {"emoji": "🎲", "help": "The special dice emoji"},
    "bb": {"emoji": "🏀", "help": "The special basketball emoji"},
    "soccer": {"emoji": "⚽️", "help": "The special football emoji"},
}
special_emoji_commands = [x for x in special_emojis_dict]


@Client.on_message(filters.command(special_emoji_commands, cmds) & filters.me)
async def special_emojis(bot: Client, message: Message):
    emoji = special_emojis_dict[message.command[0]]
    await message.delete()
    await bot.send_dice(message.chat.id, emoji["emoji"])


# Command help section
special_emoji_help = [
    [f"{cmds}moon", "Cycles all the phases of the moon emojis."],
    [f"{cmds}clock", "Cycles all the phases of the clock emojis."],
    [f"{cmds}thunder", "Cycles thunder."],
    [f"{cmds}heart", "Cycles heart emojis."],
    [f"{cmds}earth `or` {cmds}globe", "Make the world go round."],
]

for x in special_emojis_dict:
    special_emoji_help.append([f"{cmds}{x}", special_emojis_dict[x]["help"]])

add_command_help("emoji", special_emoji_help)
