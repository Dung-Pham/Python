from math import *
def soChuSo(n):
    count = len(str(n))
    return count
def lamTron (n):
    c = soChuSo(n) - 1
    t = 0
    while n > 9 and t == 0:
        n /= 10
        x = len(str(int(n)))
        if (n % 1 == 0.5) and (int(n) % 2 == 0) :
            n = ceil(n)
        else: n = round(n)
        if(len(str(n)) != x): return 10**(c+1)
    return n*(10**c)

t = int(input())
while t > 0:
    n = int(input())
    print(lamTron(n))
    t -= 1 