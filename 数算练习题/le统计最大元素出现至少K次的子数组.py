from collections import deque
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    l = [[]  for _ in range(n + 1)]
    ind=[0]*(n+1)
    for i in range(m):
        x,y=map(int,input().split())
        l[x].append(y)
        ind[y]+=1
    q=deque([i for i in range(1,n+1) if ind[i]==0])
    s=set()
    while q:
        k=q.popleft()
        s.add(k)
        for i in l[k]:
            if i not in s:
                ind[i]-=1
                if ind[i]==0:
                    q.append(i)
    if len(s)==n:
        print('No')
    else:
        print('Yes')
#

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mx = max(nums)
        pos = [-1]
        for i in range(n):
            if nums[i] == mx:
                pos.append(i)
        left, right = 1, k
        ans = 0
        while right < len(pos):
            ans += (pos[left] - pos[left - 1]) * (n - pos[right])
            left += 1
            right += 1
        return ans