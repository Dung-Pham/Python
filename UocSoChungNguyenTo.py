from math import *
def snt(n):
    if n < 2: return 0
    for i in range(2,int( sqrt(n)+1)):
        if n % i == 0: return 0
    return 1
def kt(n):
    sum = 0
    for i in range(len(str(n))):
        sum += int(str(n)[i])
    if snt(sum) == 1 : print("YES")
    else: print("NO")
t = int(input())
while t > 0 :
    a, b = map(int, input().split())
    kt(gcd(a,b))
    t -= 1