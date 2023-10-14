
t = int(input())
while t > 0 :
    b = int(input())
    n = input()
    if b == 2 : print(n)
    elif b == 16: print(hex(int(n,2))[2:])
    elif b == 4 or b == 8: print(oct(int(n,2))[2:])
    else : print(int(n,2))
    t -= 1