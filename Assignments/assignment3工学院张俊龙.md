# Assignment #3: 惊蛰 Mock Exam

Updated 1641 GMT+8 Mar 5, 2025

2025 spring, Complied by <mark>张俊龙，工学院</mark>



> **说明：**
>
> 1. **惊蛰⽉考**：<mark>AC5</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。
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

### E04015: 邮箱验证

strings, http://cs101.openjudge.cn/practice/04015



思路：不厌其烦地把所有非法的判断移除掉



代码：

```python
while True:
    try:
        s=input()
    except EOFError:
        break
    def pan(s):
        if s[0]=='.' or s[0]=='@' or s[-1]=='.' or s[-1]=='@':
            return False
        flag=0
        c=-1
        t=-1
        for i in range(1,len(s)-1):
            if s[i]=='@' and s[i+1]=='.':
                return False
            if s[i]=='@' and s[i-1]=='.':
                return False
            if s[i]=='@' and flag==1:
                return False
            if s[i]=='@':
                flag+=1
                c=i
            if s[i]=='.':
                t=i
        return t>c and flag==1
    if pan(s):
        print('YES')
    else:
        print('NO')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-2.png)



### M02039: 反反复复

implementation, http://cs101.openjudge.cn/practice/02039/



思路：分奇偶，一行一行读取



代码：

```python
m=int(input())
s=input()
n=len(s)//m
t=len(s)
l=[[' ']*m for _ in range(n)]
for i in range(n):
    if i%2==1:
        for j in range(m):
            l[i][m-1-j]=s[i*m+j]
    else:
        for j in range(m):
            l[i][j]=s[i*m+j]
print(''.join(l[i][j] for j in range(m) for i in range(n)))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-3.png)




### M02092: Grandpa is Famous

implementation, http://cs101.openjudge.cn/practice/02092/



思路：用defaultdict统计，再用sort对items()排序即可



代码：

```python
from collections import defaultdict
while True:
    n,m=map(int,input().split())
    if n==m==0:
        break
    di=defaultdict(int)
    for _ in range(n):
        l=list(map(int,input().split()))
        for i in l:
            di[i]+=1
    ans=sorted(di.items(),key=lambda x:(-x[1],x[0]))
    k=ans[1][1]
    for i in range(1,len(ans)):
        if ans[i][1]==k:
            print(ans[i][0],end=' ')
    print()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-4.png)



### M04133: 垃圾炸弹

matrices, http://cs101.openjudge.cn/practice/04133/



思路：
模拟+DP


代码：

```python
l=[[0]*1025 for i in range(1025)]
d=int(input())
for _ in range(int(input())):
    x,y,i=map(int,input().split())
    for k in range(max(x-d,0),min(x+d+1,1025)):
        for j in range(max(y-d,0),min(y+d+1,1025)):
            l[k][j]+=i
t=-1
for i in l:
    for j in i:
        if j>t:
            a=1
            t=j
        elif j==t:
            a+=1
print(str(a)+' '+str(t))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![alt text](image-5.png)


### T02488: A Knight's Journey

backtracking, http://cs101.openjudge.cn/practice/02488/



思路：dfs,将x,y方向互换并且注意一开始走到方向的排序，实际上可以将第一个出去的返回即可



代码：

```python
di = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),(1, -2), (1, 2), (2, -1), (2, 1)]
def can(x, y, n, m, visited):
    return 0 <= x < n and 0 <= y < m and (x, y) not in visited
def solve(n,m):
    all_positions = []
    for i in range(n):
        for j in range(m):
            all_positions.append((i, j))
    for start in all_positions:
        path = [start]
        visited = {start}
        def dfs(x, y):
            if len(path) == n *m:
                return True
            moves = []
            for dx, dy in di:
                nx, ny = x + dx, y + dy
                if can(nx, ny, n, m, visited):
                    moves.append((nx, ny))
            moves.sort(key=lambda x: (chr(x[0] + ord('A')),x[1] + 1))
            for nx, ny in moves:
                visited.add((nx, ny))
                path.append((nx, ny))
                if dfs(nx, ny):
                    return True
                path.pop()
                visited.remove((nx, ny))
            return False

        if dfs(start[0], start[1]):
            return ''.join(f"{chr(x + ord('A'))}{y + 1}" for x, y in path)
    return "impossible"
t = int(input())
for i in range(t):
    m,n = map(int, input().split())
    result = solve(n, m)
    print(f"Scenario #{i+1}:")
    print(result)
    print()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-6.png)



### T06648: Sequence

heap, http://cs101.openjudge.cn/practice/06648/



思路：有两个比较巧妙的点，第一个就是前n行最小的实现要在前两行的基础之上，所以可以转化为2元问题，对于这个2元问题n**2会超时，要用堆来实现，考虑当前状态下未取到的组合的最小即可。



代码：

```python
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
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![alt text](image-7.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

好久没有敲代码了，感觉手感有些下降，每个题都写得不快，最后AC5。最近两天跟进了每日选做，准备刷一下leetcode，并且多写一点oop的题目（感觉还不太熟练）。









