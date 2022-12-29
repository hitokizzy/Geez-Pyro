import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "geez"])

async def join(client):
    try:
        await client.join_chat("GeezSupport")
        await client.join_chat("ramsupportt")
    except BaseException:
        pass
