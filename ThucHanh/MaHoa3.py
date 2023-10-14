for t in range(int(input())):
    s = input()
    s1 = s[0:len(s)//2]
    s2 = s[len(s)//2:]
    count = 0
    for i in s1:
        count += (ord(i) - ord('A'))
    s11 = ""
    for i in s1:
        s11 += chr((ord(i) - ord('A') + count)%26 + ord('A'))
    count = 0
    for i in s2:
        count += ord(i) - ord('A')
    s12 = ""
    for i in s2:
        s12 += chr((ord(i) - ord('A') + count)%26 + ord('A'))
    kq = ""
    for i in range(len(s12)):
        kq += chr((ord(s11[i]) - ord('A')  +  ord(s12[i]) - ord('A'))%26 + ord('A'))
    print(kq)