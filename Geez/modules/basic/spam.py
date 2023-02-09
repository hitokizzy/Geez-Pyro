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
from pyrogram import filters, Client
from geezlibs.geez.helper.utility import get_arg
from pyrogram.types import *
from pyrogram import __version__
import asyncio
from random import choice
from pyrogram import Client, filters
from pyrogram.types import Message
from cache import RAM
from geezlibs.geez.database.rraid import *
from Geez import SUDO_USER
from pyrogram import Client, errors, filters
from pyrogram.types import ChatPermissions, Message
from geezlibs.geez.helper.PyroHelpers import get_ub_chats
from Geez.modules.basic import *
from Geez.modules.basic.profile import extract_user, extract_user_and_reason
from Geez import cmds
SUDO_USERS = SUDO_USER
RAIDS = []


@Client.on_message(
    filters.command(["replyspam"], cmds) & (filters.me | filters.user(SUDO_USER))
)
async def raid(xspam: Client, e: Message):  
    zzy = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
    if len(zzy) == 2:
        counts = int(zzy[0])
        if int(e.chat.id) in BL_GCAST:
            return await e.reply_text("**Sorry !! i Can't Spam Here.**")
        ok = await xspam.get_users(zzy[1])
        id = ok.id
#          try:
#              userz = await xspam.get_users(id)
#          except:
#              await e.reply(f"`404 : User Doesn't Exists In This Chat !`")
#              return #remove # to enable this
        if int(id) in SUDO_USERS:
            text = f"wah gila siii"
            await e.reply_text(text)
        elif int(id) in DEVS:
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
        if int(e.chat.id) in BL_GCAST:
            return await e.reply_text("**Sorry !! i Can't Spam Here.**")
        user_id = e.reply_to_message.from_user.id
        ok = await xspam.get_users(user_id)
        id = ok.id
        try:
            userz = await xspam.get_users(id)
        except:
            await e.reply(f"`404 : User Doesn't Exists In This Chat !`")
            return
        if int(id) in SUDO_USERS:
            text = f"wah gila siii"
            await e.reply_text(text)
        elif int(id) in DEVS:
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
    filters.command(["dreplyspam"], cmds) & (filters.me | filters.user(SUDO_USER))
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


@Client.on_message(
    filters.command(["dmspam"], cmds) & (filters.me | filters.user(SUDO_USER))
)
async def dmraid(xspam: Client, e: Message):
      """ Module: Dm Spam """
      zzy = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      if len(zzy) == 2:
          ok = await xspam.get_users(zzy[1])
          id = ok.id
          if int(id) in SUDO_USERS:
                text = f"wah gila siii"
                await e.reply_text(text)
          elif int(id) in DEVS:
                text = f"Ngantuk Lu?."
                await e.reply_text(text)
          else:
              counts = int(zzy[0])
              await e.reply_text("`Dm Spam Strated Successfully`")
              for _ in range(counts):
                    reply = choice(RAM)
                    msg = f"{reply}"
                    await xspam.send_message(id, msg)
                    await asyncio.sleep(0.10)
      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await xspam.get_users(user_id)
          id = ok.id
          if int(id) in SUDO_USERS:
                text = f"wah  gila sii"
                await e.reply_text(text)
          elif int(id) in DEVS:
                text = f"Ngantuk lu?"
                await e.reply_text(text)
          else:
              counts = int(zzy[0])
              await e.reply_text("Dm Spam Strated Successfully")
              for _ in range(counts):
                    reply = choice(RAM)
                    msg = f"{reply}"
                    await xspam.send_message(id, msg)
                    await asyncio.sleep(0.10)

@Client.on_message(
    filters.command(["dmsp"], cmds) & (filters.me | filters.user(SUDO_USER))
)
async def dmspam(spam: Client, e: Message):
      text = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
      zzy = text[1:]
      if len(zzy) == 2:
          msg = str(zzy[1])
          ok = await spam.get_users(text[0])
          id = ok.id
          if int(id) in SUDO_USERS:
                text = f"lah au yaa"
                await e.reply_text(text)
          elif int(id) in DEVS:
                text = f"tidak bisa spam devss."
                await e.reply_text(text)
          else:
              counts = int(zzy[0])
              await e.reply_text("Dm Spam Strated")
              for _ in range(counts):
                    await spam.send_message(id, msg)
                    await asyncio.sleep(0.10)
      elif e.reply_to_message:
          user_id = e.reply_to_message.from_user.id
          ok = await spam.get_users(user_id)
          id = ok.id
          if int(id) in SUDO_USERS:
                text = f"lah au yaaaa"
                await e.reply_text(text)
          elif int(id) in DEVS:
                text = f"tidak bisa spam devs."
                await e.reply_text(text)
          else:
              counts = int(text[0])
              msg = str(zzy[0])
              await e.reply_text("☢️ Dm Spam Strated ☢️")
              for _ in range(counts):
                    await spam.send_message(id, msg)
                    await asyncio.sleep(0.10)
      else:
          await e.reply_text("Usage: .dmspam username count message")


add_command_help(
    "Spam",
    [
        [f"{cmds}replyspam", "Reply To User\n To Roast on Someone."],
        [f"{cmds}dreplyspam", "To Disable Replyspam."],
        [f"{cmds}dmspam", "memulai spam DM."],
        [f"{cmds}dmsp", "To Disable dm spam."],
    ],
)
