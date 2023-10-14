a, k, n = map(int, input().split())
b, t = 1, 0
while a + b <= n:
    if (a + b) % k == 0 : 
        print(b, end = ' ')
        t = 1
    b += 1
if t == 0 : print(-1)