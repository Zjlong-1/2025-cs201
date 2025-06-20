from collections import defaultdict
from collections import deque
n=int(input())
di=defaultdict(list)
road=defaultdict(list)
for _ in range(n):
    s=input()
    for i in range(4):
        t=s[:i]+'-'+s[i+1:]
        di[t].append(s)
for i in di.values():
    for x in range(len(i)):
        for y in range(x+1,len(i)):
            a,b=i[x],i[y]
            road[a].append(b)
            road[b].append(a)
start,end=input().split()
q=deque()
q.append((start,[start]))
inq=set()
inq.add(start)
def solve():
    while q:
        x,way=q.popleft()
        if x==end:
            return way
        for i in road[x]:
            if i not in inq:
                q.append((i,way+[i]))
                inq.add(i)
    return False
k=solve()
if k:
    print(*k)
else:
    print('NO')




