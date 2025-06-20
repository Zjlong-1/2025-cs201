#又是脑筋急转弯，三重循环不如两个双重循环
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        nums=list(set(nums))
        l={x^ y for x in nums for y in nums}
        return len({t^z for t in l for z in nums})

#还可以剪枝优化：
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        s = set()
        n = len(nums)
        MAX = (1 << len(bin(1500)[2:]))

        for i in range(n):
            for j in range(n):
                s.add(nums[i] ^ nums[j])
            if len(s) == MAX:
                break
        ans = set()
        for i in range(n):
            x = nums[i]
            for y in s:
                ans.add(x ^ y)
            if len(ans) == MAX:
                break
        return len(ans)