def kt(n):
    if int(n) < 100 : return 0
    k,l,r,i = len(n),0,0,1
    while n[i] > n[i-1]:
        i += 1
    l = i-1
    i = 0
    while n[k - i - 1] < n[k - i - 2]:
        i += 1
    r = k - i - 1
    if(l == r): return 1
    return 0
t = int(input())
while t > 0 :
    if(kt(input()) == 1): print("YES")
    else : print("NO")
    t-=1