from math import*
def snt(n):
    if n < 2 : return 0
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0 : return 0
    return 1
t = int(input())
while t > 0 :
    s = input()
    l = len(s)
    if (snt(int(s[l-4: l])) == 1): print("YES")
    else : print("NO")
    t-=1
