from aiofiles import os
from aiogram import Bot
import json
from aiogram.fsm.context import FSMContext
from aiogram import types


from aiogram.types import Message, CallbackQuery

from core.keyboards.inline import iKB_CreateTask, iKB_s_User, iKB_s_Lead
from core.unit.state import s_Data


async def m_createTask_TITLE(message: Message, state: FSMContext, bot: Bot) -> None:
    print("State UPDETE TITLE")

    await state.update_data(TITLE=message.text)
    await bot.edit_message_text(text="ОБНОВА", reply_markup=await iKB_CreateTask(state),
                                chat_id=s_Data.CHAT_ID, message_id=s_Data.MESSEGE_ID)

async def GenerateArr_ID(tagForm:str,call: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    temporaryArray_ID = list()
    if data.get(tagForm) != None:
        temporaryArray_ID = data.get(tagForm)
    if call.data in temporaryArray_ID:
        temporaryArray_ID.remove(call.data)
    else:
        temporaryArray_ID.append(call.data)
    return temporaryArray_ID

async def m_createTask_RESPONSIBLE(call: CallbackQuery, state: FSMContext,bot:Bot):
    print("State UPDETE RESPONSIBLE")
    await state.update_data(RESPONSIBLE_ID= await GenerateArr_ID("RESPONSIBLE_ID",call,state))
    await call.message.edit_reply_markup(
        reply_markup=await iKB_s_User(state)
    )

async def m_createTask_UF_CRM_TASK(call: CallbackQuery, state: FSMContext,bot:Bot):
    await state.update_data(UF_CRM_TASK= await GenerateArr_ID("UF_CRM_TASK",call,state))
    await call.message.edit_reply_markup(
        reply_markup=await iKB_s_Lead(state)
    )


async def m_createTask_DESCRIPTION(message: Message, state: FSMContext, bot:Bot) -> None:
    print("State UPDETE DESCRIPTION")
    await state.update_data(DESCRIPTION=message.text)
    await bot.edit_message_text(text="ОБНОВА", reply_markup=await iKB_CreateTask(state),
                                chat_id=s_Data.CHAT_ID, message_id=s_Data.MESSEGE_ID)

async def m_createTask_UF_TASK_WEBDAV_FILES(message: Message, bot : Bot, state: FSMContext):
    print("State UPDETE UF_TASK_WEBDAV_FILES")

    await state.update_data(UF_TASK_WEBDAV_FILES=message.document.file_id)
    await bot.edit_message_text(text="ОБНОВА", reply_markup=await iKB_CreateTask(state),
                                chat_id=s_Data.CHAT_ID, message_id=s_Data.MESSEGE_ID)

async def m_createTask_DEADLINE(call: CallbackQuery, bot : Bot, state: FSMContext):
    print("State UPDETE UF_TASK_WEBDAV_FILES")

    await state.update_data(DEADLINE=call.data)
    await bot.edit_message_text(text="ОБНОВА", reply_markup=await iKB_CreateTask(state),
                                chat_id=s_Data.CHAT_ID, message_id=s_Data.MESSEGE_ID)
