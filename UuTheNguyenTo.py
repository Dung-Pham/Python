from math import*
s = '2357'
def snt(n):
    if n < 2 : return False
    return all( n % i != 0 for i in range(2,int(sqrt(n)) + 1))
def kt(n):
    global s 
    if not snt(len(n)): return False
    a = sum(1 for i in n if s.find(i) != -1 )
    b = sum(1 for i in n if s.find(i) == -1 ) 
    return a > b
t = int(input())
while t > 0 :
    if kt(input()): print("YES")
    else : print("NO")
    t -= 1