def kt (n):
    m = n[::-1]
    for i in range(1,len(n)):
        if abs(ord(n[i]) - ord(n[i-1])) != abs(ord(m[i]) - ord(m[i-1])): return False
    return True
t = int(input())
while t > 0 :
    if kt(input()) : print("YES")
    else : print("NO")
    t -= 1