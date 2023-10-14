def kt(n):
    t, k = 1000, 0
    sum = n
    while t >= 0 and sum % 7 != 0:
        sum += int(str(sum)[::-1])
    if sum % 7 == 0: k = 1
    if k == 0: return -1
    return sum
t = int(input())
while t > 0 :
    print(kt(int(input())))
    t-=1