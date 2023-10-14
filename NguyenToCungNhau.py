from math import*
def kt(n,m):
    if gcd(n,m) != 1 : return 0
    return 1
n, k = map(int, input().split())
cnt = 1
for i in range(10**(k-1),10**(k)):
    if kt(i,n) == 1:
        print(i, end = ' ')
        cnt += 1
    if cnt > 10 : 
        print()
        cnt = 1
    