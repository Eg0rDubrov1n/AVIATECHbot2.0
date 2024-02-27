from core.unit.state import s_Data
from setings import Connect


def countSQL(your_table_name,object_id,your_object_id):
    connect = Connect()
    with connect.cursor() as cursor:
        sqlCommand = f"SELECT COUNT(*) FROM {your_table_name} WHERE {object_id} = {your_object_id}"
        # print("-->",sqlCommand)
        cursor.execute(sqlCommand)
        return cursor.fetchall()[0]["COUNT(*)"]
def setSQL(your_table_name,isstr_queryKey,isstr_queryValues):
    connect = Connect()
    with connect.cursor() as cursor:
        # print(countSQL(your_table_name,"ChatID",s_Data.CHAT_ID))
        if countSQL(your_table_name,"ChatID",s_Data.CHAT_ID) > 0:
            sqlCommand = f"UPDATE `{your_table_name}` SET `{isstr_queryKey}` = '{isstr_queryValues}' WHERE ChatID='{s_Data.CHAT_ID}';"
        else:
            sqlCommand = (f"INSERT INTO `{your_table_name}` (`ChatID`,`{isstr_queryKey}`) VALUES ('{s_Data.CHAT_ID}','{isstr_queryValues}');")
        # print(sqlCommand)
        cursor.execute(sqlCommand)
        connect.commit()
def getSQL(table: str, elements: object, whereKey: str = None, whereItem: str = None) -> object:
    connect = Connect()
    with connect.cursor() as cursor:
        sqlCommand = f"SELECT  {','.join(elements)} FROM `{table}`"
        if whereKey != None:
            sqlCommand += f" WHERE {whereKey} = {whereItem}"
        # print("getSQL-->",sqlCommand)
        cursor.execute(sqlCommand)
        return cursor.fetchall()[0]

def getSQLOneCommand(sqlCommand: str):
    connect = Connect()
    with connect.cursor() as cursor:
        cursor.execute(sqlCommand)
        return cursor.fetchall()[0][sqlCommand[7:]]

def getSQLID(table: str):
    connect = Connect()
    with connect.cursor() as cursor:
        idRequest = f"SELECT AUTO_INCREMENT FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '{table}';"
        cursor.execute(idRequest)
        return cursor.fetchall()[0]["AUTO_INCREMENT"]