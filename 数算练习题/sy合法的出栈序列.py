#不简单的easy题，要注意到每次出栈的都是栈中最大的数。只要手动模拟这个过程即可
#一开始很容易想逆推，但事实上会比较复杂。
#现在再来看，发现是显然的，只要模拟数据的pop如果最后是空栈那么就是可行的，否则就是有问题
n=int(input())
l=list(map(int,input().split()))
stack=[]
cnt=0
for i in range(1,n+1):
    stack.append(i)
    while stack and stack[-1]==l[cnt]:
        stack.pop()
        cnt+=1
if stack:
    print('No')
else:
    print('Yes')
#不简单的easy题，要注意到每次出栈的都是栈中最大的数。只要手动模拟这个过程即可
n=int(input())
l=list(map(int,input().split()))
stack=[]
ans=[]
def solve():
    cnt=0
    for i in range(1,n+1):
        stack.append(i)
        while i>=l[cnt]:
            if cnt ==n-1:
                ans.append(stack.pop())
                break
            if not stack:
                return False
            ans.append(stack.pop())
            cnt+=1
    if ans==l:
        return True
    else:
        return False
if solve():
    print('Yes')
else:
    print('No')
#另一种方法：
def is_valid_pop_sequence(n, pop_sequence):
    stack = []
    nowMax = 0
    for x in pop_sequence:
        if x > nowMax:
            # 将 nowMax + 1 到 x 之间的所有元素入栈
            for j in range(nowMax + 1, x + 1):
                stack.append(j)
            nowMax = x
        # 检查栈顶元素是否等于 x
        if stack[-1] != x:
            return "No"
        else:
            stack.pop()
    return "Yes"

# 读取输入
n = int(input())
pop_sequence = list(map(int, input().split()))

# 输出结果
print(is_valid_pop_sequence(n, pop_sequence))