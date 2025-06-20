#两个根堆
import heapq
t=int(input())
for _ in range(t):
    l=list(map(int,input().split()))
    n=len(l)
    mi=[]
    ma=[]
    ans=[]
    m1,m2=0,0
    for i in range(n):
        if not mi or -mi[0]>=l[i]:
            heapq.heappush(mi,-l[i])
            m1+=1
        else:
            heapq.heappush(ma,l[i])
            m2+=1
        if m2>m1:
            heapq.heappush(mi,-heapq.heappop(ma))
            m1,m2=m1+1,m2-1
        if m1>m2+1:
            m1,m2=m1-1,m2+1
            heapq.heappush(ma, -heapq.heappop(mi))
        if i%2==0:
            ans.append(-mi[0])
    print(len(ans))
    print(*ans)

