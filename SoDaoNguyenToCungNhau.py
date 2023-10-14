from math import*
def kt(n):
    m = int(str(n)[::-1])
    if(gcd(m,n) != 1): return 0
    return 1
t = int(input())
while t > 0:
    n = int(input())
    if kt(n) == 1 : print("YES")
    else: print("NO")
    t-=1
