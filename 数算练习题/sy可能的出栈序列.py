n=int(input())
ans=[]
def dfs(stack,l,x):
    if x==n+1:
        while stack:
            l.append(stack.pop())
        if len(l)==n:
            ans.append(l[:])
        return
    stack.append(x)
    dfs(stack[:],l[:],x+1)
    stack.pop()
    if stack:
        l.append(stack.pop())
        dfs(stack,l,x)
        l.pop()
    else:
        dfs(stack,l,x+1)
dfs([1],[],2)
for i in reversed(ans):
    print(*i)

#另解：
def isValidSeq(v):
    s = []  # 模拟栈
    nowMax = 0  # 当前栈中最大的元素
    for num in v:
        if num > nowMax:
            for j in range(nowMax + 1, num + 1):
                s.append(j)
            nowMax = num
        if s[-1] != num:
            return False
        else:
            s.pop()
    return True

def DFS(idx, n, temp, used, result):
    if idx == n + 1:
        if isValidSeq(temp):
            result.append(temp[:])
        return
    for i in range(1, n + 1):
        if not used[i]:
            temp.append(i)
            used[i] = True
            DFS(idx + 1, n, temp, used, result)
            used[i] = False
            temp.pop()

def generate_sequences(n):
    result = []
    temp = []
    used = [False] * (n + 1)
    DFS(1, n, temp, used, result)
    return result

# 输入
n = int(input())
sequences = generate_sequences(n)

# 输出
for seq in sequences:
    print(" ".join(map(str, seq)))

