# CHEATSHEET

## 1.Dijkstra

```python
import heapq
m,n,p=map(int,input().split())
l=[input().split() for _ in range(m)]
for _ in range(p):
    a,b,c,d=map(int,input().split())
    def solve():
        if l[a][b]=='#' or l[c][d]=='#':
            return 'NO'
        heap=[(0,a,b)]
        s=set()
        di=[(0,1),(0,-1),(1,0),(-1,0)]
        while heap:
            way,x,y=heapq.heappop(heap)
            if x==c and y==d:
                return way
            s.add((x,y))
            for dx,dy in di:
                nx,ny=dx+x,dy+y
                if 0<=nx<m and 0<=ny<n and l[nx][ny]!='#' and (nx,ny) not in s:
                    heapq.heappush(heap,(way+abs(int(l[nx][ny])-int(l[x][y])),nx,ny))
        return 'NO'
   #加visit
   m, n = len(moveTime), len(moveTime[0])
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True

        heap = [(0, 0, 0, 0)]
        while heap:
            t, k, i, j = heapq.heappop(heap)
            for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                ni, nj = i + di, j + dj
                if 0<=ni<m and 0<=nj<n and not visited[ni][nj]:
                    nt = max(t+k+1, moveTime[ni][nj]+k+1)
                    nk = k ^ 1
                    if ni == m-1 and nj == n-1:
                        return nt
                    heapq.heappush(heap, (nt, nk, ni, nj))
                    visited[ni][nj] = True
        return 0
#用dist:
        n,m=len(moveTime),len(moveTime[0])
        dist=[[float('inf')]*m for _ in range(n) ]
        dist[0][0]=0
        heap=[(0,0,0,1)]
        di=[(1,0),(-1,0),(0,1),(0,-1)]
        while heap:
            t,x,y,c=heapq.heappop(heap)
            if (x,y)==(n-1,m-1):
                return t
            for dx,dy in di:
                nx,ny=dx+x,dy+y
                if 0<=nx<n and 0<=ny<m:
                    k=max(t,moveTime[nx][ny])+c
                    if k<dist[nx][ny]:
                        dist[nx][ny]=k
                        heapq.heappush(heap,(k,nx,ny,((c-1)^1)+1))
  #变形：
import heapq
k=int(input())
n=int(input())
r=int(input())
l=[[]for _ in range(n+1)]
for _ in range(r):
    s,d,le,t=map(int,input().split())
    l[s].append((d,le,t))
def solve():
    vi =[float('inf')]*(n+1)
    heap = [(0, 1, 0)]
    while heap:
        len1, u, c = heapq.heappop(heap)
        if u == n:
            return len1
        if  c>vi[u]:
            continue
        vi[u]=c
        for v, le, t in l[u]:
            if t + c <=k:
                heapq.heappush(heap, (len1+le, v, t+c))
    return -1
print(solve())
#或者：
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

## 2.Prim

```python
#prim算法（稠密图）关注的是点：
#用一个超强的字典集合组合来节省空间
import heapq
n=int(input())
di={chr(i+65):{} for i in range(n)}
for _ in range(n-1):
    l=input().split()
    t=int(l[1])
    for i in range(2,len(l),2):
        di[l[i]][l[0]]=int(l[i+1])
        di[l[0]][l[i]]=int(l[i+1])
use=set()
use.add('A')
h=[]
for to,cost in di['A'].items():
    heapq.heappush(h,(cost,'A',to))
heapq.heapify(h)
ans=0
while h:
    cost,f,t=heapq.heappop(h)
    if t not in use:
        use.add(t)
        ans+=cost
        for t1,cost1 in di[t].items():
            if t1 not in use:
                heapq.heappush(h,(cost1,t,t1))
