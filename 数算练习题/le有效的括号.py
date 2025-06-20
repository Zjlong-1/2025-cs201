#有一点小坑，考虑（{）}，这种情况，感觉枚举是不行的，只能用栈来实现
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        di = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack=[]
        for i in s:
            if s in di:
                if not stack or stack[-1]!=di[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return not stack