class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#用多次反转
        n=len(nums)
        k=k%n
        for i in range(n//2):
            nums[i],nums[n-1-i]=nums[n-1-i],nums[i]
        for i in range(k//2):
            nums[i],nums[k-1-i]=nums[k-1-i],nums[i]
        for i in range(k,(k+n)//2):
            nums[i],nums[n-1+k-i]=nums[n-1+k-i],nums[i]
        return nums
