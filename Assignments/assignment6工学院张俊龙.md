# Assignment #6: 回溯、树、双向链表和哈希表

Updated 1526 GMT+8 Mar 22, 2025

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

### LC46.全排列

backtracking, https://leetcode.cn/problems/permutations/

思路：
dfs回溯


代码：

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        l=[]
        n=len(nums)
        visit=[False]*n
        def solve(step):
            if step==n:
                ans.append(l[:])
            for i in range(n):
                if not visit[i]:
                    visit[i]=True
                    l.append(nums[i])
                    solve(step+1)
                    visit[i]=False
                    l.pop()
        solve(0)
        return ans 
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image.png)




### LC79: 单词搜索

backtracking, https://leetcode.cn/problems/word-search/

思路：
暴力dfs对每一个点都搜索是否存在


代码：

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n=len(word)
        t,m=len(board),len(board[0])
        l=[(0,1),(0,-1),(-1,0),(1,0)]
        def solve(x,y,k):
            if  not 0<=x<t or not 0<=y<m or not board[x][y]==word[k]:
                return False
            if k==n-1:
                return True
            board[x][y]=''
            for dx,dy in l:
                nx,ny=dx+x,dy+y
                if solve(nx,ny,k+1):
                    return True
            board[x][y]=word[k]
            return False
        for i in range(t):
            for j in range(m):
                if solve(i,j,0):
                    return True
        return False
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-2.png)



### LC94.二叉树的中序遍历

dfs, https://leetcode.cn/problems/binary-tree-inorder-traversal/

思路：
分为左右子树，转化为更小的问题


代码：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)
        dfs(root)
        return ans
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-3.png)




### LC102.二叉树的层序遍历

bfs, https://leetcode.cn/problems/binary-tree-level-order-traversal/

思路：一层一层来，统计每一层的个数来决定循环



代码：

```python
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        if not root:
            return []
        q.append(root)
        ans=[]
        while q:
            k=len(q)
            cur=[]
            for _ in range(k):
                x=q.popleft()
                cur.append(x.val)
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
            ans.append(cur)
        return ans
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-4.png)



### LC131.分割回文串

dp, backtracking, https://leetcode.cn/problems/palindrome-partitioning/

思路：
没有用DP，直接dfs+回溯


代码：

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        ans=[]
        def can(i,j):
            while i<j :
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        def solve(i,l):
            if i==n:
                ans.append(l)
                return 
            for j in range(i,n):
                if can(i,j):
                    solve(j+1,l+[s[i:j+1]])
        for i in range(n):
            if can(0,i):
                solve(i+1,[s[0:i+1]])
        return ans
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-6.png)




### LC146.LRU缓存

hash table, doubly-linked list, https://leetcode.cn/problems/lru-cache/

思路：
用内置函数OrderedDict（有点不讲道理）


代码：

```python
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.di=OrderedDict()
    def get(self, key: int) -> int:
        if key in self.di:
            self.di.move_to_end(key)
            return self.di[key]
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.di:
            self.di.move_to_end(key)
        elif self.capacity>0:
            self.capacity-=1
        else:
            self.di.popitem(last=False)
        self.di[key]=value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-7.png)




## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

最近把leetcode100题中的链表题全写完了，在OJ上复习了一下dp和dijkstra









