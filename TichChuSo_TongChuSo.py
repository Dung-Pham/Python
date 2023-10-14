from functools import *
def tong(n):
    return sum(int(i) for i in n[1::2])
def tich(n):
    if sum(int(i) for i in n[::2]) ==0 : return 0
    return reduce(lambda a,b: int(a)*int(b) if b != '0' else a, n[::2])
t = int(input())
while t > 0 :
    n = input()
    print(f"{tich(n)} {tong(n)}")
    t -= 1