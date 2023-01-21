from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "11891876"))
    API_HASH = getenv("API_HASH", "b48fe8105495265d1095038f8b5778cf")
    BOT_TOKEN = getenv("BOT_TOKEN", "5621620222:AAHw_X2emdBlaQBqYdD8XtF8KFTbm1DgbiA")

config = Config()
