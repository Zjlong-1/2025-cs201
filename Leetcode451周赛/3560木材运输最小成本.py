class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        if n<m:
            n,m=m,n
        if n<=k:
            return 0
        return (n-k)*k