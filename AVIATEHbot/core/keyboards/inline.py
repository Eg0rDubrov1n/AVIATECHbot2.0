import requests
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
import calendar

from core.unit.Bitrix24 import POSTbitrix24
from core.unit.state import s_Data


async def iKB_CreateTask(state: FSMContext):
    data = await state.get_data()
    # state:FSMContext = Form.name_Tasks
    MainKeyBoard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text=f'Название {["🔴","🟢"][data.get("TITLE") != None]}', url=None, callback_data='createTask_TITLE')],
                         [InlineKeyboardButton(text=f'Назначте специалистов {["🔴","🟢"][data.get("RESPONSIBLE_ID") != None]}', url=None, callback_data='createTask_RESPONSIBLE')],
                         [InlineKeyboardButton(text=f'Описание {["🔴","🟢"][data.get("DESCRIPTION") != None]}', url=None, callback_data='createTask_DESCRIPTION')],
                         [InlineKeyboardButton(text=f'Загрузить файл {["🔴","🟢"][data.get("UF_TASK_WEBDAV_FILES") != None]}', url=None, callback_data='createTask_UF_TASK_WEBDAV_FILES')],
                         [InlineKeyboardButton(text=f'CRM {["🔴", "🟢"][data.get("UF_CRM_TASK") != None]}', url=None,callback_data='createTask_UF_CRM_TASK')],
                         [InlineKeyboardButton(text=f'Дата сдачи {["🔴","🟢"][data.get("DEADLINE") != None]}', url=None, callback_data='createTask_DEADLINE')],
                         [InlineKeyboardButton(text='Send', url=None, callback_data='send'), InlineKeyboardButton(text='Exit', url=None, callback_data='exit')]])
    return MainKeyBoard

async def iKB_s_User(state: FSMContext):# Работа с Bitrix!!!
    data = await state.get_data()
    TasksKeyboardIn = InlineKeyboardBuilder()
    for User in POSTbitrix24("user.get",{"select": [ "LAST_NAME", "NAME", "SECOND_NAME","ID"]})[10 * (s_Data.quantity - 1) :10 * s_Data.quantity]:
        TasksKeyboardIn.button(text=f'{User.get("LAST_NAME")} {User.get("NAME")} {User.get("SECOND_NAME")}{["🔴","🟢"][(data.get("RESPONSIBLE_ID") != None and str(User.get("ID")) in data.get("RESPONSIBLE_ID"))]}', callback_data = str(User.get("ID")))

    TasksKeyboardIn.button(text="<", callback_data="<")
    TasksKeyboardIn.adjust(1)
    TasksKeyboardIn.button(text=">", callback_data=">")

    TasksKeyboardIn.button(text="exit", callback_data="exit_In_iKB_CreateTask")


    return TasksKeyboardIn.as_markup()

async def iKB_s_User_UP(call: CallbackQuery, state: FSMContext):# Работа с Bitrix!!!
    s_Data.quantity += 1
    await call.message.edit_reply_markup(
        reply_markup=await iKB_s_User(state)
    )

async def iKB_s_User_Down(call: CallbackQuery, state: FSMContext):# Работа с Bitrix!!!
    s_Data.quantity -= 1
    if s_Data.quantity < 1:
        s_Data.quantity = 1
        await call.message.edit_reply_markup(
            reply_markup=await iKB_s_User(state)
        )



async def iKB_User():# Работа с Bitrix!!!
    TasksKeyboardIn = InlineKeyboardBuilder()
    for User in POSTbitrix24("user.get",{"select": [ "LAST_NAME", "NAME", "SECOND_NAME","ID"]})[10 * (s_Data.quantity - 1) :10 * s_Data.quantity]:
        TasksKeyboardIn.button(text=f'Name:{User.get("Name")}', callback_data=str(User.get("ID")))
    TasksKeyboardIn.button(text="exit", callback_data="exitMainKey")
    TasksKeyboardIn.adjust(1)
    return TasksKeyboardIn.as_markup()

