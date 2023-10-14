def kt (n) :
    a = list(n)
    tong = sum(int(i) for i in a)
    if len(str(tong)) <= 1 : return 0
    if str(tong) != str(tong)[::-1] : return 0
    return 1
t = int(input())
while t > 0 :
    if kt(input()) == 1 : print("YES")
    else : print("NO")
    t -= 1