n=4
def solve(l1, k, id, t):
    if k == 0:
        ans = 0
        for i in range(1, len(l1)):
            ans += (l1[i] - l1[i - 1]) * t[i - 1]
        return ans
    if k > 0 and id == len(t) - 1:
        return float('inf')
    cur1 = solve(l1, k, id + 1, t)
    l1 = l1[:id] + l1[id + 1:]
    t = t[:id] + [t[id] + t[id + 1]] + t[id + 2:]
    cur2 = solve(l1, k - 1, id + 1, t)
    return min(cur1, cur2)
print(solve([0,1,3,4], 2, 1, [2,1,2,5]))

#超时了：
class Solution:
    def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
        def solve(l1,k,id,t):
            if k==0:
                ans=0
                for i in range(1,len(l1)):
                    ans+=(l1[i]-l1[i-1])*t[i-1]
                return ans
            if k>0 and id==len(t)-1:
                return float('inf')
            cur1=solve(l1,k,id+1,t)
            l1=l1[:id]+l1[id+1:]
            t=t[:id]+[t[id]+t[id+1]]+t[id+2:]
            cur2=solve(l1,k-1,id+1,t)
            return min(cur1,cur2)
        return solve(position,k,1,time)