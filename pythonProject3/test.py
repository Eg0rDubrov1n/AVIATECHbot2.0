import base64

file = open("C:\\Users\\egord\\Downloads\\загрузка.jpg", 'rb')
file_content = file.read()
base64_two = str(base64.b64encode(file_content))
print("_________________")
print(base64_two)
print(type(base64_two))
print("_________________")
import requestsurl = 'https://your_domain.bitrix24.ru/rest/crm.deal.get.json'
params = { 'id': 123, 'auth': 'your_access_token',}response = requests.post(url, json=params)print(response.json())
