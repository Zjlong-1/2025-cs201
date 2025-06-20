l,m=map(int,input().split())
tr=[]
for _ in range(m):
    tr.append(tuple(map(int,input().split())))
tr.sort()
cur=tr[0][1]
ans=tr[0][1]-tr[0][0]+1
for a,b in tr[1:]:
    if a>cur:
        cur=b
        ans+=b-a+1
    elif cur<b:
        ans+=b-cur
        cur=b
print(l+1-ans)