class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        x=1
        n,m=len(grid),len(grid[0])
        ans=[[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                x*=grid[i][j]
        for i in range(n):
            for j in range(m):
                ans[i][j]=(x//grid[i][j])%12345
        return ans
#竟然在倒数第二个数据上超时了，有点离谱，但是要是能过这个题目也就没有什么意思了。
#改进：
#本题的难点在于直接全部相乘的话可能数据太大导致直接超时，所以要取模处理，但是取模后再进行乘除法混用显然是不行的，所以要想一个办法
#优化，关键在于避免除法。而这只要分为两个左右乘积计算即可。
#关键在于乘积取模,以及抽象为一维数组，只要分左右即可
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        left,right=1,1
        n,m=len(grid),len(grid[0])
        ans=[[0]*m for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                ans[i][j]=right
                right=(grid[i][j]*right)%12345
        for i in range(n):
            for j in range(m):
                ans[i][j]=ans[i][j]*left%12345
                left=left*grid[i][j]%12345
        return ans
#还可以节省一个循环：
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        suf = [1] * (m * n)
        p = [[0] * n for _ in range(m)]
        MOD = 12345
        for idx in range(m * n - 2, -1, -1):
                suf[idx] = suf[idx + 1] * grid[(idx + 1) // n][(idx + 1) % n] % MOD
        pre = 1
        for i in range(m * n):
            row, col = (i // n), i % n
            p[row][col] = pre * suf[i] % MOD
            pre = pre * grid[row][col] % MOD
        return p