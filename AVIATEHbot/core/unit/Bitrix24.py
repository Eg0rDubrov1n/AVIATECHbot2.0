import datetime
import os
import json
import shutil
import base64
import time

import requests as requests

import requests

from aiogram import Bot

from core.unit.SQL import countSQL, getSQL
from core.unit.state import s_Data
from setings import settings, Connect

import tempfile


def POSTbitrix24(command,property):
    return requests.post(f'{getSQL("users", ["URL"], "ChatID", s_Data.CHAT_ID)["URL"]}{command}.json', json=property,
                         timeout=60).json()["result"]

async def uploadToDisk(data:dict = None, bot : Bot = None):
    if 1 > countSQL("users", "ChatID", s_Data.CHAT_ID):
        return None
    file_id = data.get('UF_TASK_WEBDAV_FILES')
    file = await bot.get_file(file_id)

    file_path, file_name = file.file_path.split("/")

    directoryTemp=f"C:/Windows/Temp/{file_path}"

    newNameFile= f"{data.get('TITLE')}{time.time()}{file_name[file_name.rfind('.'):]}"

    directoryTempFile=f"C:/Windows/Temp/{file_path}/{file_name}"

    os.mkdir(directoryTemp)
    await bot.download_file(f"{file_path}/{file_name}", directoryTempFile)
    with open(directoryTempFile, 'rb') as image_file:
        params2 = {
            "id": getSQL("users",["FolderID"],"ChatID",s_Data.CHAT_ID)["FolderID"],
            "data": {"NAME": f"{newNameFile}"},
            "fileContent": [file_name,base64.b64encode(image_file.read()).decode()]
        }
        r = requests.post(f'{getSQL("users",["URL"],"ChatID",s_Data.CHAT_ID)["URL"]}disk.folder.uploadfile.json',json=params2, timeout=60).json()
    shutil.rmtree(directoryTemp)
    return r.get("result").get("ID")

async def writeInBitrix24(data:dict = None, bot : Bot = None):
    params = {"fields":
                  {"TITLE": data.get('TITLE'),
                   "RESPONSIBLE_ID": None,
                   "DESCRIPTION": data.get('DESCRIPTION'),
                   "UF_CRM_TASK": data.get('UF_CRM_TASK'),
                   "DEADLINE": data.get('DEADLINE')
                   }
              }
    if data.get("UF_TASK_WEBDAV_FILES") != None:
        FileID = await uploadToDisk(data,bot)
        params["fields"]["UF_TASK_WEBDAV_FILES"] = [f"n{FileID}"]
    print(params.items())
    for User in data.get("RESPONSIBLE_ID"):
        params["fields"]["RESPONSIBLE_ID"] = User
        print(requests.post(f'{getSQL("users",["URL"],"ChatID",s_Data.CHAT_ID)["URL"]}tasks.task.add.json',json = params, timeout = 60).json())