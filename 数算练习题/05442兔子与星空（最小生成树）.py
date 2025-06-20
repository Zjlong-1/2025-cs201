#前置一个十分重要的性质，一个树的边一定是n-1条，这就奠定了贪心的基础，路径要经过的线段数一定，所以最小显然是每一个最小。
#prim算法（稠密图）关注的是点：
#用一个超强的字典集合组合来节省空间
import heapq
n=int(input())
di={chr(i+65):{} for i in range(n)}
for _ in range(n-1):
    l=input().split()
    t=int(l[1])
    for i in range(2,len(l),2):
        di[l[i]][l[0]]=int(l[i+1])
        di[l[0]][l[i]]=int(l[i+1])
use=set()
use.add('A')
h=[]
for to,cost in di['A'].items():
    heapq.heappush(h,(cost,'A',to))
heapq.heapify(h)
ans=0
while h:
    cost,f,t=heapq.heappop(h)
    if t not in use:
        use.add(t)
        ans+=cost
        for t1,cost1 in di[t].items():
            if t1 not in use:
                heapq.heappush(h,(cost1,t,t1))
print(ans)

