---# Assignment #B: 图为主

Updated 2223 GMT+8 Apr 29, 2025

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

### E07218:献给阿尔吉侬的花束

bfs, http://cs101.openjudge.cn/practice/07218/

思路：老套路，先建立maze并找点，之后bfs



代码：

```python
from collections import deque
t=int(input())
di=[(0,-1),(0,1),(1,0),(-1,0)]
def bfs(start,end):
    q=deque()
    inq=set()
    q.append((start,0))
    inq.add(start)
    while q:
        (x,y),length=q.popleft()
        if (x,y)==end:
            return length
        for dx,dy in di:
            nx,ny=dx+x,dy+y
            if 0<=nx<r and 0<=ny<c and (nx,ny) not in inq and maze[nx][ny]!='#':
                inq.add((nx,ny))
                q.append(((nx,ny,),length+1))
    return 'oop!'
for _ in range(t):
    r, c = map(int, input().split())
    maze = []
    start = end = (0, 0)
    for i in range(r):
        s = list(input())
        for j in range(c):
            if s[j] == 'S':
                start = (i, j)
            elif s[j] == 'E':
                end = (i, j)
        maze.append(s)
    print(bfs(start,end))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image.png)




### M3532.针对图的路径存在性查询I

disjoint set, https://leetcode.cn/problems/path-existence-queries-in-a-graph-i/

思路：有一点像并查集，只不过是手动分类找根



代码：

```python
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        l=[0]*n
        for i in range(1,n):
            if nums[i]-nums[i-1]>maxDiff:
                l[i]=l[i-1]+1
            else:
                l[i]=l[i-1]
        return [l[x]==l[y] for x,y in queries]
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-5.png)



### M22528:厚道的调分方法

binary search, http://cs101.openjudge.cn/practice/22528/

思路：
直接二分，一个一个试


代码：

```python
from math import ceil
l=list(map(float,input().split()))
def can(b):
    a=b/(10**9)
    l1=[a*x+1.1**(a*x) for x in l]
    l1.sort(reverse=True)
    n=len(l1)
    return l1[ceil(n*0.6)-1]>=85
left=0
right=10**9
while left<right:
    mid=(left+right)//2
    if can(mid):
        right=mid
    else:
        left=mid+1
print(left)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-1.png)



### Msy382: 有向图判环 

dfs, https://sunnywhy.com/sfbj/10/3/382

思路：Kahn 拓扑排序，非有向图必有入度为0的点，以此递降



代码：

```python
from collections import deque
n,m=map(int,input().split())
graph=[[] for _ in range(n)]
indeg=[0]*n
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    indeg[v]+=1
q=deque([u for u in range(n) if  indeg[u]==0])
cnt=0
while q:
    u=q.popleft()
    cnt+=1
    for v in graph[u]:
        indeg[v]-=1
        if indeg[v]==0:
            q.append(v)
if cnt!=n:
    print('Yes')
else:
    print('No')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-3.png)



### M05443:兔子与樱花

Dijkstra, http://cs101.openjudge.cn/practice/05443/

思路：定义最小距离以及走最小距离的第一步，之后三重循环维护



代码：

```python
p=int(input())
di={}
name=[None]*p
length=[[float('inf')]*p for _ in range(p)]
nxt=[[None]*p for _ in range(p)]
for i in range(p):
    t=input()
    di[t]=i
    length[i][i]=0
    nxt[i][i]=i
    name[i]=t
q=int(input())
for _ in range(q):
    a,b,c=input().split()
    if length[di[a]][di[b]]>int(c):
        length[di[a]][di[b]]=int(c)
        length[di[b]][di[a]]=int(c)
        nxt[di[a]][di[b]]=di[b]
        nxt[di[b]][di[a]] = di[a]
for k in range(p):
    for i in range(p):
        if length[i][k]==float('inf'):
            continue
        for j in range(p):
            if length[k][j]==float('inf'):
                continue
            x=length[i][k]+length[k][j]
            if x<length[i][j]:
                length[i][j]=x
                nxt[i][j]=nxt[i][k]
r=int(input())
for _ in range(r):
    a,b=input().split()
    u,v=di[a],di[b]
    ans=a
    cur=di[a]
    path=[]
    while u!=v:
        u=nxt[u][v]
        path.append(u)
    for i in path:
        ans+=f'->({length[cur][i]})->{name[i]}'
        cur=i
    print(ans)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![alt text](image-4.png)


### T28050: 骑士周游

dfs, http://cs101.openjudge.cn/practice/28050/

思路：

Warnsdorff 规则,有序的走，走自由度最少的（最容易成功）

代码：

```python
n=int(input())
r,c=map(int,input().split())
di=[(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
l1=[[0]*n for _ in range(n)]
def rule(x,y):
    m=0
    for dx,dy in di:
        nx,ny=dx+x,dy+y
        if 0<=nx<n and 0<=ny<n and l1[nx][ny]==0:
            m+=1
    return m
def dfs(x,y,cnt,l):
    if cnt==n*n:
        return True
    rulel=[]
    for dx,dy in di:
        nx,ny=dx+x,dy+y
        if 0<=nx<n and 0<=ny<n and l[nx][ny]==0:
            rulel.append((rule(nx,ny,),nx,ny))
    rulel.sort()
    for t,nx,ny in rulel:
        l[nx][ny]=1
        if dfs(nx,ny,cnt+1,l):
            return True
        l[nx][ny]=0
    return False
l1[c][r]=1
if dfs(c,r,1,l1):
    print('success')
else:
    print('fail')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-2.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

这次作业学到了许多知识：图的构建，Kahn 拓扑排序，Warnsdorff 规则，以及兔子与樱花建立一个标记走最近路第一步的列表。五一准备打leetcode周赛。









