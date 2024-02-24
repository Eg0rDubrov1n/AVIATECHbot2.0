import calendar
import json
import shutil

import archive
import os

import pymysql
import requests
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery
from bitrix24 import Bitrix24

from core.keyboards.Settings.inline_Settings import SettingsKeyBoard
from core.keyboards.inline import iKB_CreateTask, iKB_User, iKB_s_User, Callender, iKB_s_Lead
from core.keyboards.reply import rKB_MainTask
from core.unit.Bitrix24 import writeInBitrix24, POSTbitrix24
from core.unit.SQL import setSQL, getSQL
from core.unit.state import s_Data, s_CreateTask


async def m_settings_URL(message: Message, state: FSMContext, bot: Bot):
    print("m_settings_URL")
    try:
        print(requests.post(f'{message.text}{"user.fields"}.json',
                         timeout=60).json())
    except Exception as error:
        await message.answer(text=f"Error: {error}")
        await message.answer(text="Проверте правильность написания URL")
        return None
    await state.update_data(URL=message.text)
    setSQL("users","URL",message.text)


async def m_settings_folderID(message: Message, state: FSMContext):
    print("m_settings_folderID")
    # try
    if True:
        try:
            print(requests.post(f'{getSQL("users", ["URL"], "ChatID", s_Data.CHAT_ID)["URL"]}{"user.fields"}.json',
                                timeout=60).json())
        except Exception as error:
            await message.answer(text=f"Error: {error}")
            await message.answer(text="Проверте правильность написания URL")
            return None

        try:
             await message.answer(text="Error:" + requests.post(f'{getSQL("users",["URL"],"ChatID",s_Data.CHAT_ID)["URL"]}{"disk.folder.get"}.json',json={"id":message.text},timeout=60).json()["error"])
             await message.answer(text="Проверте правильность введенного ID")

        except Exception as error:
            await state.update_data(folderId=message.text)
            setSQL("users", "FolderID", message.text)

    # except Exception as error :
    #     await message.answer(text=f"Error: {error}")
    #     await message.answer(text=f"Проверте правильность ID папки")
    #     return None

