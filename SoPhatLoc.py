t = int(input())
while t > 0 :
    n = input()
    if n[len(n)-2: len(n)] == "86" : print("YES")
    else: print("NO")
    t-=1