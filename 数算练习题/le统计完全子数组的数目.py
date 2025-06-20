#滑动窗口，从合格的右端点开始扩散。
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        ans=0
        right=0
        m=len(set(nums))
        n=len(nums)
        s={}
        for i in range(n):
            if i>0:
                s[nums[i-1]]-=1
                if s[nums[i-1]]==0:
                    s.pop(nums[i])
            while right<n and len(s)<m:
                t=nums[right]
                s[t]=s.get(t,0)+1
                right+=1
            if len(s)==m:
                ans+=n-right+1
        return ans
#固定右端，跑左端
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        diff = len(set(nums))
        cnt = defaultdict(int)
        left = ans = 0
        for num in nums:
            cnt[num] += 1
            while len(cnt) == diff:
                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    del cnt[nums[left]]
                left += 1
            ans += left
        return ans