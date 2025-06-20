class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        di=defaultdict(list)
        for i in range(len(nums)):
            di[nums[i]].append(i)
        n=len(queries)
        ans=[-1]*n
        m=len(nums)
        for i in range(n):
            distance=float('inf')
            for j in di[nums[queries[i]]]:
                k=min((j - queries[i]) % m, (queries[i] - j) % m)
                if j!=queries[i] and k<distance:
                    ans[i]=k
                    distance=k
        return ans
#时间复杂度太高了，要优化。
#事实上，就是左右两个中的最短距离，只要在边界上再加一个边界即可。
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        di = defaultdict(list)
        for i in range(len(nums)):
            di[nums[i]].append(i)
        n = len(queries)
        ans = [-1] * n
        m = len(nums)
        for k in di.values():
            t = k[0]
            k.insert(0, k[-1] - m)
            k.append(t + m)
        for i in range(n):
            if len(di[nums[queries[i]]]) == 3:
                continue
            j = bisect_left(di[nums[queries[i]]], queries[i])
            ans[i] = min(queries[i] - di[nums[queries[i]]][j - 1], di[nums[queries[i]]][j + 1] - queries[i])
        return ans
