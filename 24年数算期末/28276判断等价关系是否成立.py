di={}
n=int(input())
l=[input() for _ in range(n)]
s=set()
for i in l:
    s.add(i[0])
    s.add(i[-1])
def f(x):
    if x!=di[x]:
        di[x]=f(di[x])
    return di[x]
for i in s:
    di[i]=i
l2=[]
for i in l:
    if i[1]=='!':
        l2.append(i)
    else:
        a,b=i[0],i[-1]
        x,y=f(a),f(b)
        if x!=y:
            di[x]=di[y]
ans=True
for i in l2:
    a, b = i[0], i[-1]
    x, y = f(a), f(b)
    if x == y:
        ans=False
print(ans)

