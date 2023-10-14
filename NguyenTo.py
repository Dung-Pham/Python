from math import *
def kt (n):
    if n < 2: return 0
    for i in range(2,isqrt(n)+1):
        if n % i == 0: return 0
    return 1
t = int(input())
while t>0:
    n = int(input())
    k = 0
    for i in range(1, n):
        if gcd(i,n) == 1 : k+=1
    if kt(k) == 1 : print("YES")
    else: print("NO")
    t-=1