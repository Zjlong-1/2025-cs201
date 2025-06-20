class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        ans=0
        t=nums[n//2]
        for i in range(n//2):
            ans+=t-nums[i]
        for i in range(n//2+1,n):
            ans+=nums[i]-t
        return ans