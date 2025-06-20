while True:
    try:
        n,m=map(int,input().split())
    except EOFError:
        break
    l=[i for i in range(n+1)]
    def f(x):
        if x!=l[x]:
            l[x]=f(l[x])
        return l[x]
    for _ in range(m):
        x,y=map(int,input().split())
        x1,y1=f(x),f(y)
        if x1==y1:
            print('Yes')
        else:
            l[y1]=x1
            print('No')
    s={f(i) for i in range(1,n+1)}
    print(len(s))
    print(*sorted(s))