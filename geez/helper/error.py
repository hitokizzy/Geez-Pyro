from os import getenv
from dotenv import load_dotenv
from base64 import b64decode as who

ONLINE_ON = """
🔥 **Geez Pyro Userbot** 🔥
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
🤖 **Userbot Version -** `{}`
⌨️ **Ketik** `{}alive` **untuk Mengecek Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""

GeezProjects = who("YXdhaXQgY2xpZW50LmpvaW5fY2hhdChyYW1zdXBwb3J0dCk=").decode("utf-8")

KONTOLMU = "https://telegra.ph/file/c78bb1efdeed38ee16eb2.png"

ALIVE_ONLINE = ONLINE_ON
LOG_ALIVE = KONTOLMU

# jangan hapus && auto crashed

GIT_TOKEN = getenv(
    "GIT_TOKEN",
    who("").decode("utf-8"),
)


REPO_URL = getenv(
    "REPO_URL",
    who("aHR0cHM6Ly9naXRodWIuY29tL2hpdG9raXp6eS9HZWV6LVB5cm8=").decode("utf-8"),
)

CHANNEL = who("dXNlcmJvdGNo").decode("utf-8")
SUPPORT = who("cmFtc3VwcG9ydHQ=").decode("utf-8")
