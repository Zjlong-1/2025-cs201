from collections import defaultdict
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        di = defaultdict(int)
        n = len(limits)
        for i in range(n):
            di[i] = limits[i]
        l = []
        sum1 = 0
        for i in range(n):
            sum1 += len(grid[i])
            for j in grid[i]:
                l.append((j, i))
        l.sort(reverse=True)
        ans = 0
        cnt = 0
        while k > 0 and cnt < sum1:
            if di[l[cnt][1]] > 0:
                di[l[cnt][1]] -= 1
                ans += l[cnt][0]
                cnt += 1
                k -= 1
            else:
                cnt += 1
        return ans
#思路是比较好的，全部拉成一列，化二维为一维，但这个while循环写得很烂，直接一开始拉长的时候只把有可能的加进去，
#这样就不需要再次判断了：
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        n = len(limits)
        l = []
        for i in range(n):
            grid[i].sort(reverse=True)
            l += grid[i][:min(len(grid[i]), limits[i])]
        l.sort(reverse=True)
        return sum(l[:min(k, len(l))])









