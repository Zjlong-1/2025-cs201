# Assignment #7: 20250402 Mock Exam

Updated 1624 GMT+8 Apr 2, 2025

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

### E05344:最后的最后

http://cs101.openjudge.cn/practice/05344/



思路：直接用双端队列模拟，但是注意最后一个数不要打印出来。



代码：

```python
from collections import deque
n,k=map(int,input().split())
q=deque()
for i in range(1,n+1):
    q.append(i)
cnt=0
ans=[]
while q:
    t=q.popleft()
    cnt+=1
    if cnt==k:
        ans.append(t)
        cnt=0
        continue
    q.append(t)
for i in range(n-1):
    print(ans[i],end=' ')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image.png)



### M02774: 木材加工

binary search, http://cs101.openjudge.cn/practice/02774/



思路：
二分，对于每个长度依次判断。


代码：

```python
n,k=map(int,input().split())
l=[int(input()) for _ in range(n)]
right=sum(l)//k
left=0
def can(x):
    cnt=0
    for i in l:
        cnt+=i//x
    return cnt>=k
mid=0
if sum(l)<k:
    print(0)
else:
    while left < right:
        mid = (left + right + 1) // 2
        if can(mid):
            left = mid
        else:
            right = mid - 1
    print(left)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-1.png)




### M07161:森林的带度数层次序列存储

tree, http://cs101.openjudge.cn/practice/07161/



思路：
构建树+dfs


代码：

```python
from collections import deque
class TreeNode:
    def __init__(self,name):
        self.name=name
        self.l=[]
def hou(root):
    if root is None:
        return
    for i in root.l:
        hou(i)
    print(root.name,end=' ')
n=int(input())
for _ in range(n):
    s=input().split()
    q=deque()
    root=TreeNode(s[0])
    q.append((root,int(s[1])))
    idx=2
    while q and idx<len(s):
        r,x=q.popleft()
        for i in range(x):
            childn,childl=s[idx],int(s[idx+1])
            child=TreeNode(childn)
            r.l.append(child)
            q.append((child,childl))
            idx+=2
    hou(root)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-2.png)




### M18156:寻找离目标数最近的两数之和

two pointers, http://cs101.openjudge.cn/practice/18156/



思路：双指针，首位各一个



代码：

```python
def solve():
    t = int(input())
    l = list(map(int, input().split()))
    l.sort()
    n = len(l)
    left = 0
    right = n - 1
    ans = -1
    while left < right:
        mid = l[left] + l[right]
        if abs(t - mid) < abs(t - ans):
            ans = mid
        elif abs(t - mid) == abs(t - ans):
            ans = min(ans, mid)
        if mid < t:
            left += 1
        elif mid==t:
            print(t)
            return
        else:
            right -= 1
    print(ans)
solve()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-3.png)




### M18159:个位为 1 的质数个数

sieve, http://cs101.openjudge.cn/practice/18159/



思路：提前素数筛



代码：

```python
l=[]
def p(x):
    l1=[True]*(x+1)
    for j in range(2,x+1):
        if l1[j] and j%10==1:
            l.append(j)
        for k in range(j*j,x+1,j):
            l1[k]=False
p(10001)
t=int(input())
for i in range(1,1+t):
    n=int(input())
    print(f'Case{i}:')
    if l[0]>=n:
        print('NULL')

    else:
        for k in l:
            if k<n:
                print(k,end=' ')
        print()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-4.png)



### M28127:北大夺冠

hash table, http://cs101.openjudge.cn/practice/28127/



思路：
字典统计


代码：

```python
m=int(input())
di1={}
di2={}
for _ in range(m):
    a,b,c=input().split(',')
    if a not in di1:
        if c=='yes':
            di1[a]=(1,1,a)
            di2[a]=set()
            di2[a].add(b)
        else:
            di1[a]=(0,1,a)
            di2[a] = set()
    else:
        if c=='yes' and b not in di2[a]:
            di1[a]=(di1[a][0]+1,di1[a][1]+1,a)
            di2[a].add(b)
        elif c=='yes':
            di1[a] = (di1[a][0] , di1[a][1] + 1, a)
        else:
            di1[a]=(di1[a][0], di1[a][1] + 1, a)
l=sorted(di1.values(),key=lambda x:(-x[0],x[1],x[2]))
if len(l)<12:
    for i in range(len(l)):
        print(f'{i+1} {l[i][2]} {l[i][0]} {l[i][1]}')
else:
    for i in range(12):
        print(f'{i+1} {l[i][2]} {l[i][0]} {l[i][1]}')
```



代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![alt text](image-5.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

这次考试有点简单，没有tough题，最近在写哈夫曼编码和二叉树的题目。









