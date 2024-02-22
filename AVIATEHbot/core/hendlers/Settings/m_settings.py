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
from bitrix24 import Bitrix24

from core.keyboards.Settings.inline_Settings import SettingsKeyBoard
from core.keyboards.inline import iKB_CreateTask, iKB_User, iKB_s_User, Callender, iKB_s_Lead
from core.keyboards.reply import rKB_MainTask
from core.unit.Bitrix24 import writeInBitrix24
from core.unit.SQL import setSQL
from core.unit.state import s_Data, s_CreateTask


async def m_settings_URL(message: Message, state: FSMContext, bot: Bot):
    print("m_settings_URL")
    await state.update_data(URL=message.text)
    setSQL("users","URL",message.text)


async def m_settings_folderID(message: Message, state: FSMContext):
    await state.update_data(folderId=message.text)
    print("m_settings_URL")
    await state.update_data(URL=message.text)
    setSQL("users","FolderID",message.text)
