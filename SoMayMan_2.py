def kt (n):
    for i in range(len(n)):
        if n[i] != '4' and n[i] != '7': return 0
    return 1
    
t = int(input())
while t > 0 :
    n = input()
    if kt (n) == 1: print("YES")
    else: print("NO")
    t -= 1

