import re
t = int(input())
while t > 0 :
    a = map(int, re.findall(r'\d+', input()))
    print(max(a))
    t -= 1