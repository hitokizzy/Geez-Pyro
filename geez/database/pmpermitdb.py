from geez.database import cli
import asyncio

collection = cli["geez"]["pmpermit"]

PMPERMIT_MESSAGE = (
    "**Hai,\n\n**"
    "**Ini adalah pesan otomatis dari Geez Pyro Userbot.\n**"
    "**Mohon untuk tidak melakukan SPAM!.\n\n**"
    "**𝘒𝘢𝘳𝘦𝘯𝘢 𝘚𝘢𝘺𝘢 𝘈𝘬𝘢𝘯 𝘖𝘵𝘰𝘮𝘢𝘵𝘪𝘴 𝘔𝘦𝘮𝘣𝘭𝘰𝘬𝘪𝘳 𝘈𝘯𝘥𝘢, \n 𝘛𝘶𝘯𝘨𝘨𝘶 𝘚𝘢𝘮𝘱𝘢𝘪 𝘗𝘦𝘮𝘪𝘭𝘪𝘬 𝘚𝘢𝘺𝘢 𝘔𝘦𝘯𝘦𝘳𝘪𝘮𝘢 𝘗𝘦𝘴𝘢𝘯 𝘈𝘯𝘥𝘢,\n 𝘛𝘦𝘳𝘪𝘮𝘢𝘬𝘢𝘴𝘪𝘩.!\n**"
    "Geez Pyro Userbot"
)

BLOCKED = "**Spammer Terdeteksi, Blocked!**"

LIMIT = 5


async def set_pm(value: bool):
    doc = {"_id": 1, "pmpermit": value}
    doc2 = {"_id": "Approved", "users": []}
    r = await collection.find_one({"_id": 1})
    r2 = await collection.find_one({"_id": "Approved"})
    if r:
        await collection.update_one({"_id": 1}, {"$set": {"pmpermit": value}})
    else:
        await collection.insert_one(doc)
    if not r2:
        await collection.insert_one(doc2)


async def set_permit_message(text):
    await collection.update_one({"_id": 1}, {"$set": {"pmpermit_message": text}})


async def set_block_message(text):
    await collection.update_one({"_id": 1}, {"$set": {"block_message": text}})


async def set_limit(limit):
    await collection.update_one({"_id": 1}, {"$set": {"limit": limit}})


async def get_pm_settings():
    result = await collection.find_one({"_id": 1})
    if not result:
        return False
    pmpermit = result["pmpermit"]
    pm_message = result.get("pmpermit_message", PMPERMIT_MESSAGE)
    block_message = result.get("block_message", BLOCKED)
    limit = result.get("limit", LIMIT)
    return pmpermit, pm_message, limit, block_message


async def allow_user(chat):
    doc = {"_id": "Approved", "users": [chat]}
    r = await collection.find_one({"_id": "Approved"})
    if r:
        await collection.update_one({"_id": "Approved"}, {"$push": {"users": chat}})
    else:
        await collection.insert_one(doc)


async def get_approved_users():
    results = await collection.find_one({"_id": "Approved"})
    if results:
        return results["users"]
    else:
        return []


async def deny_user(chat):
    await collection.update_one({"_id": "Approved"}, {"$pull": {"users": chat}})


async def pm_guard():
    result = await collection.find_one({"_id": 1})
    if not result:
        return False
    if not result["pmpermit"]:
        return False
    else:
        return True
