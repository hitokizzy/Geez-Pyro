import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")


API_ID = "24956859"
API_HASH = "69600e321da283e601378d349a86d352"
STRING_SESSION1 = "BQAhIHQASfPK9dhdwcySF4kLBsezdSAm9Vxmz7CGz1mYKRv6OWolMcryWBUIO2wK8I_9yc7DcVSxe3T0Vz8TvuuILhnUeJz3OgZDSuJ6qt6L55kUIs7oyU4NN3qO9LNsXA9sRjmY6zaaLrsJrWaOAxZKHFr-7v177mKfZZz_ykw0eJLzUaIdYQU5KazF7qb98_qLvQoS1_csH3Cf7ZTV1uZ1ZZ5prdEzsYrSwm4-H3zCB-ReSVyAAAVaN1o6jW4f0e550gO0xf3sAH8MCW6umUmIZdImUKLaHqyittwr2WgWrIOZUdNORkYq475cCW4p0HQcW0pZv_9KdVALjWC5FZTUTPMGyQAAAAB3Z90EAA"
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = "2003295492"
BOT_TOKEN = "5816749146:AAENtkguWUIkP21IkuZvXoEhE3N8znuyhoE"
MONGO_URL = "mongodb+srv://izzy:izzy123@cluster0.vy9shgr.mongodb.net/?retryWrites=true&w=majority"
ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/c78bb1efdeed38ee16eb2.png")
ALIVE_TEXT = getenv("ALIVE_TEXT", "")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/hitokizzy/Geez-Pyro")
BRANCH = getenv("BRANCH", "main") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
