t = int(input())
while t > 0:
    s = input()
    if(s[0:2] == s[len(s)-2 : len(s)]): print("YES")
    else: print ("NO")
    t -= 1