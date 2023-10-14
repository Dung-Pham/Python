def demSo(n,s):
    k = 0
    cnt = 0
    while n.find(s,k) != -1:
        cnt+=1
        k= n.find(s,k) + len(s)
    return cnt
t = int(input())
while t > 0:
    n = input()
    s = input()
    print(demSo(n,s))
    t -= 1