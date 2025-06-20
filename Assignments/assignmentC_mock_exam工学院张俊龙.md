# Assignment #C: 202505114 Mock Exam

Updated 1518 GMT+8 May 14, 2025

2025 spring, Complied by <mark>张俊龙，工学院</mark>



> **说明：**
>
> 1. **⽉考**：AC?<mark>（请改为同学的通过数）</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。
>
> 2. **解题与记录：**
>
>    对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
> 3. **提交安排：**提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
>
> 4. **延迟提交：**如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。 
>
> 请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。



## 1. 题目

### E06364: 牛的选举

http://cs101.openjudge.cn/practice/06364/

思路：

排两次

代码：

```python
n,k=map(int,input().split())
l1=[]
for i in range(n):
    a,b=map(int,input().split())
    l1.append((a,b,i+1))
l1.sort(key=lambda x:-x[0])
l1=l1[:k]
l1.sort(key=lambda x:-x[1])
print(l1[0][-1])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-2.png)



### M04077: 出栈序列统计

http://cs101.openjudge.cn/practice/04077/

思路：
dfs


代码：

```python
n=int(input())
cnt=0
def solve(t,stack):
    global cnt
    if t==n+1:
        cnt+=1
        return
    solve(t+1,stack+[t])
    while stack:
        stack.pop()
        solve(t+1,stack+[t])
solve(1,[])
print(cnt)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-3.png)



### M05343:用队列对扑克牌排序

http://cs101.openjudge.cn/practice/05343/

思路：直接排序



代码：

```python
n=int(input())
l=input().split()
di={'A':0,'B':1,'C':2,'D':3}
d={0:'A',1:'B',2:'C',3:'D'}
l1=[[] for _ in range(10)]
l2=[[]for _ in range(4)]
for i in l:
    l1[int(i[1])].append(i)
    l2[di[i[0]]].append(i)
for i in range(1,10):
    print(f'Queue{i}:',end='')
    print(*l1[i])
for i in range(4):
    print(f'Queue{d[i]}:',end='')
    l2[i].sort()
    print(*l2[i])
l.sort()
print(*l)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-5.png)



### M04084: 拓扑排序

http://cs101.openjudge.cn/practice/04084/

思路：入度为零的点放前面



代码：

```python
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
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-4.png)



### M07735:道路

Dijkstra, http://cs101.openjudge.cn/practice/07735/

思路：dijkstra的变形，要去掉dist列表，防止可能的答案被覆盖



代码：

```python
import heapq
k=int(input())
n=int(input())
r=int(input())
l=[[]for _ in range(n+1)]
for _ in range(r):
    s,d,le,t=map(int,input().split())
    l[s].append((d,le,t))
def solve():
    vi = set()
    heap = [(0, 1, 0)]
    while heap:
        len1, u, c = heapq.heappop(heap)
        if u == n:
            return len1
        vi.add((u, c))
        for v, le, t in l[u]:
            if (v,t+c) not in vi and t + c <=k:
                heapq.heappush(heap, (len1+le, v, t+c))
    return -1
print(solve())
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image.png)



### T24637:宝藏二叉树

dp, http://cs101.openjudge.cn/practice/24637/

思路：直接用数组表示二叉树，递归即可



代码：

```python
from functools import lru_cache
n=int(input())
l=list(map(int,input().split()))
@lru_cache(maxsize=None)
def g(i):
    if i>n:
        return 0
    return max(f(2*i),g(2*i))+max(f(2*i+1),g(2*i+1))
@lru_cache(maxsize=None)
def f(i):
    if i>n:
        return 0
    return l[i-1]+g(2*i)+g(2*i+1)
print(max(f(1),g(1)))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-1.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>
本次考试感觉状态不太好，第5题卡了好久，没有想到潜在的路径较长但是花费比较小的怎么储存下来，之后才发现只要去掉dist列表就行了。第6题明显比第5题简单许多，被这个排序搞心态了。期末考试的时候还是要灵活一点，先把会做的做了，不要花太多时间在某一道题上。










