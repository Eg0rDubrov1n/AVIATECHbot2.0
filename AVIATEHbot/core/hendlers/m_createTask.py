from aiofiles import os
from aiogram import Bot
import json
from aiogram.fsm.context import FSMContext
from aiogram import types


from aiogram.types import Message, CallbackQuery

from core.keyboards.inline import iKB_CreateTask, iKB_s_User, iKB_s_Lead, iKB_s_Fils
from core.unit.state import s_Data


async def m_createTask_TITLE(message: Message, state: FSMContext, bot: Bot) -> None:
    await state.update_data(TITLE=message.text)
    await bot.edit_message_text(text="Новая задача", reply_markup=await iKB_CreateTask(state),
                                chat_id=s_Data.CHAT_ID, message_id=s_Data.MESSEGE_ID)

async def GenerateArr_ID(tagForm:str,element: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    temporaryArray_ID = list()
    if data.get(tagForm) != None:
        temporaryArray_ID = data.get(tagForm)
    if element in temporaryArray_ID:
        temporaryArray_ID.remove(element)
    else:
        temporaryArray_ID.append(element)
    return temporaryArray_ID


async def m_createTask_RESPONSIBLE(call: CallbackQuery, state: FSMContext,bot:Bot):
    # print("State UPDETE RESPONSIBLE")
    await state.update_data(RESPONSIBLE_ID= await GenerateArr_ID("RESPONSIBLE_ID",call.data,state))
    await call.message.edit_reply_markup(
        reply_markup=await iKB_s_User(state)
    )

async def m_createTask_UF_CRM_TASK(call: CallbackQuery, state: FSMContext,bot:Bot):
    await state.update_data(UF_CRM_TASK= await GenerateArr_ID("UF_CRM_TASK",call.data,state))
    await call.message.edit_reply_markup(
        reply_markup=await iKB_s_Lead(state)
    )


async def m_createTask_DESCRIPTION(message: Message, state: FSMContext, bot:Bot) -> None:
    await state.update_data(DESCRIPTION=message.text)
    await bot.edit_message_text(text="Новая задача", reply_markup=await iKB_CreateTask(state),
                                chat_id=s_Data.CHAT_ID, message_id=s_Data.MESSEGE_ID)

async def Add_ID_in_Dict(tagForm:str,key:CallbackQuery,values: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    # print("key,values-->",key,values)
    temporaryDict_ID = dict()
    if data.get(tagForm) != None:
        temporaryDict_ID = data.get(tagForm)
    if not (key in temporaryDict_ID):
        temporaryDict_ID[key] = values
    return temporaryDict_ID

async def Pop_ID_in_Dict(tagForm:str,key:CallbackQuery, state: FSMContext):
    data = await state.get_data()
    # print("key,values-->",key)
    temporaryDict_ID = dict()
    if data.get(tagForm) != None:
        temporaryDict_ID = data.get(tagForm)
    temporaryDict_ID.pop(key)
    return temporaryDict_ID

async def m_createTask_UF_TASK_WEBDAV_FILES(message: Message, bot : Bot, state: FSMContext):
    await state.update_data(UF_TASK_WEBDAV_FILES=await Add_ID_in_Dict("UF_TASK_WEBDAV_FILES",message.document.file_name, message.document.file_id,state))
    await bot.edit_message_text(text="Файлы", reply_markup=await iKB_s_Fils(state),
                                chat_id=s_Data.CHAT_ID, message_id=s_Data.MESSEGE_ID)

async def m_createTask_UF_TASK_WEBDAV_FILES_del(call: CallbackQuery, bot : Bot, state: FSMContext):
    await state.update_data(UF_TASK_WEBDAV_FILES=await Pop_ID_in_Dict("UF_TASK_WEBDAV_FILES",call.data,state))
    await bot.edit_message_text(text="Файлы", reply_markup=await iKB_s_Fils(state),
                                chat_id=s_Data.CHAT_ID, message_id=s_Data.MESSEGE_ID)

async def m_createTask_DEADLINE(call: CallbackQuery, bot : Bot, state: FSMContext):
    if call.data in "None":
        return None
    await state.update_data(DEADLINE=call.data)
    await bot.edit_message_text(text="Новая задача", reply_markup=await iKB_CreateTask(state),
                                chat_id=s_Data.CHAT_ID, message_id=s_Data.MESSEGE_ID)
