from setings import Connect


def getSQL(table: str, elements: object, whereKey: str = None, whereItem: str = None) -> object:
    connect = Connect()
    with connect.cursor() as cursor:
        sqlCommand = f"SELECT  {','.join(elements)} FROM `{table}`"
        if whereKey != None:
            sqlCommand += f" WHERE {whereKey} = {whereItem}"
        cursor.execute(sqlCommand)
        return cursor.fetchall()

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