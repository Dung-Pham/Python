from math import *
def snt(n):
    if n < 2: return 0
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0 : return 0
    return 1 
s = '2357'
def kt(n):
    global s
    if(snt(len(n)) == 0): return 0
    cnt = 0
    for i in range(len(n)):
        if s.find(n[i]) != -1 : 
            cnt +=1
    if(cnt <= len(n)//2): return 0
    return 1
        
t = int(input())
while t > 0 :
    if kt(input()) == 1: print("YES")
    else : print("NO")
    t -= 1