# Assignment #9: Huffman, BST & Heap

Updated 1834 GMT+8 Apr 15, 2025

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

### LC222.完全二叉树的节点个数

dfs, https://leetcode.cn/problems/count-complete-tree-nodes/

思路：dfs,转为左子树和右子树



代码：

```python
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image.png)



### LC103.二叉树的锯齿形层序遍历

bfs, https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/

思路：还是用deque来一层一层展开，只是用一个cnt来判断是顺序还是反序。



代码：

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        if not root:
            return []
        q.append(root)
        ans=[]
        cnt=0
        while q:
            n=len(q)
            l=[]
            cnt+=1
            for _ in range(n):
                node=q.popleft()
                l.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if cnt%2==0:
                ans.append(l[::-1])
            else:
                ans.append(l[:])
        return ans
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-1.png)




### M04080:Huffman编码树

greedy, http://cs101.openjudge.cn/practice/04080/

思路：
直接用树来模拟


代码：

```python
import heapq
from collections import deque
n=int(input())
l=list(map(int,input().split()))
class Node:
    def __init__(self,w):
        self.w=w
        self.left=None
        self.right=None
    def __lt__(self, other):
        return self.w<other.w
heap=[Node(i) for i in l]
heapq.heapify(heap)
while len(heap)>1:
    a=heapq.heappop(heap)
    b=heapq.heappop(heap)
    merge=Node(a.w+b.w)
    merge.left=a
    merge.right=b
    heapq.heappush(heap,merge)
root=heap[0]
q=deque()
q.append((root,0))
ans=0
while q:
    node,d=q.popleft()
    if node.left:
        q.append((node.left,d+1))
    if node.right:
        q.append((node.right,d+1))
    if not node.right and not node.left:
        ans+=node.w*d
print(ans)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-2.png)




### M05455: 二叉搜索树的层次遍历

http://cs101.openjudge.cn/practice/05455/

思路：知道原理模拟就好了



代码：

```python
from collections import deque
class Node:
    def __init__(self,v):
        self.v=v
        self.left=None
        self.right=None
def solve(node,new):
    if node.v<new.v:
        if not node.right:
            node.right=new
            return
        solve(node.right,new)
    else:
        if not node.left:
            node.left=new
            return
        solve(node.left,new)
l=list(map(int,input().split()))
s=set()
s.add(l[0])
root=Node(l[0])
for i in l[1:]:
    if i in s:
        continue
    s.add(i)
    new=Node(i)
    solve(root,new)
q=deque()
q.append(root)
while q:
    for _ in range(len(q)):
        node=q.popleft()
        print(node.v,end=' ')
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-3.png)



### M04078: 实现堆结构

手搓实现，http://cs101.openjudge.cn/practice/04078/

类似的题目是 晴问9.7: 向下调整构建大顶堆，https://sunnywhy.com/sfbj/9/7

思路：由上一题有感而发用二叉树实现



代码：

```python
class Node:
    def __init__(self,v):
        self.v=v
        self.left=None
        self.right=None
def solve(node,new):
    if node.v<new.v:
        if not node.right:
            node.right=new
            return
        solve(node.right,new)
    else:
        if not node.left:
            node.left=new
            return
        solve(node.left,new)
n=int(input())
root=Node(float('inf'))
for _ in range(n):
    l=input().split()
    if len(l)==2:
        new=Node(int(l[-1]))
        solve(root,new)
    else:
        node=root
        parent=None
        while node.left:
            parent=node
            node=node.left
        print(node.v)
        parent.left=node.right
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-4.png)



### T22161: 哈夫曼编码树

greedy, http://cs101.openjudge.cn/practice/22161/

思路：
套模板，但就是很繁琐


代码：

```python
import heapq
from collections import deque
class Node:
    def __init__(self,w,v):
        self.w=w
        self.v=v
        self.left=None
        self.right=None
    def __lt__(self, other):
        if  self.w==other.w:
            return self.v<other.v
        return self.w<other.w
n=int(input())
heap=[]
for _ in range(n):
    v,w=input().split()
    w=int(w)
    heapq.heappush(heap,Node(w,v))
while len(heap)>1:
    a=heapq.heappop(heap)
    b=heapq.heappop(heap)
    merge=Node(a.w+b.w,min(a.v,b.v))
    merge.left=a
    merge.right=b
    heapq.heappush(heap,merge)
root=heap[0]
codes={}

def solve(node,code):
    if not node:
        return
    if not node.left and not node.right :
        codes[node.v]=code
    else:
        solve(node.left,code+'0')
        solve(node.right,code+'1')
solve(root,'')
def h_encode(s):
    ans=''
    for i in s:
        ans+=codes[i]
    return ans
def decode(s):
    ans=''
    node=root
    for i in s:
        if i=='0':
            node=node.left
        else:
            node=node.right
        if not node.left and not node.right:
            ans+=node.v
            node=root
    return ans
while True:
    try:
        s=input()
    except EOFError:
        break
    if s[0]=='0' or s[0]=='1':
        print(decode(s))
    else:
        print(h_encode(s))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-5.png)



## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

作业还行，感觉只要知道原理就比较好写了，前面的题目为后面的题做了铺垫，许多基础的class只要继承就行了。考完了期中，最近要把每日选做跟进。









