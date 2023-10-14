def demXau(s,x):
    cnt = 0
    i = s.find(x,0)
    while i != -1:
        cnt+=1
        i = s.find(x,i+len(x))
    return cnt
t = int(input())
while t > 0 :
    s = input()
    x = input()
    print(demXau(s,x))
    t-=1