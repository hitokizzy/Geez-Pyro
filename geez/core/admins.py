from config import config


async def is_sudo(message):
    if message.from_user and message.from_user.id in config.SUDO_USERS:
        return True
    else:
        return False


async def is_admin(message):
    if message.from_user and (
        message.from_user.id
        in [
            admin.user.id
            for admin in (await message.chat.get_members(filter="administrators"))
        ]
    ):
        return True
    elif message.from_user and message.from_user.id in config.SUDO_USERS:
        return True
    elif message.sender_chat and message.sender_chat.id == message.chat.id:
        return True
    else:
        return False
