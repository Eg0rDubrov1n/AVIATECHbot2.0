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

from core.keyboards.Settings.inline_Settings import SettingsKeyBoard
from core.keyboards.Viewing_tasks.inline_viewing_tasks import iKB_s_Tasks, iKB_s_Info_Task
from core.keyboards.inline import iKB_CreateTask, iKB_User, iKB_s_User, Callender, iKB_s_Lead
from core.keyboards.reply import rKB_MainTask
from core.unit.Bitrix24 import writeInBitrix24, POSTbitrix24
from core.unit.SQL import getSQL, countSQL
from core.unit.state import s_Data, s_CreateTask, User

async def viewingTasks(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(s_Data.Task)
    if 1 > countSQL("users", "ChatID", message.chat.id):
        await message.answer(text=f"Вы не настроили доступ")
        await message.answer(text=f"Настройки",
                             reply_markup= SettingsKeyBoard
                             )
        return None
    try:
        await message.answer(text=f"Мои задачи",
            reply_markup=await iKB_s_Tasks(state)
        )
    except Exception as error:
        print(error)
    s_Data.MESSEGE_ID =  str(int(message.message_id) + 1)
    # s_Data.CHAT_ID = message.chat.id


async def viewingTaskInfo(call: CallbackQuery, state: FSMContext,bot:Bot):
    info = POSTbitrix24("tasks.task.get",{"taskId":call.data,"select": ["TITLE","DESCRIPTION","DEADLINE"]})["task"]
    # print(requests.post(f'{getSQL("users", ["URL"], "ChatID", s_Data.CHAT_ID)["URL"]}{"tasks.task.get"}.json',
    #               json={"select": ["TITLE", "DESCRIPTION", "STATUS", "DEADLINE"]},
    #               timeout=60).json())
    print(info)
    # await state.update_data(Task=call.data)
    # state.clear()
    await bot.edit_message_text(text=f'<strong>{info.get("title")}\n\n</strong>'
                                     f'{info.get("description")}\n'
                                     f'<i>{" " if info.get("deadline")==None else info.get("deadline").split("T")[0]}\n</i>',
                                reply_markup=await iKB_s_Info_Task(state),
                                chat_id=s_Data.CHAT_ID, message_id=s_Data.MESSEGE_ID, parse_mode='HTML')


async def viewingTasks_exit_In_iKB_viewingTasks(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("Мои задачи", reply_markup=await iKB_s_Tasks(state))
