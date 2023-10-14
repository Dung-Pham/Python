for _ in range(int(input())):
    n=int(input())
    u=float(input())
    v=[float(i) for i in input().split()]
    v.sort()
    for i in range(n-1):
        if(v[i]!=v[i+1]):
            tmp=v[i+1]-v[i]
            if(u<tmp*(i+1)):
                cnt=u/(i+1)
                for j in range(i+1):
                    v[j]+=cnt
                    u-=cnt
                u=0
                break
            else :
                for j in range(i+1):
                    v[j]+=tmp
                    u-=tmp
        if u==0:
            break
    # for i in v:
    #     print(i,end=' ')
    # print(u)
    if u==0:
        sum=1
        for i in v:
            sum*=i
        print('{0:.6f}'.format(sum))
    else:
        sum=1
        tmp=min(v[0]+u/n,1)
        for i in v:
            sum*=tmp
        print('{0:.6f}'.format(sum))