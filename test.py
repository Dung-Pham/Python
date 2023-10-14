from math import *
def soChuSo(n):
    count = len(str(n))
    return count
def lamTron (n):
    c = soChuSo(n) - 1
    while n > 9:
        n /= 10
        if (len(str(round(n))) - len(str((int)(n))) == 1): return round(n) * 10**(c)
        if ((n - (int)(n) == 0.5) and (int(n) % 2 == 0)) :
            n = ceil(n)
        else: n = round(n)
    return n*(10**c)

t = int(input())
while t > 0:
    n = int(input())
    print(lamTron(n), end ='\n')
    t -= 1