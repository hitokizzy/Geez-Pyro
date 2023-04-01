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
import os
import openai
from pyrogram.errors import MessageNotModified
from geezlibs.geez import geez
from Geez import cmds
from config import OPENAI_API
from geezlibs.geez.helper.what import *
from Geez.modules.basic import add_command_help

class OpenAi:
    def Text(question):
        openai.api_key = os.getenv("OPENAI_API")
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Q: {question}\nA:",
            temperature=0,
            max_tokens=500,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
        return response.choices[0].text

    def Photo(question):
        openai.api_key = os.getenv("OPENAI_API")
        response = openai.Image.create(prompt=question, n=1, size="1024x1024")
        return response["data"][0]["url"]

@geez("ask", cmds)
async def open_ai(c, m):
    if len(m.command) == 1:
        return await m.reply(f"Ketik <code>{cmds}{m.command[0]} [question]</code> Pertanya untuk menggunakan OpenAI")
    question = m.text.split(" ", maxsplit=1)[1]
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API}",
    }

    json_data = {
        "model": "text-davinci-003",
        "prompt": question,
        "max_tokens": 200,
        "temperature": 0,
    }
    msg = await m.reply("`Processing..")
    try:
        response = (await http.post("https://api.openai.com/v1/completions", headers=headers, json=json_data)).json()
        await msg.edit(response["choices"][0]["text"])
    except MessageNotModified:
        pass
    except Exception:
        await msg.edit("**AI tidak merespon...**")



@geez("ai", cmds)
async def open_ai_img(client, message):
    p_message = await message.reply("<code>Memproses...</code>")
    if len(message.command) < 2:
        return await p_message.edit(f"<b><code>{message.text}</code> [query]</b>")
    try:
        response = OpenAi.Photo(message.text.split(None, 1)[1])
        msg = message.reply_to_message or message
        await client.send_photo(message.chat.id, response, reply_to_message_id=msg.id)
        return await p_message.delete()
    except Exception as error:
        await message.reply(error)
        return await p_message.delete()

add_command_help(
    "openAI",
    [
        [f"{cmds}ask [question]", "to ask questions using the OpenAI."],
        [f"{cmds}ai [query]", "to generate image using OpenAI."],
    ],
)
