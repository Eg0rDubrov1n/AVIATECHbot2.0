# import calendar
# C = calendar.TextCalendar()
# f = calendar.Calendar()
# print(*f.itermonthdays4(2023,1))
# print(C.formatmonth(2023,1).replace('   ',' _ '))
import datetime

DATA_NOW = datetime.datetime.now()

print(DATA_NOW.month)