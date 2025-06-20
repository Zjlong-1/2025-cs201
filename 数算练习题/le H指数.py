class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l=sorted(citations,reverse=True)
        def pan(h):
            return l[h-1]>=h
        n=len(l)
        left,right=0,n
        while left<right:
            mi=(left+right+1)//2
            if pan(mi):
                left=mi
            else:
                right=mi-1
        return left