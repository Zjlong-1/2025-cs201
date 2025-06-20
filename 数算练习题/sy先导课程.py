#实际上就是要求没有环
#“能同时学习多门课程时，总是先学习编号最小的课程。导致要用heap

import heapq
n,m=map(int,input().split())
l=[[] for _ in range(n)]
ind=[0]*n
for _ in range(m):
    u,v=map(int,input().split())
    ind[v]+=1
    l[u].append(v)
heap=[i for i in range(n) if ind[i]==0]
heapq.heapify(heap)
ans=[]
while heap:
    t=heapq.heappop(heap)
    ans.append(t)
    for i in l[t]:
        ind[i]-=1
        if ind[i]==0:
            heapq.heappush(heap,i)
if len(ans)==n:
    print('Yes')
    print(*ans)
else:
    print('No')
    print(n-len(ans))