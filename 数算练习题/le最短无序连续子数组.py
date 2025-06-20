#如果只跑一边的化会导致存在相等的情况时left的定位不准
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        right=-1
        left=-1
        cur=nums[0]
        n=len(nums)
        for i in range(n):
            if cur>nums[i]:
                right=i
            cur=max(cur,nums[i])
        cur=nums[-1]
        for i in range(n-1,-1,-1):
            if cur<nums[i]:
                left=i
            cur=min(cur,nums[i])
        return 0 if left==right==-1 else right-left+1
#妙一点的解法：
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        r = n - 1
        while r > 0 and nums[r - 1] <= nums[r]:
            r -= 1
        if r == 0: return 0

        vmax = max(nums[:r + 1])
        while r < n and vmax > nums[r]:
            r += 1

        l = 0
        while l < n - 1 and nums[l] <= nums[l + 1]:
            l += 1
        vmin = min(nums[l:])
        while l >= 0 and nums[l] > vmin:
            l -= 1

        return r - l - 1