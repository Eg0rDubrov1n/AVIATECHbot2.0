from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

rKB_MainTask = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Создать задачу"),KeyboardButton(text="Мои задачи"), KeyboardButton(text="Настройки")]
    ]
)