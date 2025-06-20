class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [-1] * n
        ma = arr[-1]
        for i in range(-2, -n - 1, -1):
            ma = max(ma, arr[i + 1])
            if ma >= arr[-1]:
                ans[i] = ma
        return ans
#看错题了，但误打误撞对了。题目是说最后一个换为-1，其余的换为右侧最大的

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans=arr[:]
        ans[-1]=-1
        ma=arr[-1]
        for i in range(-2, -n - 1, -1):
            ma = max(ma, arr[i + 1])
            ans[i] = ma
        return ans
#稍微快一点：
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        a = [x for x in arr]
        cur_max = -1
        for i in range(len(a) - 1, -1, -1):
            a[i] = cur_max
            if arr[i] > cur_max:
                cur_max = arr[i]
        return a

