from collections import defaultdict
while True:
    n,m=map(int,input().split())
    if n==m==0:
        break
    di=defaultdict(int)
    for _ in range(n):
        l=list(map(int,input().split()))
        for i in l:
            di[i]+=1
    ans=sorted(di.items(),key=lambda x:(-x[1],x[0]))
    k=ans[1][1]
    for i in range(1,len(ans)):
        if ans[i][1]==k:
            print(ans[i][0],end=' ')
    print()
