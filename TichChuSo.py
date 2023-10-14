from functools import*
def tich(n):
    a = filter(lambda x: x != 0, map(int, list(n)))
    tich = reduce(lambda x, y : x * y, a, 1)
    return tich
t = int(input())
while t > 0:
    print(tich(input()))
    t -= 1