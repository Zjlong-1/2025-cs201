#直接放在一个队列里面显然不合适，因为要用insert从中间插进去，而且要定位插入位置。这是比较难做到的
#所以只能将组放在队里，反正一组的在一起，每次pop都是针对最前面的组
#超级多结合好题
from collections import deque
from collections import defaultdict
t=int(input())
group=defaultdict(int)
for i in range(t):
    l=list(map(int,input().split()))
    for j in l:
        group[j]=i
q=deque()
d=defaultdict(deque)
cnt=t+1
while True:
    s=input().split()
    if s[0]=='STOP':
        break
    elif s[0]=='DEQUEUE':
        print(d[q[0]].popleft())
        if not d[q[0]]:
            q.popleft()
    else:
        x=int(s[1])
        if x not in group:
            group[x]=cnt
            cnt+=1
        if not d[group[x]]:
            q.append(group[x])
        d[group[x]].append(x)




