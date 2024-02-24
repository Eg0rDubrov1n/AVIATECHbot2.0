from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
import calendar

from core.unit.Bitrix24 import POSTbitrix24
from core.unit.state import s_Data

async def iKB_s_Tasks(state: FSMContext):# Работа с Bitrix!!!
    data = await state.get_data()
    TasksKeyboardIn = InlineKeyboardBuilder()

    for Task in POSTbitrix24("tasks.task.list",{"order":{"DEADLINE":'asc'},"filter": {"RESPONSIBLE_ID" : "308"},"select": [ "ID", "TITLE","RESPONSIBLE_ID"],"start": f"{10 * (s_Data.quantity - 1)}"})["tasks"]:
        TasksKeyboardIn.button(text=f'{Task.get("title")}', callback_data = str(Task.get("id")))

    TasksKeyboardIn.button(text="<", callback_data="<")
    TasksKeyboardIn.adjust(1)
    TasksKeyboardIn.button(text=">", callback_data=">")

    TasksKeyboardIn.button(text="exit", callback_data="exit")


    return TasksKeyboardIn.as_markup()

async def iKB_s_Tasks_UP(call: CallbackQuery, state: FSMContext):# Работа с Bitrix!!!
    s_Data.quantity += 1
    await call.message.edit_reply_markup(
        reply_markup=await iKB_s_Tasks(state)
    )

async def iKB_s_Tasks_Down(call: CallbackQuery, state: FSMContext):# Работа с Bitrix!!!
    if s_Data.quantity > 1:
        s_Data.quantity -= 1
        await call.message.edit_reply_markup(
            reply_markup=await iKB_s_Tasks(state)
        )

async def iKB_s_Info_Task(state: FSMContext):# Работа с Bitrix!!!
    # data = await state.get_data()
    TasksKeyboardIn = InlineKeyboardBuilder()
    #
    # for Task in POSTbitrix24("tasks.task.list",{"order":{"DEADLINE":'asc'},"filter": {"RESPONSIBLE_ID" : "308"},"select": [ "ID", "TITLE","RESPONSIBLE_ID"],"start": f"{10 * (s_Data.quantity - 1)}"})["tasks"]:
    #     TasksKeyboardIn.button(text=f'{Task.get("title")}', callback_data = str(Task.get("id")))
    #
    # TasksKeyboardIn.button(text="<", callback_data="<")
    # TasksKeyboardIn.adjust(1)
    # TasksKeyboardIn.button(text=">", callback_data=">")
    TasksKeyboardIn.button(text="exit", callback_data="exit_iKB_s_Tasks")
    return TasksKeyboardIn.as_markup()