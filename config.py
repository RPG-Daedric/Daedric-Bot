from dotenv import load_dotenv
from environs import Env

env = Env()
load_dotenv()


class Config:
    DISCORD_TOKEN = env.str("DISCORD_TOKEN")
    APP_ENV = env.str("APP_ENV")


config_selector = {
    'development': Config
}
