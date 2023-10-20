class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "6714185998:AAG6kuo07dY5lygl1gy7z2CrrrJStHMi6Pk"
    OWNER_ID = "5278953200" # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "senor_cristo"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgres://cardinalsaint:CardiCCodes@database-1.cxelifqjcwbt.us-east-2.rds.amazonaws.com:5431/DeeppDB'  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = ['translation', 'rss']
    WEBHOOK = False
    URL = None

    # OPTIONAL
    SUDO_USERS = []  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = []  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = []  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = False
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker
    ALLOW_EXCL = False  # Allow ! commands as well as /


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