async def Callender():
    import calendar
    TasksKeyboardIn = InlineKeyboardBuilder()
    # _calendar = calendar.TextCalendar()
    # Callender = _calendar.formatmonth(s_Data.YEAR, s_Data.MONTH).replace('   ', ' _ ').split()[1:]
    for dayWeek in calendar.day_abbr:
            TasksKeyboardIn.button(text=f'{dayWeek}',callback_data='None')
    for daysWeek in calendar.monthcalendar(s_Data.YEAR, s_Data.MONTH):
        for day in daysWeek:
            TasksKeyboardIn.button(text=f'{day if day else "_"}', callback_data=f'{f"{day}.{s_Data.MONTH}.{s_Data.YEAR}" if day else "None"}')


    TasksKeyboardIn.button(text="<", callback_data="<")
    TasksKeyboardIn.button(text=">", callback_data=">")

    TasksKeyboardIn.button(text="exit", callback_data="exit_In_iKB_CreateTask")
    TasksKeyboardIn.adjust(7)

    return TasksKeyboardIn.as_markup()

async def iKB_Callender_Next_mounth(call: CallbackQuery, state: FSMContext):# Работа с Bitrix!!!
    print("iKB_Callender_Next_mounth")
    s_Data.MONTH += 1
    if s_Data.MONTH > 12:
        s_Data.MONTH = 1
        s_Data.YEAR += 1
    await call.message.edit_text(text=f"{s_Data.YEAR}\n{calendar.month_name[s_Data.MONTH]}",
        reply_markup=await Callender()
    )

async def iKB_Callender_Last_mounth(call: CallbackQuery, state: FSMContext):# Работа с Bitrix!!!
    print("iKB_Callender_Last_mounth")
    s_Data.MONTH -= 1
    if s_Data.MONTH < 1:
        s_Data.MONTH = 12
        s_Data.YEAR -= 1
    await call.message.edit_text(text=f"{s_Data.YEAR}\n{calendar.month_name[s_Data.MONTH]}",
        reply_markup=await Callender()
    )


async def iKB_s_Lead(state: FSMContext):# Работа с Bitrix!!!
    data = await state.get_data()
    TasksKeyboardIn = InlineKeyboardBuilder()
    # print(requests.post('https://eurotechpromg.bitrix24.ru/rest/308/2gnr740m6pfywjof/crm.lead.list.json',json={"select": [ "ID", "TITLE"],"start": "3"}, timeout=60).json())
    for User in POSTbitrix24("crm.lead.list",{"select": [ "ID", "TITLE"]})[10 * (s_Data.quantity - 1) :10 * s_Data.quantity]:
        TasksKeyboardIn.button(text=f'{User.get("TITLE")}{["🔴","🟢"][(data.get("UF_CRM_TASK") != None and str(User.get("ID")) in data.get("UF_CRM_TASK"))]}', callback_data=str(User.get("ID")))

    TasksKeyboardIn.button(text="<", callback_data="<")
    TasksKeyboardIn.adjust(1)
    TasksKeyboardIn.button(text=">", callback_data=">")

    TasksKeyboardIn.button(text="exit", callback_data="exit_In_iKB_CreateTask")
    return TasksKeyboardIn.as_markup()

async def iKB_s_Lead_UP(call: CallbackQuery, state: FSMContext):# Работа с Bitrix!!!
    s_Data.quantity += 1
    await call.message.edit_reply_markup(
        reply_markup=await iKB_s_Lead(state)
    )

async def iKB_s_Lead_Down(call: CallbackQuery, state: FSMContext):# Работа с Bitrix!!!
    s_Data.quantity -= 1
    if s_Data.quantity < 1:
        s_Data.quantity = 1
        await call.message.edit_reply_markup(
            reply_markup=await iKB_s_Lead(state)
        )