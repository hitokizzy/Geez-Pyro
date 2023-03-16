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
import pytz
from asyncio import sleep
from glob import iglob
from random import randint
from urllib.parse import urlparse
import aiofiles
from github import Github
from pyrogram import filters, Client
from pyrogram.types import Message
from reportlab.graphics import renderPM
from svglib.svglib import svg2rlg
from geezlibs.geez import geez
from geezlibs.geez.helper.PyroHelpers import ReplyCheck
from geezlibs.geez.helper.aiohttp_helper import AioHttp
from Geez.modules.basic import add_command_help
from Geez import cmds

@geez("ggraph", cmds)
async def commit_graph(bot: Client, message: Message):
    if len(message.command) < 2:
        await message.edit(
            "Please provide a github profile username to generate the graph!"
        )
        await sleep(2)
        await message.delete()
        return
    else:
        git_user = message.command[1]

    url = f"https://ghchart.rshah.org/{git_user}"
    file_name = f"{randint(1, 999)}{git_user}"

    resp = await AioHttp.get_raw(url)
    f = await aiofiles.open(f"{file_name}.svg", mode="wb")
    await f.write(resp)
    await f.close()

    try:
        drawing = svg2rlg(f"{file_name}.svg")
        renderPM.drawToFile(drawing, f"{file_name}.png")
    except UnboundLocalError:
        await message.edit("Username does not exist!")
        await sleep(2)
        await message.delete()
        #return

    try:
        await asyncio.gather(
        bot.send_photo(
            chat_id=message.chat.id,
            photo=f"{file_name}.png",
            caption=git_user,
            reply_to_message_id=ReplyCheck(message),
        ),
        message.delete(),
    )
    except Exception as e:
        print(f"An error occurred: {e}")

    for file in iglob(f"{file_name}.*"):
        os.remove(file)

@Client.on_message(filters.command("github", cmds) & filters.me)
async def github_command_handler(client, message):
    if len(message.text.split()) != 2:
        await message.edit("Please provide a valid GitHub repository URL.")
        return
    g = Github()
    url = message.text.split()[1]
    parsed_url = urlparse(url)

    if not parsed_url.scheme or not parsed_url.netloc or not parsed_url.path:
        await message.edit("Invalid URL format. Please provide a valid GitHub repository URL.")
        return

    owner_username, repo_name = parsed_url.path.strip('/').split("/")[-2:]

    try:
        repo = g.get_repo(f"{owner_username}/{repo_name}")

        created_at = repo.created_at.astimezone(pytz.timezone("UTC"))
        forks_count = repo.forks_count
        stars_count = repo.stargazers_count

        contributors = []
        commits = repo.get_commits()
        for commit in commits:
            if commit.author is not None:
                contributor = commit.author.login
                if contributor not in contributors:
                    contributors.append(contributor)
        message_text = f"**REPO** : {repo_name}\n\n"
        message_text += f"📅 Created on: {created_at}\n"
        message_text += f"🍴 Forks: {forks_count}\n"
        message_text += f"⭐ Stars: {stars_count}\n"
        message_text += "👥 Contributors:\n"
        for contributor in contributors:
            message_text += f"   - {contributor}\n"

        await message.edit(text=message_text)
    except Exception as e:
        await message.edit(f"Error occurred: {e}")

add_command_help(
    "git",
    [
        [f"{cmds}ggraph | {cmds}commitgraph", "Gets the commit graph for a Github user."],
        [f"{cmds}github <url github>", "mengambil info repo github."],
    ],
)
