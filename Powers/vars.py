from os import getcwd

from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

env_file = f"{getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])


class Config:
    """Config class for variables."""

    LOGGER = True
    BOT_TOKEN = config("BOT_TOKEN", default="6174431362:AAHFZi74qbO5n-yhuu21kh6xOqdFmuRYwu0")
    API_ID = int(config("API_ID", default="28122413"))
    API_HASH = config("API_HASH", default="750432c8e1b221f91fd2c93a92710093")
    OWNER_ID = int(config("OWNER_ID", default=5443243540))
    MESSAGE_DUMP = int(config("MESSAGE_DUMP", default=-100))
    DEV_USERS = [
        int(i)
        for i in config(
            "DEV_USERS",
            default="5443243540 5453933259 5125896572",
        ).split(" ")
    ]
    SUDO_USERS = [
        int(i)
        for i in config(
            "SUDO_USERS",
            default="5443243540 5453933259 5125896572",
        ).split(" ")
    ]
    WHITELIST_USERS = [
        int(i)
        for i in config(
            "WHITELIST_USERS",
            default="5443243540 5453933259 5125896572",
        ).split(" ")
    ]
    GENIUS_API_TOKEN = config("GENIUS_API")
    DB_URI = config("DB_URI", default="")
    DB_NAME = config("DB_NAME", default="")
    NO_LOAD = config("NO_LOAD", default="").split()
    PREFIX_HANDLER = config("PREFIX_HANDLER", default="/").split()
    SUPPORT_GROUP = config("SUPPORT_GROUP", default="Kira_bot_support")
    SUPPORT_CHANNEL = config("SUPPORT_CHANNEL", default="SIAmKira_BotSupport")
    VERSION = config("VERSION", default="v2.0")
    WORKERS = int(config("WORKERS", default=16))
    BOT_USERNAME = "S_I_Am_Kira_Bot"
    BOT_ID = "6174431362"
    BOT_NAME = "Kira"
    owner_username = "SIAmKira"


class Development:
    """Development class for variables."""

    # Fill in these vars if you want to use Traditional method of deploying
    LOGGER = True
    BOT_TOKEN = "YOUR BOT_TOKEN"
    API_ID = 12345  # Your APP_ID from Telegram
    API_HASH = "YOUR API HASH"  # Your APP_HASH from Telegram
    OWNER_ID = 1344569458  # Your telegram user id defult to mine
    MESSAGE_DUMP = -100  # Your Private Group ID for logs
    DEV_USERS = []
    SUDO_USERS = [1906306037]
    WHITELIST_USERS = []
    DB_URI = ""  # Your mongo DB URI
    DB_NAME = ""  # Your DB name
    NO_LOAD = []
    GENIUS_API_TOKEN = ""
    PREFIX_HANDLER = ["!", "/"]
    SUPPORT_GROUP = "SUPPORT_GROUP"
    SUPPORT_CHANNEL = "SUPPORT_CHANNEL"
    VERSION = "VERSION"
    WORKERS = 8
