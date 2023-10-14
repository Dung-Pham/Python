def kt (n):
    sum = 0
    for i in range(len(n)):
        if n[i] == '4' or n[i] == '7': sum += 1
    if sum == 4 or sum == 7: return 1
    return 0
    
n = input()
if kt (n) == 1: print("YES")
else: print("NO")

