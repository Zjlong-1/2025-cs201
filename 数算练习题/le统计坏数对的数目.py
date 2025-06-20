#直接暴力分堆算
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        nums = [n - i for n, i in enumerate(nums)]
        cnt = collections.Counter(nums)
        n = len(nums)
        res = n * (n - 1) // 2

        for k, v in cnt.items():
            if v >= 2:
                res -= v * (v - 1) // 2

        return res
#我的一遍过：
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        s=defaultdict(int)
        n=len(nums)
        ans=0
        for i in range(n):
            ans+=i-s[nums[i]-i]
            s[nums[i]-i]+=1
        return ans