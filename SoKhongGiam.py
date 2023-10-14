def soKGiam(n):
    for i in range(1,len(n)) :
        if n[i] < n[i-1]: return 0
    
    return 1
t = int(input())
while t > 0 : 
    n = input()
    if(soKGiam(n) == 1): print("YES")
    else: print("NO")
    t -= 1