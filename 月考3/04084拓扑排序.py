import heapq
v,a=map(int,input().split())
l=[[] for _ in range(v)]
ind=[0]*v
for _ in range(a):
    x,y=map(int,input().split())
    l[x-1].append(y-1)
    ind[y-1]+=1
heap=[i for i in range(v) if ind[i]==0]
heapq.heapify(heap)
ans=[]
while heap:
    t=heapq.heappop(heap)
    ans.append(f'v{t+1}')
    for i in l[t]:
        ind[i]-=1
        if ind[i]==0:
            heapq.heappush(heap,i)
print(*ans)