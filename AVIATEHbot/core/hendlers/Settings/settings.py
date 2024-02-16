import calendar
import json
import shutil

import archive
import os

import pymysql
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery

from core.keyboards.Settings.inline_Settings import SettingsKeyBoard
from core.keyboards.inline import iKB_CreateTask, iKB_User, iKB_s_User, Callender, iKB_s_Lead
from core.keyboards.reply import rKB_MainTask
from core.unit.Bitrix24 import writeInBitrix24
from core.unit.state import s_Data, s_CreateTask
from setings import User_settings


async def SettingsStart(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(text=f"Здравствуйте",
            reply_markup=SettingsKeyBoard)

    s_Data.MESSEGE_ID =  str(int(message.message_id) + 1)
    s_Data.CHAT_ID = message.chat.id

async def settings_URL(call: CallbackQuery, state: FSMContext):
    print("createTask_DESCRIPTION")
    await call.answer("Введите краткое url")
    await state.set_state(User_settings.url)

async def settings_URL(call: CallbackQuery, state: FSMContext):
    print("createTask_DESCRIPTION")
    await call.answer("Введите ID папки")
    await state.set_state(User_settings.folderID)
