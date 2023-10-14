from math import *
def chanLe(n):
    return all((i % 2 == 0 and int(a) %2 == 0) or (i % 2 != 0 and int(a) % 2 != 0) for i,a in enumerate(n))
def tong(n):
    return sum(int(i) for i in n)
def snt(n):
    if n < 2 : return False
    for i in range(2,int(sqrt(n)) + 1):
        if n % i == 0 : return False
    return True
t = int(input())
while t > 0 :
    n = input()
    if chanLe(n) and snt(tong(n)): print("YES")
    else: print("NO")
    t -= 1
