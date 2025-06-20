#有点意思，加cache超内存，不加又超时
while True:
    m,n=map(int,input().split())
    if n==m==0:
        break
    def dfs(x):
        if x>n:
            return 0
        return dfs(2*x)+dfs(x*2+1)+1
    print(dfs(m))
#只能动一点脑子了，手动找到最后一行
while True:
    m,n=map(int,input().split())
    if n==m==0:
        break
    cnt=0
    while (2**cnt)*m<=n:
        cnt+=1
    ans=2**cnt-1
    if (m+1)*(2**(cnt-1))-1>n:
        ans-=(m+1)*(2**(cnt-1))-1-n
    print(ans)
#还可以懒一点：
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