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
from core.unit.SQL import getSQL, countSQL
from core.unit.state import s_Data, s_CreateTask, User


async def SettingsStart(message: Message, state: FSMContext):
    await state.clear()

    await message.answer(text=f"НАСТРОЙКИ",
            reply_markup=SettingsKeyBoard)

    s_Data.MESSEGE_ID =  str(int(message.message_id) + 1)


async def settings_URL(call: CallbackQuery, state: FSMContext):
    await state.set_state(User.URL)
    print("settings_URL")
    await call.answer("Введите url")

async def settings_folderId(call: CallbackQuery, state: FSMContext):
    await state.set_state(User.folderId)
    print("settings_folderId")
    await call.answer("Введите ID папки")
