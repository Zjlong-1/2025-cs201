class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m=len(strs)
        right=min(len(s) for s in strs)
        def can(x):
            for i in strs:
                if i[:x]!=strs[0][:x]:
                    return False
            return True
        left=0
        while left<right:
            mi=(left+right+1)//2
            if can(mi):
                left=mi
            else:
                right=mi-1
        return strs[0][:left]