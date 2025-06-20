# Assignment #4: 位操作、栈、链表、堆和NN

Updated 1203 GMT+8 Mar 10, 2025

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

### 136.只出现一次的数字

bit manipulation, https://leetcode.cn/problems/single-number/



<mark>请用位操作来实现，并且只使用常量额外空间。</mark>
注意到a^a=0,0^a=a


代码：

```python
    def singleNumber(self, nums: List[int]) -> int:
        ans=0
        for i in nums:
            ans=ans^i
        return ans
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>


![alt text](image.png)


### 20140:今日化学论文

stack, http://cs101.openjudge.cn/practice/20140/



思路：栈操作，与波兰表达式类似



代码：

```python
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



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-1.png)



### 160.相交链表

linked list, https://leetcode.cn/problems/intersection-of-two-linked-lists/



思路：两个都走一圈重合，看重合的部分



代码：

```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a,b=headA,headB
        while a!=b:
            a=a.next if a else headB
            b=b.next if b else headA
        return a
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-4.png)



### 206.反转链表

linked list, https://leetcode.cn/problems/reverse-linked-list/



思路：
就是间接量赋值


代码：

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a,b=head,None
        while a:
            a.next,b,a=b,a,a.next
        return b
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-2.png)



### 3478.选出和最大的K个元素

heap, https://leetcode.cn/problems/choose-k-elements-with-maximum-sum/



思路：难点在于用比较小的时间复杂度来实现前k大元素,事实上关注的前k个最大的，所以用堆实时维护（减去最小的）是比较巧妙的。



代码：

```python
class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        l=sorted((x,y,i) for i,(x,y) in enumerate(zip(nums1,nums2)))
        n=len(l)
        heap=[]
        ans=[0]*n
        s=0
        for i,(x,y,id) in enumerate(l):
            ans[id]=ans[l[i-1][2]] if i and x==l[i-1][0] else s
            s+=y
            if len(heap)<k:
                heappush(heap,y)
            else:
                s-=heappushpop(heap,y)
        return ans
            
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![alt text](image-3.png)



### Q6.交互可视化neural network

https://developers.google.com/machine-learning/crash-course/neural-networks/interactive-exercises

**Your task:** configure a neural network that can separate the orange dots from the blue dots in the diagram, achieving a loss of less than 0.2 on both the training and test data.

**Instructions:**

In the interactive widget:

1. Modify the neural network hyperparameters by experimenting with some of the following config settings:
   - Add or remove hidden layers by clicking the **+** and **-** buttons to the left of the **HIDDEN LAYERS** heading in the network diagram.
   - Add or remove neurons from a hidden layer by clicking the **+** and **-** buttons above a hidden-layer column.
   - Change the learning rate by choosing a new value from the **Learning rate** drop-down above the diagram.
   - Change the activation function by choosing a new value from the **Activation** drop-down above the diagram.
2. Click the Play button above the diagram to train the neural network model using the specified parameters.
3. Observe the visualization of the model fitting the data as training progresses, as well as the **Test loss** and **Training loss** values in the **Output** section.
4. If the model does not achieve loss below 0.2 on the test and training data, click reset, and repeat steps 1–3 with a different set of configuration settings. Repeat this process until you achieve the preferred results.

给出满足约束条件的<mark>截图</mark>，并说明学习到的概念和原理。





## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

额外刷了leetcode周赛，第440场有一点难，easy都要bfs，medium则直接上线段树和堆了，只做了两道，还是要多积累树的运用。









