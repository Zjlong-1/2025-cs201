p=int(input())
di={}
name=[None]*p
length=[[float('inf')]*p for _ in range(p)]
nxt=[[None]*p for _ in range(p)]
for i in range(p):
    t=input()
    di[t]=i
    length[i][i]=0
    nxt[i][i]=i
    name[i]=t
q=int(input())
for _ in range(q):
    a,b,c=input().split()
    if length[di[a]][di[b]]>int(c):
        length[di[a]][di[b]]=int(c)
        length[di[b]][di[a]]=int(c)
        nxt[di[a]][di[b]]=di[b]
        nxt[di[b]][di[a]] = di[a]
for k in range(p):
    for i in range(p):
        if length[i][k]==float('inf'):
            continue
        for j in range(p):
            if length[k][j]==float('inf'):
                continue
            x=length[i][k]+length[k][j]
            if x<length[i][j]:
                length[i][j]=x
                nxt[i][j]=nxt[i][k]
r=int(input())
for _ in range(r):
    a,b=input().split()
    u,v=di[a],di[b]
    ans=a
    cur=di[a]
    path=[]
    while u!=v:
        u=nxt[u][v]
        path.append(u)
    for i in path:
        ans+=f'->({length[cur][i]})->{name[i]}'
        cur=i
    print(ans)

