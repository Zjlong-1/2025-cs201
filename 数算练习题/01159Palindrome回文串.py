#最少插入字符数 = 原字符串长度 - LPS 长度
#证明：最少插入字符数 = 最少删除字符数，而最少删除字符数很显然就是LPS
#而且，计算 s 和 s_rev 的 最长公共子序列（LCS），它就是 LPS
n=int(input())
s=list(input())
rev=s[::-1]
l=[[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if s[i-1]==rev[j-1]:
            l[i][j]=l[i-1][j-1]+1
        else:
            l[i][j]=max(l[i-1][j],l[i][j-1])
print(n-l[n][n])
#超时了，改为一维数组：
n=int(input())
s=list(input())
rev=s[::-1]
l=[0]*(n+1)
for i in range(n):
    for j in range(1,n+1):
        if s[i]==rev[j-1]:
            l[j]=l[j-1]+1
        else:
            l[j]=max(l[j],l[j-1])
print(n-l[-1])
#两个列表又超时了，只能每次记录一个值
n=int(input())
s=list(input())
rev=s[::-1]
l=[0]*(n+1)
for i in range(n):
    pre=0
    for j in range(1,n+1):
        cur=l[j]
        if s[i]==rev[j-1]:
            l[j]=pre+1
        else:
            l[j]=max(l[j],l[j-1])
        pre=cur
print(n-l[-1])
#还是很慢，加一个函数加快一点,而且max很慢，要改为手动判断赋值
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
solve()