t=int(input())
for _ in range(t):
    m,n=map(int,input().split())
    l=[]
    for _ in range(m):
        k=list(map(int,input().split()))
        k.sort()
        l.append(k)