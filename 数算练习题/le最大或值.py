#异或的话如下：
class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
            a=0
            for i in nums:
                a^=i
            ans=0
            for i in nums:
                ans=max(ans,a^i^(i<<k))
            return ans
#题目看错了，要求的是或值
class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        total_or = 0
        for num in nums:
            total_or |= num  # 计算整个数组的 OR 值

        ans = 0
        for num in nums:
            without_num = total_or & ~num  # 去掉当前 num 的 OR 贡献
            new_or = without_num | (num << k)  # 计算替换后的 OR
            ans = max(ans, new_or)  # 取最大值

        return ans
#这个又有问题，事实上这个去除贡献的方法在一些情况下有bug，所以只能用前缀和后缀处理