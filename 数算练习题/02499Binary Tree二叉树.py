#要相信题目说的（哈哈哈哈哈），正的跟二叉树差不多。但是还是比较巧妙，要倒着来。
#注意到(i,j)的根节点，i<j时就是右子树，i>j时就是左子树
def solve(i,j):
    left=right=0
    if i==j==1:
        return 0,0
    if i>j:
        left,right=solve(i-j,j)
        left+=1
    else:
        left, right = solve(i, j-i)
        right+=1
    return left,right

n=int(input())
for i in range(1,n+1):
    a,b=map(int,input().split())
    print(f'Scenario #{i}:')
    a1,b1=solve(a,b)
    print(a1,b1)
    if i !=n:
        print()
#每次只一步一步走，显然是太慢了，数据大一点就直接爆栈。
#一次把可以走的都走了（取模）
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

n=int(input())
for i in range(1,n+1):
    a,b=map(int,input().split())
    print(f'Scenario #{i}:')
    a1,b1=solve(a,b)
    print(a1,b1)
    print()