import asyncio
from pyrogram import filters, Client
from geez.modules.help import *
from geez.helper.utility import get_arg
from pyrogram.types import *
from pyrogram import __version__
import os
import sys
import asyncio
import re
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from cache.data import *
from geez.database.mongodb.rraid import *
from geez import SUDO_USER
from pyrogram import Client, errors, filters
from pyrogram.types import ChatPermissions, Message
from geez.helper.PyroHelpers import get_ub_chats
from geez.helper.dev import *
from geez.modules.basic.profile import extract_user, extract_user_and_reason
SUDO_USERS = SUDO_USER
RAIDS = []


@Client.on_message(
    filters.command(["replyspam"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def raid(xspam: Client, e: Message):  
      zzy = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(zzy) == 2:
          counts = int(zzy[0])
          if int(e.chat.id) in GROUP:
               return await e.reply_text("**Sorry !! i Can't Spam Here.**")
          ok = await xspam.get_users(zzy[1])
          id = ok.id
#          try:
#              userz = await xspam.get_users(id)
#          except:
#              await e.reply(f"`404 : User Doesn't Exists In This Chat !`")
#              return #remove # to enable this
          if int(id) in VERIFIED_USERS:
                text = f"wah gila siii"
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"tidak bisa devs."
                await e.reply_text(text)
          else:
              fname = ok.first_name
              mention = f"[{fname}](tg://user?id={id})"
              for _ in range(counts):
                    reply = choice(RAM)
                    msg = f"{mention} {reply}"
                    await xspam.send_message(e.chat.id, msg)
                    await asyncio.sleep(0.10)
      elif e.reply_to_message:
          msg_id = e.reply_to_message.from_user.id
          counts = int(zzy[0])
          if int(e.chat.id) in GROUP:
               return await e.reply_text("**Sorry !! i Can't Spam Here.**")
          user_id = e.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          id = ok.id
          try:
              userz = await xspam.get_users(id)
          except:
              await e.reply(f"`404 : User Doesn't Exists In This Chat !`")
              return
          if int(id) in VERIFIED_USERS:
                text = f"wah gila siii"
                await e.reply_text(text)
          elif int(id) in SUDO_USERS:
                text = f"tidak bisa devs."
                await e.reply_text(text)
          else:
              fname = ok.first_name
              mention = f"[{fname}](tg://user?id={id})"
              for _ in range(counts):
                    reply = choice(RAM)
                    msg = f"{mention} {reply}"
                    await xspam.send_message(e.chat.id, msg)
                    await asyncio.sleep(0.10)
      else:
          await e.reply_text("Usage: .raid count username")


@Client.on_message(
    filters.command(["dreplyspam"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def gmute_user(client: Client, message: Message):
    args = await extract_user(message)
    reply = message.reply_to_message
    ex = await message.edit_text("`Processing...`")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            await ex.edit(f"`Please specify a valid user!`")
            return
    elif reply:
        user_id = reply.from_user.id
        user = await client.get_users(user_id)
    else:
        await ex.edit(f"`Please specify a valid user!`")
        return
    try:
        if user.id not in (await get_rraid_users()):
           await ex.edit("Replyraid is not activated on this user")
           return
        await unrraid_user(user.id)
        RAIDS.remove(user.id)
        await ex.edit(f"[{user.first_name}](tg://user?id={user.id}) DeActivated ReplyRaid!")
    except Exception as e:
        await ex.edit(f"**ERROR:** `{e}`")
        return


add_command_help(
    "replyspam",
    [
        [".replyspam", "Reply To User\n To Roast on Someone."],
        [".dreplyspam", "To Disable Replyspam."],
    ],
)
