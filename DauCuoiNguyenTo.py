from math import*
def snt(n):
    if n < 2 : return False
    return all( n % i != 0 for i in range(2,int(sqrt(n)) + 1))
def kt(n):
    if snt(int(n[:3])) and snt(int(n[len(n)-3:])) : print("YES")
    else : print("NO")
t = int(input())
while t > 0 :
    kt(input())
    t -= 1