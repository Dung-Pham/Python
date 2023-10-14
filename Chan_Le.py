def chanLe(n):
    sum = int(n[0])
    for i in range(1, len(n)):
        if abs(int(n[i]) - int(n[i-1])) != 2: return 0
        sum += int(n[i])
    if sum % 10 != 0: return 0
    return 1
t = int(input())
while t > 0 :
    n = input()
    if(chanLe(n) == 1): print("YES")
    else: print("NO")
    t -= 1