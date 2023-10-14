def tinhTongPhanThuc(n):
    ans = 0
    if n % 2 != 0 :
        for i in range (1,n+1,2):
            ans += 1/i
    else: 
        for i in range(2,n+1,2):
            ans += 1/i
    return ans
t = int(input())
while t > 0 :
    n = int(input())
    print('{:.6f}'.format(tinhTongPhanThuc(n)))
    t-=1