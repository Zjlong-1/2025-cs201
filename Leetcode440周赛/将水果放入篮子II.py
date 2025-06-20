#看错题了，可以放就一定放。事实上，有一点小丑，有贪心的思想知道前面可以的话就直接放（反正贡献都是1），所以有就放就是最后的答案，没必要dfs恶心自己。要是要dfs这个题目加大数据直接是tough了
#其实也不小丑，贪心不对，是题目要求必须放。
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n=len(baskets)
        l=[1]*n
        ans=[]
        @lru_cache(maxsize=None)
        def dfs(i):
            if i==n:
                ans.append(sum(l))
                return
            for j in range(n):
                if fruits[i]<=baskets[j] and l[j]:
                    l[j]=0
                    dfs(i+1)
                    l[j]=1
                    break
            dfs(i+1)
        dfs(0)
        return min(ans)