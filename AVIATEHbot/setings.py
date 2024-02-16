import pymysql
from bitrix24 import Bitrix24
from environs import  Env
from dataclasses import dataclass
# from pybitrix24 import Bitrix24


# bx24 = Bitrix24('https://eurotechpromg.bitrix24.ru/rest/308/2gnr740m6pfywjof/')

@dataclass
class Server:
    host: str
    port: int
    user: str
    password: str
    db_name: str
    # admin_id: str
@dataclass
class Bots:
    bot_token: str
    path_save: str
    # admin_id: str
@dataclass
class User:
    folderId: str
@dataclass
class Settings:
    bots :Bots
    server: Server
    user: User

def get_settings(path: str):
    env = Env()
    env.read_env(path)
    return  Settings(
        bots = Bots(
            bot_token = env.str("TOKEN"),
            path_save = env.str("myPATH")
            # admin_id = env.str("ADMIN_ID")
        ),
        server = Server(
            host = env.str("HOST"),
            port=env.str("PORT"),
            user = env.str("USER"),
            password = env.str("PASSWORD"),
            db_name = env.str("DB_NAME")
        ),
        user = User(
            folderId = env.str("folderId")
        )
    )
def Connect():
    connect = pymysql.connect(
        host=settings.server.host,
        port=int(settings.server.port),
        user=settings.server.user,
        password=settings.server.password,
        database=settings.server.db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    return connect

from aiogram.fsm.state import StatesGroup, State

class User_settings(StatesGroup):
    url = State()
    folderID = State()


settings = get_settings('input')
print(settings)
