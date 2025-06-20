#后面两个直接暴力模拟都超时了，虽然加了二分，但是每次判断都要O(n)，所以超时
#考虑一次判断，不断更新，最后由尾部推出整个列表
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n=len(skill)
        t=[0]*n
        for m in mana:
            s=0
            for x,y in zip(skill,t):
                if y>s:
                    s=y
                s+=m*x
            t[-1]=s
            for i in range(n-2,-1,-1):
                s-=skill[i+1]*m
                t[i]=s
        return t[-1]


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n=len(skill)
        m=len(mana)
        pre=[0]*(n+1)
        for i in range(n):
            pre[i+1]=pre[i]+skill[i]
        def pan(mid,start,cnt):
            for i in range(n):
                if mid+pre[i]*mana[cnt]<start+pre[i+1]*mana[cnt-1]:
                    return False
            return True
        def solve(cnt,start,ans):
            if cnt==m:
                return ans
            left,right=start,ans
            while left<right:
                mid=(left+right)//2
                if pan(mid,start,cnt):
                    right=mid
                else:
                    left=mid+1
            return solve(cnt+1,left,left+pre[-1]*mana[cnt])
        return solve(1,0,pre[-1]*mana[0])
#和：
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        m = len(mana)
        t = [0] * (n + 1)
        for i in range(n):
            t[i + 1] = t[i] + skill[i] * mana[0]

        def pan(mid, t, cnt):
            for i in range(n):
                if mid < t[i + 1]:
                    return False
                mid += skill[i] * mana[cnt]
            return True

        def solve(cnt, t):
            if cnt == m:
                return t[-1]
            left, right = t[0], t[-1]
            while left < right:
                mid = (left + right) // 2
                if pan(mid, t, cnt):
                    right = mid
                else:
                    left = mid + 1
            t[0] = left
            for i in range(n):
                t[i + 1] = t[i] + skill[i] * mana[cnt]
            return solve(cnt + 1, t)

        return solve(1, t)
