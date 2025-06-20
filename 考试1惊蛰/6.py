#带一点数学推理，前面出现的小的不管，当前最小的可能只要在这个方向二维位置加入堆
#有一种线性规划的感觉
import heapq
t=int(input())
for _ in range(t):
    m,n=map(int,input().split())
    l=[]
    for _ in range(m):
        k=list(map(int,input().split()))
        k.sort()
        l.append(k)
    l1=l[0]
    def merge(l2,l3):
        heap=[]
        ret=[]
        vi=set()
        heapq.heappush(heap,(l2[0]+l3[0],0,0))
        vi.add((0,0))
        while len(ret)<n:
            a,b,c=heapq.heappop(heap)
            ret.append(a)
            if b+1<n and (b+1,c) not in vi:
                vi.add((b+1,c))
                heapq.heappush(heap,(l2[b+1]+l3[c],b+1,c))
            if c+1<n and (b,1+c) not in vi:
                vi.add((b,1+c))
                heapq.heappush(heap,(l2[b]+l3[c+1],b,c+1))
        return ret
    for i in range(1,m):
        l1=merge(l1,l[i])
    print(*l1)







