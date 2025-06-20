class Solution:
#难点在于用比较小的时间复杂度来实现前k大元素,事实上关注的前k个最大的，所以用堆实时维护（减去最小的）是比较巧妙的。
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        l=sorted((x,y,i) for i,(x,y) in enumerate(zip(nums1,nums2)))
        n=len(l)
        heap=[]
        ans=[0]*n
        s=0
        for i,(x,y,id) in enumerate(l):
            ans[id]=ans[l[i-1][2]] if i and x==l[i-1][0] else s
            s+=y
            if len(heap)<k:
                heappush(heap,y)
            else:
                s-=heappushpop(heap,y)
        return ans