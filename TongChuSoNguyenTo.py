from math import*
def snt(n):
    if n < 2 : return 0
    for i in range(2,int(sqrt(n)) +1):
        if n % i == 0 : return 0
    return 1
def kt(n):
    global s 
    a = list(n)
    tong = sum(int(i)  for i in a )
    if snt(tong) == 1 : print("YES")
    else : print("NO")
    
t = int(input())
while t > 0 :
    kt(input())
    t -= 1