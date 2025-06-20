t=int(input())
def d(x1,x2):
    return (x1[0]-x2[0])**2+(x1[1]-x2[1])**2
for _ in range(t):
    n=int(input())
    l=[]
    for i in range(n):
        x, y = map(int, input().split())
        l.append((x,y))
    ans=float('inf')
    for i in range(n):
        for j in range(i+1,n):
            k=d(l[i],l[j])
            ans=min(ans,k)
    print(ans)