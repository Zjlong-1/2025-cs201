while True:
    n,k=map(int,input().split())
    if n==k==-1:
        break
    chess=[list(input()) for _ in range(n)]
    use=[False]*n
    ans=0
    def dfs(j,t):
        global ans
        if t==k:
            ans+=1
            return
        if j==n:
            return
        for i in range(j,n):
            for x in range(n):
                if chess[i][x]=='#' and not use[x]:
                    use[x]=True
                    dfs(i+1,t+1)
                    use[x]=False
    dfs(0,0)
    print(ans)
#另：
def solve(n, k, board):
    # 保存哪些列已经被占用
    used_cols = [False] * n
    # 保存哪些行已经放置了棋子
    used_rows = [False] * n
    result = 0

    def backtrack(row, count):
        nonlocal result

        # 如果放置的棋子数已经达到k，则返回
        if count == k:
            result += 1
            return

        if row >= n:
            return

        # 遍历这一行的每一个可能的位置
        for col in range(n):
            if board[row][col] == '#' and not used_cols[col] and not used_rows[row]:
                # 放置棋子
                used_cols[col] = True
                used_rows[row] = True
                backtrack(row + 1, count + 1)
                # 回溯
                used_cols[col] = False
                used_rows[row] = False

        # 也可以选择不放棋子
        backtrack(row + 1, count)

    backtrack(0, 0)
    return result


# 主程序
def main():
    while True:
        # 读入n和k
        n, k = map(int, input().split())
        if n == -1 and k == -1:
            break
        # 读入棋盘
        board = [input().strip() for _ in range(n)]
        # 计算并输出结果
        print(solve(n, k, board))


if __name__ == "__main__":
    main()
