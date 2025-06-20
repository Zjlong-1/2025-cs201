#最外面的如果有问题就必须得换，所以外面一层一层换，直接不断缩小。就是从左开始，一有异常就必须换，不管和谁换，反正将左括号换完之后右括号自动补全
class Solution:
    def minSwaps(self, s: str) -> int:
        ans=0
        cnt=0
        for x in s:
            cnt+=1 if x=='[' else -1
            if cnt<0:
                cnt=1
                ans+=1
        return ans
#另一种神思路：将配对好的都丢掉，剩下的就是要换的
class Solution:
    def minSwaps(self, s: str) -> int:
        # x记录当前未匹配的左括号的数量
        x = 0
        for c in s:
            # 如果c是左括号，x加1
            if c == "[":
                x = x + 1
            # 如果c是右括号，并且x大于0，那么右括号与最近的一个左括号匹配，即x减1
            elif x > 0:
                x = x - 1
        # 遍历结束后，得到的一定是形如 "]]]...[[[..."的字符串
        # 我们再贪心地每次将两端的括号交换，这样一次可以消去 2 个不匹配的左括号
        return (x + 1) // 2