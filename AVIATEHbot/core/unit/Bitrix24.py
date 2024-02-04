import os

from setings import bx24
from aiogram import Bot
import base64


async def writeInBitrix24(data, bot : Bot):
    file_id = data.get('UF_TASK_WEBDAV_FILES')
    print(f"-----------------------{file_id}----------------------")
    file = await bot.get_file(file_id)
    file_path = file.file_path
    print(f"{file_path}")
    # os.mkdir(f"C:/{file_path[:file_path.find('/')]}")
    await bot.download_file(file_path, f"C:/{file_path}")

    file = open(f"C:/{file_path}", 'rb')
    file_content = file.read()
    base64_two = str(base64.b64encode(file_content))
    print(base64_two)
    from io import BytesIO
    from base64 import b64encode

    ...

    with open("C:\\Users\\egord\\Downloads\\загрузка.jpg", "rb") as f:
        content = BytesIO(f.read())
        content.seek(0)
    params = {
        "TITLE": data.get("TITLE"),
        "DESCRIPTION": data.get("DESCRIPTION"),
        "RESPONSIBLE_ID": int(data.get("RESPONSIBLE_ID")[0]),
        "UF_TASK_WEBDAV_FILES": ["n74360"],
    }
    bx24.callMethod("tasks.task.add", fields=params)

    # bx24.callMethod("tasks.task.add", fields=params)

    # bx24.callMethod('tasks.task.add', fields={'TITLE':data.get("TITLE"),'DESCRIPTION':data.get("DESCRIPTION"),'RESPONSIBLE_ID':int(data.get("RESPONSIBLE_ID")[0]),"UF_TASK_WEBDAV_FILES":"C:\\Users\\egord\\Downloads\\загрузка.jpg"})
