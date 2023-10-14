def kt(n):
    a = list(n)
    tong = sum ( map(int , a))
    if tong % 3 == 0: print("YES")
    else: print("NO")
t = int(input())
while t > 0 :
    kt(input())
    t -= 1