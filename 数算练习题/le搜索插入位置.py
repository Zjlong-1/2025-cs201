class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[-1]<target:
            return len(nums)
        left,right=0,len(nums)-1
        while left<right:
            m=(left+right)//2
            if nums[m]<target:
                left=m+1
            elif nums[m]==target:
                return m
            else:
                right=m
        return left