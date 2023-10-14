from math import *
s = '2357'
def snt(n):
    if n < 2 : return False
    return all(n % i != 0 for i in range(2,int(sqrt(n))+1))
def kt(n):
    global s
    return all((s.find(v) != -1 and snt(i) == True) or (s.find(v) == -1 and snt(i) == False) for i,v in enumerate(n))
t = int(input())
while t > 0 :
    if kt(input()) == 1 : print("YES")
    else : print("NO")
    t -= 1