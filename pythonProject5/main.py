# def f(arr,x,y,c,n,m):
#     if x == (n - 1) and c == 'b':
#         # print(x, y)
#         return 1
#     elif x == 0 and c == 'w':
#         # print(x, y)
#         return 1
#     # print(x, y)
#     if x + 2 < n and y + 2 < m and (arr[x+1][y+1] != c) and (arr[x+1][y+1] != ".") and (arr[x+2][y+2] == "."):
#         arr1 = arr
#         arr1[x + 1][y + 1] = '.'
#         t = f(arr1, x + 2, y + 2, c, n, m)
#         if t != 0:
#             # print(x, y)
#             return (x, y)
#     if x - 2 >= 0 and y - 2 >= 0 and (arr[x-1][y-1] != c) and (arr[x-1][y-1] != ".") and (arr[x-2][y-2] == "."):
#         arr1 = arr
#         arr1[x - 1][y - 1] = '.'
#         t = f(arr1, x - 2, y - 2, c, n, m)
#         if t != 0:
#             # print(x, y)
#             return (x, y)
#     if x + 2 < n and y - 2 >= 0 and (arr[x+1][y-1] != c) and (arr[x+1][y-1] != ".") and (arr[x+2][y-2] == "."):
#         arr1 = arr
#         arr1[x + 1][y - 1] = '.'
#         t = f(arr1, x + 2, y - 2, c, n, m)
#         if t != 0:
#             # print(x, y)
#             return (x, y)
#     if x - 2 >= 0 and y + 2 < m and (arr[x-1][y+1] != c) and (arr[x-1][y+1] != ".") and (arr[x-2][y+2] == "."):
#         arr1 = arr
#         arr1[x - 1][y + 1] = '.'
#         t = f(arr1, x - 2, y + 2, c, n, m)
#         if t != 0:
#             # print(x, y)
#             return (x, y)
#     return 0
#
#
# def main():
#     n, m, c = input().split()
#     n = int(n)
#     m = int(m)
#     arr = list()
#     for i in range(n):
#         arr.append(list(input()))
#     for i in range(n) if c == 'w' else range(n - 1,-1,-1):
#         j = 0
#         x = ''.join(arr[i]).find(c.upper(), j)
#         while x > 0:
#             if c == 'b' and (i + 1) == (n - 1) and (arr[i + 1][x + 1] == '.' or arr[i + 1][x - 1] == '.'):
#                 # print(f"BBB-------->{(i,x)}")
#                 return (i,x)
#             if c == 'w' and (i - 1) == (0) and (arr[i - 1][x + 1] == '.' or arr[i - 1][x - 1] == '.'):
#                 # print(f"WWW-------->{(i,x)}")
#                 return (i,x)
#             ddr = f(arr, i, x, c, n, m)
#             # print(f"--------->{ddr}<-------------")
#             if ddr != 0:
#                 return ddr
#             j=x + 1
#             x = ''.join(arr[i]).find(c.upper(), j)
#
# for i in range(int(input())):
#     xxx = main()
#     if xxx != None:
#         print(xxx[0]+1,xxx[1]+1)
#     else :
#         print(-1,-1)
params2 = {"fields":
               {"TITLE": "TTTT",
                "RESPONSIBLE_ID": ["1"]

                }
           }
}
# a = json.JSONEncoder()
# b = a.encode(d)
# print(b)
r = requests.post('https://eurotechpromg.bitrix24.ru/rest/308/2gnr740m6pfywjof/tasks.task.add.json',
json =, timeout = 60).json()
print(r)