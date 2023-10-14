def tinhNam(n,x,m):
    sum = n
    cnt = 0
    while sum < m:
        sum += sum * x / 100 
        cnt += 1
    return cnt
t = int(input())
while t > 0 :
    n, x, m = map ( float , input().split())
    print(tinhNam(n,x,m))
    t-=1