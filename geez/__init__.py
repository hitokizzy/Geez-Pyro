from pyrogram import Client
from config import API_ID, API_HASH, SUDO_USERS, OWNER_ID, BOT_TOKEN, STRING_SESSION1, STRING_SESSION2, STRING_SESSION3, STRING_SESSION4, STRING_SESSION5, STRING_SESSION6, STRING_SESSION7, STRING_SESSION8, STRING_SESSION9, STRING_SESSION10
from datetime import datetime
import time
from aiohttp import ClientSession

StartTime = time.time()
START_TIME = datetime.now()
CMD_HELP = {}
SUDO_USER = SUDO_USERS
clients = []
ids = []

SUDO_USERS.append(OWNER_ID)
aiosession = ClientSession()

if not API_ID:
   print("WARNING: API ID TIDAK DITEMUKAN")

if not API_HASH:
   print("WARNING: API HASH TIDAK DITEMUKAN")   

if not BOT_TOKEN:
   print("WARNING: BOT TOKEN TIDAK DITEMUKAN")   

app = Client(
    name="app",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="geez/modules/bot"),
    in_memory=True,
)

if STRING_SESSION1:
   print("Client1: Starting..")
   client1 = Client(name="geez1", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION1, plugins=dict(root="geez/modules"))
   clients.append(client1)

if STRING_SESSION2:
   print("Client2: Starting.. ")
   client2 = Client(name="geez2", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION2, plugins=dict(root="geez/modules"))
   clients.append(client2)

if STRING_SESSION3:
   print("Client3: Starting.. ")
   client3 = Client(name="geez3", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION3, plugins=dict(root="geez/modules"))
   clients.append(client3)

if STRING_SESSION4:
   print("Client4: Starting.. ")
   client4 = Client(name="geez4", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION4, plugins=dict(root="geez/modules"))
   clients.append(client4)

if STRING_SESSION5:
   print("Client5: Starting.. ")
   client5 = Client(name="geez5", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION5, plugins=dict(root="geez/modules"))
   clients.append(client5)

if STRING_SESSION6:
   print("Client6: Starting.. ")
   client6 = Client(name="geez6", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION6, plugins=dict(root="geez/modules"))
   clients.append(client6)

if STRING_SESSION7:
   print("Client7: Starting.. ")
   client7 = Client(name="geez7", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION7, plugins=dict(root="geez/modules"))
   clients.append(client7)

if STRING_SESSION8:
   print("Client8: Starting.. ")
   client8 = Client(name="geez8", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION8, plugins=dict(root="geez/modules"))
   clients.append(client8)

if STRING_SESSION9:
   print("Client9: Starting.. ")
   client9 = Client(name="geez9", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION9, plugins=dict(root="geez/modules"))
   clients.append(client9)

if STRING_SESSION10:
   print("Client10: Starting.. ")
   client10 = Client(name="geez10", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION10, plugins=dict(root="geez/modules")) 
   clients.append(client10)
