class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def solve(heights):
            stack=[]
            n=len(heights)
            stack.append(0)
            ans=heights[0]
            for i in range(1,n):
                while stack and heights[stack[-1]]>=heights[i]:
                    stack.pop()
                if stack:
                    ans=max((i-stack[-1])*heights[i],ans)
                else:
                    ans=max(ans,(i+1)*heights[i])
                stack.append(i)
            return ans
        return max(solve(heights),solve(heights[::-1]))
#这个只实现了以边界的高度为高的情况，没有考虑中间的情况，如2，1，2
#应该改为pop时计算（左右都有）
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        heights.append(-1)#精髓，大火收汁！！！！
        n=len(heights)
        stack.append(0)
        ans=heights[0]
        for i in range(1,n):
            while stack and heights[stack[-1]]>=heights[i]:
                id=stack.pop()
                if stack:
                    ans=max((i-1-stack[-1])*heights[id],ans)
                else:
                    ans=max(ans,(i)*heights[id])
            stack.append(i)
        return ans
#一个小优化：
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)  # 最后大火收汁，用 -1 把栈清空（-1 可以改成 0）
        st = [-1]  # 在栈中只有一个数的时候，栈顶的「下面那个数」是 -1，对应 left[i] = -1 的情况
        ans = 0
        for right, h in enumerate(heights):
            while len(st) > 1 and h <= heights[st[-1]]:
                i = st.pop()  # 矩形的高（的下标）
                left = st[-1]  # 栈顶下面那个数就是 left
                ans = max(ans, heights[i] * (right - left - 1))
            st.append(right)
        return ans