print(ans)
```

## 3.stack处理括号

```python
        if len(s)%2!=0:
            return False
        di = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack=[]
        for i in s:
            if s in di:
                if not stack or stack[-1]!=di[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return not stack
```

## 4.判断数字二进制第x位是否为1

```python
i&1<<x!=0#其中的优先级：'<<'>&>!
```

## 5.stack实现后缀表达式与中缀表达式，以及计算器的实现

```python
#中缀转后缀：带括号，数字直接加入，当前的优先级小于stack最后的，那么就一直pop
stack = []
output = []
di = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
l = input()
cnt = 0
n = len(l)
while cnt < n:
    if l[cnt].isdigit():
        x = int(l[cnt])
        cnt += 1
        while cnt < n and l[cnt].isdigit():
            x = x * 10 + int(l[cnt])
            cnt += 1
        output.append(x)
    elif l[cnt] == '(':
        stack.append(l[cnt])
        cnt += 1
    elif l[cnt] == ')':
        cnt += 1
        while stack and stack[-1] != '(':
            output.append(stack.pop())
        stack.pop()
    else:
        while stack and stack[-1] != '(' and di[l[cnt]] <= di[stack[-1]]:
            output.append(stack.pop())
        stack.append(l[cnt])
        cnt += 1
while stack:
    output.append(stack.pop())
print(' '.join(map(str, output)))
#计算后缀：
s=input().split()
stack=[]
for i in s:
    if i.isdigit():
        stack.append(int(i))
    else:
        a,b=stack.pop(),stack.pop()
        stack.append(eval(f'{b}{i}{a}'))#这里是为了保证原来输入的顺序
print(f'{stack[0]:.2f}')
#后序转中序，并且去除多余的括号：
l=input().split()
di={'+':1, '-':1, '*':2, '/':2, '^':3}
stack=[]
for i in l:
    if i not in di:
        stack.append((i,4))
    else:
        right,rightv=stack.pop()
        left,leftv=stack.pop()
        curv=di[i]
        if leftv<curv:#优先级小，加括号
            left=f'({left})'
        if rightv<curv or (i=='^' and curv==rightv):
            right=f'({right})'
        new=f'{left}{i}{right}'
        stack.append((new,curv))
print(stack[-1][0])
#计算波兰表达式（前缀表达式）：
D=input().split()
D.reverse()
def STACK(D):
    stack=[]
    for i in D:
        if i in '+-*/':
            a=stack.pop()
            b=stack.pop()
            stack.append(str(eval(a+i+b)))
        else:
            stack.append(i)
    return stack[0]
print('%6f'% float(STACK(D)))
```

## 6.另外一个经典的栈（每日化学论文，把连续的x个字符串s记为[xs]）

```python
#[2b[3a]c]->baaacbaaac
l=input()
stack=[]
res,multi='',0
k=0
if l[k]=='[':
    k+=1
    stack.append(('',1))
for i in l[k:]:
    if i=='[':
        stack.append((res,multi))
        res,multi='',0
    elif i==']':
        res1,multi1=stack.pop()
        res=res1+multi*res
        multi=multi1
    elif '0' <= i <= '9':
        multi = multi * 10 + int(i)
    else:
        res += i
print(res)
```

## 7.辅助栈，找出没有匹配的括号

```python
stack1=[]
    stack2=[]
    n=len(s)
    ans=[' ']*n
    for i in range(n):
        if s[i] in d:
            if d[s[i]]==0:
                stack1.append(i)
            else:
                if stack1:
                    stack1.pop()
                else:
                    stack2.append(i)
    for i in stack1:
        ans[i]='$'
    for i in stack2:
        ans[i]='?'
```

## 8.提取小数

```python
for i in s:#s是一个没有空隙的字符串
        if i.isdigit() or i=='.':
            num+=i
        else:
            if num:
                ans.append(num)
                num=''
#之后再依据要求看是否转浮点数
```

## 9.小组队列，将deque放在defaultdict,并且用坐标排

```python
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
```

## 10.倒排索引查询

```python
for i in range(n):
    l=list(map(int,input().split()))
    for k in l[1:]:
        di[i].add(k)
        file.add(k)
t=int(input())
for _ in range(t):
    l=list(map(int,input().split()))
    ans=None
    for i in range(n):
        if l[i]==1:
            if ans is None:
                ans=di[i].copy()
            else:
                ans&=di[i]
        elif l[i]==-1:
            if ans is None:
                ans=file.copy()
            ans-=di[i]
```

## 11.一些注意事项

1.防止静态检测出现问题： pylint:skip-file或者提前声明变量
\
2.有时候循环层数过多导致的runtime error:改递归层数：import sys
sys.setrecursionlimit(100000)
\
3.from functools import lru_cache
@lru_cache(maxsize=None)

## 12.并查集+路径压缩

```python
    l=[i for i in range(n+1)]
    def find(x):
        if l[x]!=x:
            l[x]=find(l[x])
        return l[x]
```

## 13.线段树（先弄成完全二叉树）开一个4*n的列表

## 14.中序与后序遍历构建二叉树,前序和中序遍历

```python
    def buildTree( inorder: List[int], postorder: List[int]):#中+后
        index = {element: i for i, element in enumerate(inorder)}
        def build(in_left, in_right, post_left, post_right):
            if post_left > post_right:
                return None
            root_val = postorder[post_right]
            root = TreeNode(root_val)
            root_pos = index[root_val]
            left_size = root_pos - in_left
            root.left = build(in_left, root_pos - 1, post_left, post_left + left_size - 1)
            root.right = build(root_pos + 1, in_right, post_left + left_size, post_right - 1)
            return root
        return build(0, len(inorder) - 1, 0, len(postorder) - 1)
#前+中
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        val_to_index = {}
        for i in range(len(inorder)):
            val_to_index[inorder[i]] = i
        def build(preorder, pre_start, pre_end, inorder, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            index = val_to_index[root_val]
            left_size = index - in_start
            root.left = build(preorder, pre_start + 1, pre_start + left_size, inorder, in_start, index - 1)
            root.right = build(preorder, pre_start + left_size + 1, pre_end, inorder, index + 1, in_end)
            return root
        return build(preorder, 0, len(preorder) - 1, inorder, 0, len(inorder) - 1)
#不加哈希表：
        if len(inorder) == 0:
            return None
        head = postorder[-1]
        leftlen = inorder.index(head)
        rightlen = len(inorder) - 1 - leftlen
        return TreeNode(head, self.buildTree(inorder[:leftlen], postorder[:leftlen]),
                        self.buildTree(inorder[leftlen + 1:], postorder[leftlen:len(inorder) - 1]))
            
 if len(preorder)==0:
            return None
        head=preorder[0]
        leftlen=inorder.index(head)
        return TreeNode(head,self.buildTree(preorder[1:leftlen+1],inorder[:leftlen]),self.buildTree(preorder[leftlen+1:],inorder[leftlen+1:]))
```

## 15.merge(求逆序数)也可以用此快排

```python
def merge(l):
    global ans
    if len(l)<=1:
        return l
    mid=len(l)//2
    leftl,rightl=merge(l[:mid]),merge(l[mid:])
    left,right=0,0
    cnt=0
    while len(leftl)>left and len(rightl)>right:
        if leftl[left]<=rightl[right]:
            l[cnt]=leftl[left]
            left+=1
        else:
            l[cnt]=rightl[right]
            right+=1
            ans+=len(leftl)-left
        cnt+=1
    while len(leftl)>left:
        l[cnt] = leftl[left]
        left += 1
        cnt+=1
    while len(rightl)>right:
        l[cnt]=rightl[right]
        right+=1
        cnt+=1
    return l
```

## 16.求最小操作数生成回文串

```python
def solve():
    n = int(input())
    s = list(input())
    rev = s[::-1]
    l = [0] * (n + 1)
    for i in range(n):
        pre = 0
        for j in range(1, n + 1):
            cur = l[j]
            if s[i] == rev[j - 1]:
                l[j] = pre + 1
            else:
                if l[j-1]>l[j]:
                    l[j]=l[j-1]
            pre = cur
    print(n - l[-1])
solve()#最少插入字符数 = 原字符串长度 - LPS 长度
#证明：最少插入字符数 = 最少删除字符数，而最少删除字符数很显然就是LPS
#而且，计算 s 和 s_rev 的 最长公共子序列（LCS），它就是 LPS
```

## 17.查找多个

```python
#有一个很好的剪枝
        if r0 not in visited:
            visited.add(r0)
            queue.append((r0, num_str + "0"))#利用模周期
```

## 18.前中后遍历

- 前序遍历：根 -> 左子树 -> 右子树，第一个节点是**根节点**。
- 后序遍历：左子树 -> 右子树 -> 根，最后一个节点是**根节点**。
- 中序遍历：左子树 -> 根 -> 右子树，根节点在中间，**左边是左子树**，右边是右子树。

## 19.括号树建树

```python
class TreeNode:#A(B(E),C(F,G),D(H(I)))
    def __init__(self,val):
        self.l=[val]
s=input()
stack=[]
node=None
for i in s:
    if i!='(' and i!=')' and i!=',':
        node=TreeNode(i)
        if stack:
            stack[-1].l.append(node)
    elif i=='(':
        if node:
            stack.append(node)
            node=None
    elif i==')':
        if stack:
            node=stack.pop()
```

## 20.建立二叉搜索树

```python
from collections import deque#实际上就是一个一个插入
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

## 21.词梯构建

```python
from collections import defaultdict
from collections import deque
n=int(input())
di=defaultdict(list)
road=defaultdict(list)
for _ in range(n):
    s=input()
    for i in range(4):
        t=s[:i]+'-'+s[i+1:]#替换符，将点都加入列表，同一表里面相互连边
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
```

## 22.Warnsdorff 规则,有序的走，可以大量减低时间复杂度

```python
n=int(input())#总结来说就是每次都走选择度最小的（最窄的路径）
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

## 23.入度判断是否有环

```python 
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
            q.append(v)#最后cnt==n就没有环，否则有

```

## 23.Floyd-Warshall求**任意两点之间的最短路径**（多源最短路径）

```python
for k in range(n):      # 枚举中间节点
    for i in range(n):  # 起点
        for j in range(n):  # 终点
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                #如果要记录路径
p=int(input())#用下一个指向统计
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
for k in range(p):#最小路径中的下一跳
    for i in range(p):
        if length[i][k]==float('inf'):
            continue
        for j in range(p):
            if length[k][j]==float('inf'):
                continue
            x=length[i][k]+length[k][j]
            if x<length[i][j]:
                length[i][j]=x·
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

## 24.扩展二叉树（空的节点用.补齐）

```python
def build(idx):
    if s[idx]=='.':
        return None,idx+1
    node=Node(s[idx])
    idx+=1
    node.left,idx=build(idx)
    node.right,idx=build(idx)
    return node,idx
root,t=build(0)
```

## 25.Binary Tree(a,b->a+b,b and a,a+b)

```python 
def solve(i,j):
    left=right=0
    if i==j==1:
        return 0,0
    if i==1:
        return 0,j-1
    if j==1:
        return i-1,0
    if i>j:
        left,right=solve(i%j,j)
        left+=i//j
    else:
        left, right = solve(i, j%i)
        right+=j//i
    return left,right
```

## 26.二叉树数节点

```python
def count_subtree_nodes(m, n):
    count = 0
    left = m
    right = m
    # 每层的节点编号范围为 [left, right]
    while left <= n:
        count += min(n, right) - left + 1
        left *= 2
        right = right * 2 + 1
    return count
```

## 27.电话号码，用字典套字典存储每一个路径

```python
t=int(input())
for _ in range(t):
    s = {}
    s2 = s
    n=int(input())
    l=[input() for i in range(n)]
    l.sort(reverse=True)
    for j in l[0]:
        s2[j]={}
        s2=s2[j]
    def solve():
        for i in l[1:]:
            flag = True
            s1 = s
            for j in range(len(i)):
                if i[j] not in s1:
                    flag = False
                    s1[i[j]] = {}
                    s1 = s1[i[j]]
                    for k in range(j + 1, len(i)):#还可以这样：if i[j] not in s1:
                        s1[i[k]] = {}             #       flag=True
                        s1 = s1[i[k]]             #      s1[i[j]] = {}
                    break                           #然后直接继续循环，反正是空的，所以每次第一个if都成立
                else:
                    s1=s1[i[j]]

            if flag:
                print('NO')
                return
        print('YES')
    solve()
```

## 28.Kruskal(并查集)

```python
def solve(dist):
    n=len(dist)
    s=[i for i in range(n)]
    size=[1]*n
    def f(x):
        if f(x)!=s[x]:
            s[x]=f(s[x])
        return s[x]
    edges=[]
    for i in range(n):
        for j in range(i+1,n):
            edges.append((dist[i][j],i,j))
    edges.sort()
    ans=0
    for lens,x,y in edges:
        x1,y1=f(x),f(y)
        if x1==y1:
            continue
        ans+=lens
        size[x1]+=size[y1]
        s[y1]=x1
        if size[x1]==n:
            break
    return ans
```

## 29.最大正方形：确定右下角，取周围三个最小 + 1

```python 
for i in range(m):
    if matrix[0][i] == '1':
        la[0][i] = 1
        ans = 1
for i in range(1, n):
    if matrix[i][0] == '1':
        la[i][0] = 1
        ans = max(ans, la[i][0])
    for j in range(1, m):
        if matrix[i][j] == '1':
            la[i][j] = min(la[i-1][j], la[i-1][j-1], la[i][j-1]) + 1
            ans = max(ans, la[i][j])
return ans**2
```

## 30.集合的一些用法

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # 并集: {1, 2, 3, 4, 5}
print(a & b)   # 交集: {3}
print(a - b)   # 差集: {1, 2}
print(a ^ b)   # 对称差集: {1, 2, 4, 5}
```

## 31.文本二叉树，用stack实现

```python
class Node:
    def __init__(self,v,d):
        self.d=d
        self.v=v
        self.left=None
        self.right=None
def q(node):
    if not node:
        return ''
    if node.v=='*':
        return ''
    return node.v+q(node.left)+q(node.right)
n=int(input())
for _ in range(n):
    l=[]
    stack=[]
    while True:
        s=input()
        if s=='0':
            break
        d=len(s)-1
        node=Node(s[-1],d)
        l.append(node)
        while stack and l[stack[-1]].d>=d:#下面几行是精华
            stack.pop()
        if stack:
            parent=l[stack[-1]]
            if not parent.left:
                parent.left=node
            else:
                parent.right=node
        stack.append(len(l)-1)
    print(q(l[0]))
    print(h(l[0]))
    print(z(l[0]))
    print()
```

## 32.全有边，其中又有特殊边

```python
#每两个点之间都连边，只是地铁和走路导致的时间区别而已，最优化肯定是走已经存在的点。
# 而且由于只考虑时间的加和，同一轨道上面的点只需要记录相邻的点连边即可
#题目没有讲清楚输入的终止条件
import heapq
import math
a,b,c,d=map(int,input().split())
s={}
way=set()
while True:
    try:
        l=list(map(int,input().split()))
        if l==[-1,-1]:
            break
        l1=[(l[2*i],l[2*i+1]) for i in range(len(l)//2-1)]
        for j,x in enumerate(l1):
            s[x]=float('inf')
            if j!=len(l1)-1:
                way.add((x,l1[j+1]))
                way.add((l1[j+1],x))
    except EOFError:
        break
def di(x1,y1,x2,y2):
    return math.sqrt(((x1-x2)**2+(y1-y2)**2))
s[(a,b)],s[(c,d)]=0,float('inf')
heap=[(0,a,b)]
while heap:
    w,x,y=heapq.heappop(heap)
    if (x,y)==(c,d):
        break
    for i in s.keys():
        if i!=(x,y):
            chu=40000 if ((x,y),i) in way else 10000
            t=di(x,y,i[0],i[1])/chu+w
            if t<s[i]:
                s[i]=t
                heapq.heappush(heap,(t,i[0],i[1]))
print(round(s[(c,d)]*60))
```

## 33.defaultdict的灵活使用

```python
d = defaultdict(lambda: float('inf'))
```

## 34.所有的环都必须有偶数个顶点，这等价于图是二分图(dfs实现)

```python
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        l=[-1]*n
        flag=True
        def dfs(x,t):
            nonlocal flag 
            for i in graph[x]:
                if l[i]==-1:
                    l[i]=t
                    dfs(i,t^1)
                elif l[i]!=t:
                    flag=False
        for i in range(n):
            if l[i]==-1:
                l[i]=0
                dfs(i,1)
        return flag
```

## 35.dfs实现二分图最大匹配

```python
class Solution:
    def domino(self, n: int, m: int, broken: List[List[int]]) -> int:
        # 相邻坐标（x,y）的和，奇偶性不同。 所以转化为二分图最大匹配
        match = [[(-1, -1)] * m for _ in range(n)]
        bk = set()
        for x, y in broken:
            bk.add((x, y))
        # 匈牙利算法(增广路)
        def dfs(i: int, j: int) -> bool:
            st.add((i, j))
            for i0, j0 in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= i0 < n and 0 <= j0 < m and (i0, j0) not in bk:
                    nxt = match[i0][j0]  # 寻找增广路径
                    if nxt in st:
                        continue
                    if nxt[0] == -1 or dfs(nxt[0], nxt[1]):  # 如果还没配对，或者配的对可以找到增广路径
                        match[i][j] = (i0, j0)
                        match[i0][j0] = (i, j)
                        return True
            return False
        res = 0
        for x in range(n):
            for y in range(m):
                if (x + y) % 2 == 0:  # 从偶数集开始，从奇数集开始也行
                    if (x, y) not in bk:
                        st = set()
                        if dfs(x, y):
                            res += 1
        return res

```

## 36.KMP

```python
def build_next(pattern):
    m = len(pattern)
    next_arr = [0] * m
    j = 0 
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = next_arr[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        next_arr[i] = j
    return next_arr
def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return 0
    next_arr = build_next(pattern)
    j = 0  
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = next_arr[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            return i - m + 1
    return -1 
def kmp_all_matches(text, pattern):
    #在主串 text 中查找模式串 pattern 的所有出现位置，返回一个列表。
    #如果完全没有匹配位置，则返回空列表。
    n, m = len(text), len(pattern)
    result = []
    if m == 0:
        # 约定：空串在每个位置都被认为是匹配，但是通常不单独使用此情况
        return list(range(n + 1))
    next_arr = build_next(pattern)
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = next_arr[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            # 匹配起始位置为 i - m + 1
            result.append(i - m + 1)
            # 继续寻找下一个匹配，回退 j 到 next_arr[j - 1]
            j = next_arr[j - 1]
    return result

```

## 37.dp小偷背包

```python
N, B = map(int, input().split())
values = list(map(int, input().split()))
weights = list(map(int, input().split()))
dp = [0] * (B + 1)
for i in range(N):
	prev = dp[:] # 复制上⼀次的状态
for j in range(B + 1):
	if j >= weights[i]:
		dp[j] = max(prev[j], prev[j - weights[i]] + values[i])
print(dp[B])
```

## 38.KMP的用处

```python
#next[i] 表示字符串 s[0:i+1] 的 最长相等的前后缀长度。
def kmp_next(s):
  	# kmp算法计算最长相等前后缀
    next = [0] * len(s)
    j = 0
    for i in range(1, len(s)):
        while s[i] != s[j] and j > 0:
            j = next[j - 1]
        if s[i] == s[j]:
            j += 1
        next[i] = j
    return next
def main():
    case = 0
    while True:
        n = int(input().strip())
        if n == 0:
            break
        s = input().strip()
        case += 1
        print("Test case #{}".format(case))
        next = kmp_next(s)
        for i in range(2, len(s) + 1):
            k = i - next[i - 1]		# 可能的重复子串的长度，精华
            if (i % k == 0) and i // k > 1:#可以用反证法证明
                print(i, i // k)
        print()
```

## 39.Bellman–Ford,判断是否有负环或者找没有负环的最小路径

```python
# 2. 对全部边做 n-1 轮松弛
#    如果在某一轮没有任何松弛发生，可以提前退出
dist = [INF] * (n + 1)
dist[src] = 0
for i in range(1, n):
    updated = False
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            updated = True
    if not updated:
        break
# 3. 再做一次遍历，检测负权环
has_neg_cycle = False
for u, v, w in edges:
    if dist[u] != INF and dist[u] + w < dist[v]:#有一点DP背包循环的感觉
        # 说明还可以继续松弛，则一定存在负权环
        has_neg_cycle = True
        break

return dist, has_neg_cycle
```

## 40.滑动窗口

```python
 		ans=0
        for i in range(n):
            if nums[i]==m:
                cnt+=1
            while cnt>=k:
                if nums[left]==m:
                    cnt-=1
                left+=1
            ans+=left
```

