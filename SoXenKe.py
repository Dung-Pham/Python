def kt(n):
    if len(n) % 2 == 0: return 0
    if n[0] == n[1] : return 0
    for i in range(2,len(n),2):
        if n[i] != n[0]: return 0
    return 1
t = int(input())
while t > 0 :
    if kt(input()) == 1: print("YES")
    else: print("NO")
    t -= 1