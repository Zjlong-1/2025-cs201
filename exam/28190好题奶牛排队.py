#因为 A 是区间内最矮的，所以 [A.B]中，都比 A 高。所以只要 A 右侧第一个 ≤A的奶牛位于 B 的右侧，则 A 合法
#同理，因为B是区间内最高的，所以 [A.B]中，都比 B 矮。所以只要 B 左侧第一个 ≥B 的奶牛位于 A的左侧，则 B合法
#对于 “ 左/右侧第一个 ≥/≤ ” 我们可以使用单调栈维护。用单调栈预处理出 zz数组表示左，r 数组表示右。
#然后枚举右端点 B寻找 A，更新 ans 即可
#之前的思路有问题，想要有左边遍历得到右端点，侧重与找到一个确定右端点比较快的方法
#事实上，检验任意两个点是否合法更好操作，a,b（考虑两者的相互作用，相互影响），第一个小于a的数在b右侧，b左边第一个大于b的数在a左侧

n=int(input())
l=[]
for _ in range(n):
    l.append(int(input()))
left,right=[-1]*n,[n]*n
stack=[]
for i in range(n):#找左侧第一个大于l[i]的数位置
    while stack and l[stack[-1]]<l[i]:
        stack.pop()
    if stack:
        left[i]=stack[-1]
    stack.append(i)
stack=[]
for i in range(n-1,-1,-1):
    while stack and l[stack[-1]]>l[i]:
        stack.pop()
    if stack:
        right[i]=stack[-1]
    stack.append(i)
ans=0
for i in range(n):
    for j in range(left[i]+1,i):
        if right[j]>i:
            ans=max(ans,i-j+1)
            break
print(ans)
