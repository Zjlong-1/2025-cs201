class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        @lru_cache(maxsize=None)
        def solve(n):
            if n==1:
                return [1]
            l1=[1]
            l=solve(n-1)
            for i in range(n-2):
                l1.append(l[i]+l[i+1])
            l1.append(1)
            return l1
        ans=[solve(i) for i in range(1,numRows+1)]
        return ans
#还可以DP
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = list()
        for i in range(numRows):
            row = list()
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(ret[i - 1][j] + ret[i - 1][j - 1])
            ret.append(row)
        return ret
