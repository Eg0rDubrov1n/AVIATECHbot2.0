import datetime
from aiogram.fsm.state import StatesGroup, State

class s_CreateTask(StatesGroup):
    TITLE = State() #имя
    DESCRIPTION = State() # Описание
    PRIORITY = State() # Приоретет
    UF_TASK_WEBDAV_FILES = State() # Файл
    RESPONSIBLE_ID = State() # Ответственные
    DEADLINE = State()
    UF_CRM_TASK = State()
class s_Data(StatesGroup):
    MESSEGE_ID = None
    CHAT_ID = None
    DATA_NOW = datetime.datetime.now()
    quantity = 1
    YEAR = DATA_NOW.year
    MONTH = DATA_NOW.month
    Task = State()
class User(StatesGroup):
    URL = State()
    folderId = State()
