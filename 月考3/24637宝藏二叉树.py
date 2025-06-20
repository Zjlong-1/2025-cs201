from functools import lru_cache
n=int(input())
l=list(map(int,input().split()))
@lru_cache(maxsize=None)
def g(i):
    if i>n:
        return 0
    return max(f(2*i),g(2*i))+max(f(2*i+1),g(2*i+1))
@lru_cache(maxsize=None)
def f(i):
    if i>n:
        return 0
    return l[i-1]+g(2*i)+g(2*i+1)
print(max(f(1),g(1)))
#尝试用dp写一下
n=int(input())
l=[0]+list(map(int,input().split()))
la=[0]*(1+n)#选自身
lb=[0]*(1+n)
for i in range(n,0,-1):
    if 2*i>n:
        la[i]=l[i]
        lb[i]=0
    elif 2*i==n:
        la[i]=l[i]
        lb[i]=l[2*i]
    else:
        la[i]=l[i]+lb[2*i]+lb[2*i+1]
        lb[i]=max(la[2*i],lb[2*i])+max(la[2*i+1],lb[2*i+1])
print(max(la[1],lb[1]))
#或者dp:

n = int(input())  # 节点数
value = list(map(int, input().split()))  # 每个节点的宝藏价值，1-based

# DP 数组初始化
f = [0] * (n + 2)  # f[i]: 选中 i
g = [0] * (n + 2)  # g[i]: 不选 i

# 自底向上，从叶子往根处理
for i in range(n, 0, -1):
    left = 2 * i
    right = 2 * i + 1

    # 安全获取左右子节点的状态
    if left <= n:
        f_left = f[left]
        g_left = g[left]
    else:
        f_left = g_left = 0

    if right <= n:
        f_right = f[right]
        g_right = g[right]
    else:
        f_right = g_right = 0

    # 状态转移
    f[i] = value[i - 1] + g_left + g_right
    g[i] = max(f_left, g_left) + max(f_right, g_right)

# 输出最大值
print(max(f[1], g[1]))

