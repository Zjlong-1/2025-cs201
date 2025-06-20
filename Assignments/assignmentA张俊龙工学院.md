# Assignment #A: Graph starts

Updated 1830 GMT+8 Apr 22, 2025

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

### M19943:图的拉普拉斯矩阵

OOP, implementation, http://cs101.openjudge.cn/practice/19943/

要求创建Graph, Vertex两个类，建图实现。

思路：直接模拟



代码：

```python
n,m=map(int,input().split())
A=[[0]*n for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    A[a][b]=-1
    A[b][a]=-1
    A[a][a]+=1
    A[b][b]+=1
for i in range(n):
    print(*A[i])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image.png)




### LC78.子集

backtracking, https://leetcode.cn/problems/subsets/

思路：dfs


代码：

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        l=[]
        n=len(nums)
        def solve(k,l):
            ans.append(l[:])
            for j in range(k,n):
                solve(j+1,l+[nums[j]])
        solve(0,l)
        return ans
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-1.png)



### LC17.电话号码的字母组合

hash table, backtracking, https://leetcode.cn/problems/letter-combinations-of-a-phone-number/

思路：dfs



代码：

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
            di = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno","7": "pqrs","8": "tuv","9": "wxyz",}
            if not digits:
                return []
            ans=[]
            n=len(digits)
            def dfs(cnt,s):
                if cnt==n:
                    ans.append(s)
                    return 
                for i in di[digits[cnt]]:
                    dfs(cnt+1,s+i)
            dfs(0,'')
            return ans
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-2.png)



### M04089:电话号码

trie, http://cs101.openjudge.cn/practice/04089/

思路：
用字典套字典表示，要先排序预处理。


代码：

```python
class Node:
    def __init__(self):
        self.child={}
t=int(input())
for _ in range(t):
    n=int(input())
    root=Node()
    l=[input() for i in range(n)]
    l.sort(reverse=True)
    ans=0
    for s in l:
        def solve(root,s):
            for i in s:
                if i not in root.child:
                    return 0
                root=root.child[i]
            return 1
        ans+=solve(root,s)
        node=root
        for i in s:
            if i not in node.child:
                node.child[i]=Node()
            node=node.child[i]
    if ans>0:
        print('NO')
    else:
        print('YES')
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-3.png)




### T28046:词梯

bfs, http://cs101.openjudge.cn/practice/28046/

思路：最主要的是用两个字典建立边的联系



代码：

```python
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
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-4.png)



### T51.N皇后

backtracking, https://leetcode.cn/problems/n-queens/

思路：
回溯


代码：

```python
class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        ans = [] 
        def can_place(row, col, col_positions):
            for prev_row in range(row):
                prev_col = col_positions[prev_row]
                if prev_col == col or abs(prev_row - row) == abs(prev_col - col):
                    return False
            return True

        def solve(row, col_positions):
            if row == n:
                board = []
                for i in range(n):
                    line = ['.'] * n
                    line[col_positions[i]] = 'Q'
                    board.append(''.join(line))
                ans.append(board)
                return
            for col in range(n):
                if can_place(row, col, col_positions):
                    col_positions[row] = col
                    solve(row + 1, col_positions)
                    col_positions[row] = -1 
        
        col_positions = [-1] * n 
        solve(0, col_positions)
        return ans
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-5.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>
这次作业比较简单，好多都是以前做过的，跟进每日选做，正在学习图论。










