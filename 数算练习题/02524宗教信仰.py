t=0
while True:
    n,m=map(int,input().split())
    t+=1
    if n==m==0:
        break
    l=[i for i in range(n+1)]
    def find(x):
        if l[x]!=x:
            l[x]=find(l[x])
        return l[x]
    for _ in range(m):
        x,y=map(int,input().split())
        x1,y1=find(x),find(y)
        if x1!=y1:
            l[x1]=y1
    ans=0
    ins=set()
    for i in range(1, 1 + n):
        if find(i) not in ins:
            ans += 1
            ins.add(find(i))
    print(f'Case {t}: {ans}')