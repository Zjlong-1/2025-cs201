#转化为多重背包
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        if all(x==0 for x in nums):
            return 0
        flag=[[True]+[False]*x for x in nums]
        for k,(l,r,val) in enumerate(queries):
            for i in range(l,r+1):
                if flag[i][-1]:
                    continue
                for j in range(nums[i],val-1,-1):
                    flag[i][j]=flag[i][j] or flag[i][j-val]
            if all(f[-1] for f in flag):
                return k+1
        return -1