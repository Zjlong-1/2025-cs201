class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n=len(nums)
        ans=[-1]
        di=defaultdict(int)
        s=defaultdict(int)
        left=0
        for i in range(k):
            s[nums[i]]+=1
        for j in s:
            di[j]+=1
        for j in range(k,n):
            s[nums[j]]+=1
            while j-left+1>k:
                s[nums[left]]-=1
                left+=1
            for i in s:
                if s[i]:
                    di[i]+=1
        for i in di:
            if di[i]==1:
                ans.append(i)
        return max(ans)
#优化：只要想清楚就好做了，就是排除一些比较极端的情况，answer几乎是在左右两端产生的。
from collections import Counter
from typing import List


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return max(nums)
        if k == 1:
            res = -1
            counter = Counter(nums)
            for k, v in counter.items():
                if v == 1:
                    res = max(res, k)
            return res

        def f(arr: List[int], v: int):
            return -1 if v in arr else v

        return max(f(nums[1:], nums[0]), f(nums[:-1], nums[-1]))