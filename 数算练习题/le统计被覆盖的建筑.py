#本来想用SUM来判断周围是否有树，但是两个合在一起时间复杂度会非常高（有许多没有必要的检查）还不如行列分开
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        l1=[[] for _ in range(n+1)]
        l2=[[] for _ in range(n+1)]
        for i in buildings:
            l1[i[0]].append(i[1])
            l2[i[1]].append(i[0])
        for i in l1:
            i.sort()
        for j in l2:
            j.sort()
        ans=0
        for i in buildings:
            a,b=i[0],i[1]
            if a!=l2[b][0] and a!=l2[b][-1] and b!=l1[a][-1] and b!=l1[a][0]:
                ans+=1
        return ans
#还可以就记录min,max(一维数组):
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        row_min = [n + 1] * (n + 1)
        row_max = [0] * (n + 1)
        col_min = [n + 1] * (n + 1)
        col_max = [0] * (n + 1)

        for x, y in buildings:
            if x < row_min[y]:
                row_min[y] = x
            if x > row_max[y]:
                row_max[y] = x
            if y < col_min[x]:
                col_min[x] = y
            if y > col_max[x]:
                col_max[x] = y

        res = 0
        for x, y in buildings:
            if row_min[y] < x < row_max[y] and col_min[x] < y < col_max[x]:
                res += 1
        return res
#时间复杂度太高，而且有问题。
n = 3
buildings = [[1,2],[2,1],[3,1],[1,1],[2,3],[3,2],[1,3]]
l = [[0] * (n + 1) for _ in range(n + 1)]
for i in buildings:
    l[i[0]][i[1]] = 1
l1 = [l[i][:] for i in range(n + 1)]
l2 = [l[i][:] for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        l1[i][j] += l1[i][j - 1]
        l2[j][i] += l2[j-1][i ]
ans = 0
for i in range(2, n):
    for j in range(2, n):
        if l1[i][j-1] > 0 and l1[i][j] < l1[i][-1] and l2[i-1][j] > 0 and l2[i][j] < l2[-1][j]:
            ans += 1
print(ans)

