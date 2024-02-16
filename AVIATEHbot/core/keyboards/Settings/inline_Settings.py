from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
import calendar

from core.unit.Bitrix24 import POSTbitrix24
from core.unit.state import s_Data



SettingsKeyBoard = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text="URL",callback_data="url")],
                     [InlineKeyboardButton(text="Id папки",callback_data="folderID")],
                     [InlineKeyboardButton(text='Exit', url=None, callback_data='exit')]
    ]
)
