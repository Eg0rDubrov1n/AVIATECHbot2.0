
# A---------------------------------------------
# def MaxI(arr):
#     max = -1
#     maxi = -1
#     for i in range(n - 1):
#         if abs(arr[i] - arr[i + 1]) > max:
#             max = abs(arr[i] - arr[i + 1])
#             maxi = i
#     return max,maxi
#
#
# def MediumZnach(arr,i):
#     if (i + 2) < n:
#         return (arr[i] + arr[i+2]) / 2
#     else:
#         return arr[i]
#
# n = int(input())
# arr = list(map(int, input().split()))
# max,maxi = MaxI(arr)
# NewZnac = round(MediumZnach(arr,maxi))
# arr[maxi + 1] = NewZnac
# print(MaxI(arr)[0], maxi + 2, NewZnac)
# A---------------------------------------------
# B---------------------------------------------

def Nesovpadayet(arr,s,t):
    j = 0
    arrN = list()
    for i in range(len(s)):
        if j < len(t) and s[i] == t[j]:
            j+=1
        else:
            arrN.append(i)
    return arrN


def main():
    s = input()
    t = input()
    k = 0
    arr = list()
    arrN = Nesovpadayet(arr,s,t)
    for i in range(len(arrN)):
        if (arrN[i] + 1) % 2 != 0 and k % 2 == 0:
            return 0
        k += 1
    return 1

print(["NO","YES"][main()])
