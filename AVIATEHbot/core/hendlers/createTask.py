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

from core.keyboards.inline import iKB_CreateTask, iKB_User, iKB_s_User, Callender, iKB_s_Lead
from core.keyboards.reply import rKB_MainTask
from core.unit.Bitrix24 import writeInBitrix24
from core.unit.SQL import countSQL
from core.unit.state import s_Data, s_CreateTask


async def createTask(message: Message, state: FSMContext):
    # await state.clear()
    if 1 > countSQL("users", "ChatID", message.chat.id):
        return None
    try:
        await message.answer(text=f"Здравствуйте",
            reply_markup=await iKB_CreateTask(state)
        )
    except Exception:
        print(Exception)
    s_Data.MESSEGE_ID =  str(int(message.message_id) + 1)
    s_Data.CHAT_ID = message.chat.id

async def createTask_TITLE(call: CallbackQuery, state: FSMContext):
    print("createTask_TITLE")
    await call.answer("Введите название проекта")
    await state.set_state(s_CreateTask.TITLE)

async def createTask_RESPONSIBLE(call: CallbackQuery, state: FSMContext):
    print("createTask_RESPONSIBLE")
    s_Data.quantity = 1
    await state.set_state(s_CreateTask.RESPONSIBLE_ID)
    await call.answer("Выберите специалистов")
    await call.message.edit_reply_markup(
        reply_markup=await iKB_s_User(state)
    )
async def createTask_UF_CRM_TASK(call: CallbackQuery, state: FSMContext):
    print("createTask_UF_CRM_TASK")
    s_Data.quantity = 1
    await state.set_state(s_CreateTask.UF_CRM_TASK)
    await call.answer("Выберите лид")
    await call.message.edit_reply_markup(
        reply_markup=await iKB_s_Lead(state)
    )
async def createTask_DESCRIPTION(call: CallbackQuery, state: FSMContext):
    print("createTask_DESCRIPTION")
    await call.answer("Введите краткое описание проекта")
    await state.set_state(s_CreateTask.DESCRIPTION)

async def createTask_UF_TASK_WEBDAV_FILES(call: CallbackQuery, state: FSMContext):
    print("createTask_UF_TASK_WEBDAV_FILES")
    await call.answer("Загрузите файл")
    await state.set_state(s_CreateTask.UF_TASK_WEBDAV_FILES)

async def createTask_DEADLINE(call: CallbackQuery, state: FSMContext):
    print("DEADLINE")
    await call.answer("DEADLINE")
    await state.set_state(s_CreateTask.DEADLINE)
    await call.message.edit_text(text=f"{s_Data.YEAR}\n{calendar.month_name[s_Data.MONTH]}",
                         reply_markup=await Callender()
                         )




async def createTask_send(call: CallbackQuery, state: FSMContext, bot : Bot):

    data = await state.get_data()
    if data.get("TITLE") != None and data.get("RESPONSIBLE_ID") != None:
        await writeInBitrix24(data,bot)
        await state.clear()
    else:
        await call.message.answer(text="Error: Неуказанно имя!!!")

async def _exit(call: CallbackQuery, state: FSMContext):
    await state.clear()
    # await call.message.edit_reply_markup()
    await call.message.edit_text(text="closed")
    await call.message.answer("What Project?",reply_markup=rKB_MainTask)

async def createTask_exit_In_iKB_CreateTask(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup("What Project?", reply_markup=await iKB_CreateTask(state))
