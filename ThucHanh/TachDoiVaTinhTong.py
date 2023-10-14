def tach(n):
    l = len(n)
    ans =  int(n[0:int(l/2) ]) + int(n[int(l/2) :l])
    print(ans)
    l = len(str(ans))
    while l > 1:
        ans = int(str(ans)[0:int(l/2)]) + int(str(ans)[int(l/2) :l])
        l = len(str(ans))
        print(ans)

n = input()
tach(n)
