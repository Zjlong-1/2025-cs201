# Assignment #D: 图 & 散列表

Updated 2042 GMT+8 May 20, 2025

2025 spring, Complied by <mark>张俊龙，工学院</mark>



> **说明：**
>
> 1. **解题与记录：**
>
>    对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
> 2. **提交安排：**提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
>
> 3. **延迟提交：**如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。 
>
> 请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。



## 1. 题目

### M17975: 用二次探查法建立散列表

http://cs101.openjudge.cn/practice/17975/

<mark>需要用这样接收数据。因为输入数据可能分行了，不是题面描述的形式。OJ上面有的题目是给C++设计的，细节考虑不周全。</mark>

```python
import sys
input = sys.stdin.read
data = input().split()
index = 0
n = int(data[index])
index += 1
m = int(data[index])
index += 1
num_list = [int(i) for i in data[index:index+n]]
```



思路：
这个题目有一个坑点，同一个数据可以多个相同的关键字。其实理解题意才是最难的。


代码：

```python

import sys
input = sys.stdin.read
data = input().split()
index = 0
n = int(data[index])
index += 1
m = int(data[index])
index += 1
num_list = [int(i) for i in data[index:index+n]]
s={}
ans=[]
for i in num_list:
    t=i%m
    cnt=1
    if t not in s or s[t]==i:
        s[t]=i
        ans.append(t)
        continue
    while True:
        if (t+cnt**2)%m not in s:
            s[(t+cnt**2)%m]=i
            ans.append((t+cnt**2)%m)
            break
        elif (t-cnt**2)%m not in s:
            s[(t-cnt**2)%m]=i
            ans.append((t-cnt**2)%m)
            break
        cnt+=1
print(*ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-6.png)



### M01258: Agri-Net

MST, http://cs101.openjudge.cn/practice/01258/

思路：prim最小生成树



代码：

```python
import heapq
while True:
    try:
        n=int(input())
    except EOFError:
        break
    l=[list(map(int,input().split())) for _ in range(n)]
    heap=[(0,0)]
    dist=[float('inf')]*n
    ans=0
    vi=[False]*n
    cnt=0
    while heap and cnt<n:
        w,u=heapq.heappop(heap)
        if vi[u]:
            continue
        ans+=w
        cnt+=1
        vi[u]=True
        for i in range(n):
            if not vi[i] and l[u][i]<dist[i]:
                dist[i]=l[u][i]
                heapq.heappush(heap,(l[u][i],i))
    print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-7.png)



### M3552.网络传送门旅游

bfs, https://leetcode.cn/problems/grid-teleportation-traversal/

思路：其实传送门就是吓人的，实际上就是某些点多了一些路径，只能用一次用一次是显然的毕竟找最短距离，所以一遇到就直接用了（这肯定是最优的）其余的部分就是普通的bfs



代码：

```python
class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        di=defaultdict(list)
        for i in range(n):
            for j in range(m):
                if 64<ord(matrix[i][j])<91:
                    di[matrix[i][j]].append((i,j))
        vi=[[False]*m for _ in range(n)]
        d=[(0,1),(0,-1),(1,0),(-1,0)]
        q=deque([(0,0,0)])
        if matrix[0][0]!='.': 
            for a,b in di[matrix[0][0]]:
                if (a,b)!=(0,0):
                    q.append((a,b,0))
                    vi[a][b]=True
        vi[0][0]=True
        while q:
            x,y,w=q.popleft()
            if (x,y)==(n-1,m-1):
                return w
            for dx,dy in d:
                nx,ny=dx+x,dy+y
                if 0<=nx<n and 0<=ny<m and not vi[nx][ny] and matrix[nx][ny]!='#':
                    if matrix[nx][ny]!='.': 
                            for a,b in di[matrix[nx][ny]]:
                                if (a,b)!=(nx,ny):
                                    q.append((a,b,w+1))
                                    vi[a][b]=True
                    vi[nx][ny]=True
                    q.append((nx,ny,w+1))    
        return -1
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-11.png)



### M787.K站中转内最便宜的航班

Bellman Ford, https://leetcode.cn/problems/cheapest-flights-within-k-stops/

思路：
Dijkstra的变形，好在中转次数是以一为单位增加的，可以类似BFS的想法先按照中转数量出入堆。


代码：

```python
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = [[] for _ in range(n)]
        for i, j, w in flights:
            g[i].append((j, w))
        k += 1
        
        dist = [inf] * n 
        dist[src] = 0
        h = [(0, 0, src)] 
        
        while h:
            time, cost, dx = heappop(h)
            
            for y, w in g[dx]:
                new_dist = time + 1
                new_cost = cost + w
                if new_cost < dist[y] and new_dist <= k:
                    dis[y] = new_cost
                    heappush(h, (new_dist, new_cost, y))

        ans = dist[dst]
        return ans if ans < inf else -1

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-8.png)



### M03424: Candies

Dijkstra, http://cs101.openjudge.cn/practice/03424/

思路：
实际上就是找最短路径（在相邻的边取max）,但是题目有一点没有说清楚，就是1比n小而不是1比n大


代码：

```python
import heapq
n,m=map(int,input().split())
l=[[]for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    l[a].append((b,c))
def d(start,end):
    dist=[float('inf')]*(1+n)
    heap=[(0,start)]
    dist[start]=0
    while heap:
        w,u=heapq.heappop(heap)
        if dist[u]<w:
            continue
        for v,len1 in l[u]:
            if dist[v]>len1+w:
                dist[v]=len1+w
                heapq.heappush(heap,(len1+w,v))
    return dist[end]
print(d(1,n))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-9.png)



### M22508:最小奖金方案

topological order, http://cs101.openjudge.cn/practice/22508/

思路：实际上就是把每一个点的深度相加，dfs



代码：

```python
from functools import lru_cache
n,m=map(int,input().split())
l=[[] for _ in range(n)]
ind=[0]*n
for _ in range(m):
    a,b=map(int,input().split())
    l[a].append(b)
    ind[b]+=1
ans=0
l1=[i for i in range(n) if ind[i]==0]
s=set()
@lru_cache(maxsize=None)
def depth(i):
    global ans
    if i in s:
        return
    s.add(i)
    t=0
    for j in l[i]:
        t=max(depth(j)+1,t)
    ans+=t
    return t

for i in l1:
    depth(i)
print(ans+n*100)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-10.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

这次作业终于做的比较顺手了，全是自己想出来的，最近把每日选做做完了，感觉提升还是挺大的。继续挑战leetcode周赛。









