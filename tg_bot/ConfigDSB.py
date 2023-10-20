from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 5278953200  # my telegram ID
    OWNER_USERNAME = "senor_cristo"  # my telegram username
    API_KEY = "6714185998:AAG6kuo07dY5lygl1gy7z2CrrrJStHMi6Pk"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgres://cardinalsaint:CardiCCodes@database-1.cxelifqjcwbt.us-east-2.rds.amazonaws.com:5431/DeeppDB'  # sample db credentials
    MESSAGE_DUMP = '-1234567890' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [5278953200]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']




class Development(Config):
    LOGGER = True
