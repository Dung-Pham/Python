def hoaThuong(s):
    hoa,thuong = 0, 0
    for i in range(len(s)):
        if s[i].isupper(): hoa += 1
        else: thuong += 1
    if hoa > thuong : print (s.upper())
    else: print ( s.lower())
    
s = input()
hoaThuong(s)