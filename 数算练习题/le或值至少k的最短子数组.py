class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        #两个循环暴力解，反正数据量不大
        ans=float('inf')
        n=len(nums)
        for i in range(n):
            t=nums[i]
            for j in range(i,n):
                t|=nums[j]
                if t>=k:
                    ans=min(ans,j-i+1)
        return ans if ans!=float('inf') else -1
#法2，非常巧妙的解法。因为|不好求逆，所以考虑统计每一位1出现的个数移动窗口时只要减去个数即可。
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        left=0
        l=[0]*30
        n=len(nums)
        def f(l):
            return sum(1<<i for i in range(30) if l[i]>0)
        ans=float('inf')
        for i in range(n):
            for j in range(30):
                l[j]+=(nums[i]>>j)&1
            while f(l)>=k and left<=i:
                for t in range(30):
                    l[t]-=(nums[left]>>t)&1
                ans=min(ans,i+1-left)
                left+=1
        return ans if ans!=float('inf') else -1
#但法2时间好像比较慢，因为每一次都要用函数，不如指针停下之后直接往回再算一次：
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        res = inf
        left = right = sum = 0
        for right, x in enumerate(nums):
            sum |= x
            while left <= right and sum >= k:
                res = min(res, right - left + 1)
                left += 1
                sum_ = 0
                for i in range(right, left - 1, -1):
                    sum_ |= nums[i]
                    if (sum_ >= k):
                        left = i
                        break
                sum = sum_
        return res if res < inf else -1