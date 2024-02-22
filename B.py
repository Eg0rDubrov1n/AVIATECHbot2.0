def Nesovpadayet(s,t):
    j = 0
    arrN = list()
    arrNZ = list()
    for i in range(len(s)):
        if j < len(t) and s[i] == t[j]:
            j+=1
        else:
            arrNZ.append(s[i])
            arrN.append(i)
    return arrN, arrNZ

def f(s,t):
    for i in t:
        if not(i in s):
            return 1
    return 0
def main():
    s = input()
    t = input()
    if f(s,t):
        return 0
    b = True
    arrN,arrNz = Nesovpadayet(s,t)
    for i in range(len(arrN)):
        if (arrN[i] - 1 > -1 and (arrNz[i] == s[arrN[i] - 1])) and ((arrN[i] + 1) < len(s) and (arrNz[i] == s[arrN[i] + 1])):
            b = False
        elif ((arrN[i] + 1) % 2 != 0 and
                b and
                not(arrN[i] - 1 > -1 and (arrNz[i] == s[arrN[i] - 1])) and
                not ((arrN[i] + 1) < len(s) and (arrNz[i] == s[arrN[i] + 1]))):
            return 0
        elif (arrN[i] + 1) % 2 == 0:
            b = False
    return 1

print(["NO","YES"][main()])
