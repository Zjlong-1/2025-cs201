# Assignment #5: 链表、栈、队列和归并排序

Updated 1348 GMT+8 Mar 17, 2025

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

### LC21.合并两个有序链表

linked list, https://leetcode.cn/problems/merge-two-sorted-lists/

思路：分治排序



代码：

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans=ListNode()
        k=ans
        while list1 and list2:
            if list1.val<list2.val:
                k.next=list1
                list1=list1.next
                k=k.next
            else:
                k.next=list2
                list2=list2.next
                k=k.next
        while list1:
            k.next=list1
            list1=list1.next
            k=k.next
        while list2:
            k.next=list2
            list2=list2.next
            k=k.next
        return ans.next
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-5.png)




### LC234.回文链表

linked list, https://leetcode.cn/problems/palindrome-linked-list/

<mark>请用快慢指针实现。</mark>



代码：

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l,f=head,head
        stack=[]
        while f and f.next:
            stack.append(l.val)
            l=l.next
            f=f.next.next
        if f :
            l=l.next
        while l:
            if l.val!=stack.pop():
                return False
            l=l.next
        return True
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-10.png)



### LC1472.设计浏览器历史记录

doubly-lined list, https://leetcode.cn/problems/design-browser-history/

<mark>请用双链表实现。</mark>



代码：

```python
class Node:
    def __init__(self,val=None,pre=None,next=None):
        self.val=val
        self.next=None
        self.pre=None
class BrowserHistory:
    def __init__(self, homepage: str):
        self.cur=Node(homepage)
    def visit(self, url: str) -> None:
        self.cur.next=Node(url)
        self.cur.next.pre=self.cur
        self.cur=self.cur.next
    def back(self, steps: int) -> str:
        k=self.cur
        while k.pre and steps:
            k=k.pre
            steps-=1
        self.cur=k
        return k.val
    
    def forward(self, steps: int) -> str:
        k=self.cur
        while k.next and steps:
            steps-=1
            k=k.next
        self.cur=k
        return k.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-6.png)




### 24591: 中序表达式转后序表达式

stack, http://cs101.openjudge.cn/practice/24591/

思路：

用栈实现，并用字典确定运算顺序

代码：

```python
def solve(s):
    di={'*':1,'/':1,'-':0,'+':0}
    d1={'(',')'}
    stack=[]
    ans=[]
    num=''
    for i in s:
        if i.isdigit() or i=='.':
            num+=i
        else:
            if num:
                ans.append(num)
                num=''
            if i in di:
                while stack and stack[-1] in di and di[stack[-1]]>=di[i]:
                    ans.append(stack.pop())
                stack.append(i)
            elif i=='(':
                stack.append(i)
            elif i==')':
                while stack[-1]!='(':
                    ans.append(stack.pop())
                stack.pop()
    if num:
        ans.append(num)
    while stack :
        ans.append(stack.pop())
    print(' '.join(ans))
n=int(input())
for _ in range(n):
    s=input()
    solve(s)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-7.png)




### 03253: 约瑟夫问题No.2

queue, http://cs101.openjudge.cn/practice/03253/

<mark>请用队列实现。</mark>
每m次就只popleft()不append


代码：

```python
from collections import deque
while True:
    n,p,m=map(int,input().split())
    if n==p==m==0:
        break
    ans=[]
    q=deque()
    for i in range(p,n+1):
        q.append(i)
    for i in range(1,p):
        q.append(i)
    while q:
        for _ in range(m-1):
            q.append(q.popleft())
        ans.append(q.popleft())
    print(','.join(map(str,ans)))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-8.png)




### 20018: 蚂蚁王国的越野跑

merge sort, http://cs101.openjudge.cn/practice/20018/

思路：两个部分之间产生的逆序数与内部之间的顺序无关，所以可以在在实现排序的同时实现逆序数



代码：

```python
n=int(input())
l=[0]*n
for i in range(n-1,-1,-1):
    l[i]=int(input())
ans=0
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
merge(l)
print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![alt text](image-9.png)




## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>
最近额外在leetcode上刷了一些二叉树的题目：236，117，116，106.正在学习线段树的用法










