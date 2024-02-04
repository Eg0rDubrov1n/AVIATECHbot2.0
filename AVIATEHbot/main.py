import logging
import sys
import calendar
from pydoc import html
from typing import Optional
import os
from aiofiles import os
from aiogram.dispatcher import router
from aiogram.enums import ContentType
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from datetime import datetime
from aiogram.filters import CommandStart, StateFilter, Command

from aiogram.handlers import callback_query
import asyncio
from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup, KeyboardButton, \
    ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types.callback_query import CallbackQuery

from core.hendlers.createTask import createTask, createTask_TITLE, createTask_RESPONSIBLE, createTask_DESCRIPTION, \
    createTask_UF_TASK_WEBDAV_FILES, createTask_send, createTask_exit_In_iKB_CreateTask, createTask_DEADLINE, \
    createTask_UF_CRM_TASK
from core.hendlers.m_createTask import m_createTask_RESPONSIBLE, m_createTask_TITLE, m_createTask_DESCRIPTION, \
    m_createTask_UF_TASK_WEBDAV_FILES, m_createTask_DEADLINE, m_createTask_UF_CRM_TASK
from core.keyboards.inline import iKB_s_User_UP, iKB_s_User_Down, Callender, iKB_Callender_Last_mounth, \
    iKB_Callender_Next_mounth, iKB_s_Lead_UP, iKB_s_Lead_Down
from core.unit.SQL import getSQLOneCommand
from core.unit.state import s_Data, s_CreateTask
from setings import settings, Connect, bx24


async def Registration(message: Message):
    s_Data.CHAT_ID = message.chat.id
    connect = Connect()
    with connect.cursor() as cursor:
        if not getSQLOneCommand(f"SELECT EXISTS(SELECT * FROM `colleagues` where ChatID = '{message.chat.id}');"):
            # await state.set_state(Specialist.ID)
           # I await message.answer(text="Выберите себя в списке",
           #                       reply_markup=await iKB_User()
           #                       )
            pass
async def Check(message: Message, state: FSMContext):
    print(bx24.callMethod('crm.lead.list')[0])
    # await state.set_state(s_CreateTask.DEADLINE)
    # await message.answer(text=f"{s_Data.YEAR}\n{calendar.month_name[s_Data.MONTH]}",
    #                      reply_markup=await Callender()
    #                      )
async def Start():
    dp = Dispatcher()
    bot = Bot(settings.bots.bot_token)

    dp.message.register(Registration,Command(commands=["start","registration"]))
    dp.message.register(Check,Command(commands=["check"]))


    dp.message.register(createTask,F.text.lower() == "cоздать задачу")

    dp.callback_query.register(createTask_TITLE, F.data == 'createTask_TITLE')  # Отправить названия Задачи
    dp.callback_query.register(createTask_RESPONSIBLE, F.data == 'createTask_RESPONSIBLE')  # Выбрать специалиста
    dp.callback_query.register(createTask_UF_CRM_TASK, F.data == 'createTask_UF_CRM_TASK')  # Выбрать специалиста
    dp.callback_query.register(createTask_DESCRIPTION, F.data == 'createTask_DESCRIPTION')  # Отправить Описание
    dp.callback_query.register(createTask_UF_TASK_WEBDAV_FILES, F.data == 'createTask_UF_TASK_WEBDAV_FILES')  # Отправить ZIP-file
    dp.callback_query.register(createTask_DEADLINE, F.data == 'createTask_DEADLINE')  # Отправить ZIP-file
    dp.callback_query.register(createTask_send, F.data.lower() == 'send')  # Сохранить
    dp.callback_query.register(createTask_exit_In_iKB_CreateTask, F.data == 'exit_In_iKB_CreateTask')  # Сохранить

    dp.callback_query.register(iKB_s_Lead_UP, s_CreateTask.UF_CRM_TASK, F.data == '>')  # Отправить ZIP-file
    dp.callback_query.register(iKB_s_Lead_Down, s_CreateTask.UF_CRM_TASK, F.data == '<')  # Отправить ZIP-file
    dp.callback_query.register(iKB_s_User_UP, s_CreateTask.RESPONSIBLE_ID ,F.data == '>')  # Отправить ZIP-file
    dp.callback_query.register(iKB_s_User_Down, s_CreateTask.RESPONSIBLE_ID, F.data == '<')  # Отправить ZIP-file
    dp.callback_query.register(iKB_Callender_Next_mounth, s_CreateTask.DEADLINE, F.data == '>')  # Отправить DEADLINE
    dp.callback_query.register(iKB_Callender_Last_mounth, s_CreateTask.DEADLINE, F.data == '<')  # Отправить DEADLINE

    dp.message.register(m_createTask_TITLE, s_CreateTask.TITLE)  # Ввод названия
    dp.message.register(m_createTask_DESCRIPTION, s_CreateTask.DESCRIPTION)  # Ввод Описания
    dp.message.register(m_createTask_UF_TASK_WEBDAV_FILES, s_CreateTask.UF_TASK_WEBDAV_FILES, F.document)  # Ввод Zip file
    dp.callback_query.register(m_createTask_DEADLINE, s_CreateTask.DEADLINE)
    dp.callback_query.register(m_createTask_RESPONSIBLE, s_CreateTask.RESPONSIBLE_ID)
    dp.callback_query.register(m_createTask_UF_CRM_TASK, s_CreateTask.UF_CRM_TASK)


    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(Start())