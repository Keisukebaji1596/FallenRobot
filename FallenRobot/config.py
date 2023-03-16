class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 26959103
    API_HASH = "ebe24f37c6f8ee727fc406c68ba5bc70"

    CASH_API_KEY = "IU3DP7MDMTQDRXQS"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://yhwuogma:rRWDWa7kOXpoSuS24OLMiTFtBe-7Oztd@isilo.db.elephantsql.com/yhwuogma"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001857365749)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://Anshul0554:Anshul0554@cluster0.uwx7fnj.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/40eb1ed850cdea274693e.jpg"

    SUPPORT_CHAT = "HentaiAssociation"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6175188005:AAFxIHCt9v5QzKdmgkTFpzZ5ADWZIRkoUXg"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "CRJY2DIG3FAN"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 1356469075  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
