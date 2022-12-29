import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = "24956859"
API_HASH = "69600e321da283e601378d349a86d352"
STRING_SESSION1 = "BQCfPnxSAZ1JIGwhEFcknSu0okORqMafnziA6jxlmeZWljHXCptutEE6yPmdjPLdzf3GoES0IcFxwILIgWT0c1c_33Jesa-soDCXDI0Da7sELCN3ZOYtzr76e-ZgLMPXON-AmtbbtY-W1O9P3HuxD8_VQCe3ib7qN_OcspDnEa2dNmaPU3d910pU6SyhtN8vfG0zvFUBh91O_2hZkTlPECN9v-dFrMWtquw59pEjwzqmUFTyOA0T1OVuQ0f6IFTDYbNO0qD6ffkGetBhBF6Jzui9iL3pPdDx-tf9uiJO9hcXZaD08p5lPMOsrrqfu4HYfIt8q5P_KJYE-bByIMJGZ--Sd2fdBAA"
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
OWNER_ID = "2003295492"
BOT_TOKEN = "5931456213:AAG6wBLe0TufEaHsZxgLf7GI3e_yQCr3TXU"
MONGO_URL = "mongodb+srv://izzy:izzy123@cluster0.vy9shgr.mongodb.net/?retryWrites=true&w=majority"
ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/c78bb1efdeed38ee16eb2.png")
ALIVE_TEXT = getenv("ALIVE_TEXT", "Geez-Pyro UserBot, Sumpah gada yg spesial...")
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
