def kt(n):
    for i in range(3,len(str(n)),2):
        if n[i-1] != n[0] or n[i] != n[1] : return 0
    return 1
t = int(input())
while t > 0 :
    if(kt(input()) == 1): print("YES")
    else: print("NO")
    t-=1
    