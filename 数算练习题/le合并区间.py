#和cs101中挤牛奶是一样的
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #列表中的列表排序
        intervals.sort(key=lambda x:x[0])
        ans=[]
        for i in intervals:
            if not ans or ans[-1][-1]<i[0]:
                ans.append(i)
            else:
                ans[-1][-1]=max(ans[-1][-1],i[1])
        return ans