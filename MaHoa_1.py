def maHoa1(s):
    ans = ""
    n = 1
    dif = s[0]
    for  i in range(1, len(s)):
        if s[i] != s[i-1]: 
            ans += str(n) + dif
            dif = s[i]
            n = 1
        else: n+=1
    ans += str(n) + s[len(s) - 1] 
    return ans

t = int(input())
while t > 0:
    print(maHoa1(input()))
    t -= 1