p ="ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
def maHoa2(s,k):
    global p
    ans = ""
    for i in range(0,len(s)):
        ans += p[(p.index(s[i])+k)%28]
    ans = ans[::-1]
    return ans 

while 1>0:
    x =input()
    if x == "0": break
    k, s = x.split()
    print(maHoa2(s,int(k)))