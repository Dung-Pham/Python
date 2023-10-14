from math import*
def snt (n):
    if n < 2 : return 0
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0: return 0
    return 1
def phanTichThuaSNT(n):
    ans = "1"
    i, cnt = 2, 0
    while n > 0:
        
        if n % i == 0 : 
            cnt += 1
            n = int(n/i)
        else:
            ans += " * " + str(i) + "^" + str(cnt)
            cnt = 1
            i += 1
        
    
    return ans 
        
t = int(input())
while t > 0:
    print(phanTichThuaSNT(int(input())))
    t-=1