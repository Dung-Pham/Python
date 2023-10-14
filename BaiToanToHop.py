from itertools import combinations

n, k = map(int, input().split())
a = list(set(map(int, input().split())))
a.sort()
toHop = list(combinations(a,k))
toHop.sort()
for i in toHop: print(' '.join(map(str,i)))
