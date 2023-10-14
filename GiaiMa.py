def giaiMa(s):
    ans =""
    for i in range(0, len(s) , 2):
        t= int(s[i+1])
        while t > 0:
            ans += s[i]
            t -= 1
    return ans
t = int(input())
while t > 0:
    s = input()
    print(giaiMa(s))
    t -= 1