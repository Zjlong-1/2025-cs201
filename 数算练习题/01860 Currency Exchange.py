#这个题目有点小难
n,m,s,v=input().split()
n,m,s=int(n),int(m),int(s)
v=float(v)
edges=[]
for _ in range(m):
    a,b,ab1,ab2,ba1,ba2=map(float,input().split())
    a,b=int(a),int(b)
    edges.append((a,b,ab1,ab2))
    edges.append((b,a,ba1,ba2))
def solve():
    l = [0.0] * (n + 1)
    l[s] = v
    for _ in range(n - 1):
        flag = False
        for a, b, ab1, ab2 in edges:
            if (l[a] - ab2) * ab1 > l[b]:
                l[b] = (l[a] - ab2) * ab1
                flag = True
        if not flag:
            return False
    for a, b, ab1, ab2 in edges:
        if (l[a] - ab2) * ab1 > l[b]:
            return True
    return False
if solve():
    print('YES')
else:
    print('NO')

