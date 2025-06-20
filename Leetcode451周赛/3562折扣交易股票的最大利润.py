#这个题目有点难，DP+dfs
max=lambda a,b:b if b>a else a#卡常数，不然还过不了
class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        l=[[] for _ in range(n)]
        for x,y in hierarchy:
            l[x-1].append(y-1)
        def dfs(x):
            la=[[0,0] for _ in range(budget+1)]#先不管优惠，之后再补上
            for y in l[x]:
                ly=dfs(y)
                for j in range(budget,-1,-1):
                    for i in range(j+1):
                        for k in range(2):
                            la[j][k]=max(la[j][k],la[j-i][k]+ly[i][k])
            ans=[[0,0] for _ in range(budget+1)]
            for j in range(budget+1):
                for k in range(2):
                    cost=present[x]//(k+1)
                    if j>=cost:
                        ans[j][k]=max(la[j][0],la[j-cost][1]+future[x]-cost)
                    else:
                        ans[j][k]=la[j][0]
            return ans
        return dfs(0)[budget][0]
#快50倍的算法：
class Solution:
    def __init__(self):
        self.budget = None
        self.future = None
        self.present = None
        self.pre1 = {}
        self.pre0 = {}

    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        adj = [[] for _ in range(n + 1)]
        for u, v in hierarchy:
            adj[u].append(v)

        self.present = present
        self.future = future
        self.budget = budget

        def cal(y):
            if not y:
                return []
            y.sort(key=lambda x: (x[0], -x[1]))
            ans = []
            a, b = y[0]
            ans.append((a, b))
            for a0, b0 in y[1:]:
                if a0 == a:
                    if b0 > b:
                        ans[-1] = (a0, b0)
                        b = b0
                elif a0 > a:
                    if b0 > b:
                        ans.append((a0, b0))
                        a = a0
                        b = b0
            return ans

        def merge_adj(u, t):
            ans = [(0, 0)]
            for v in adj[u]:
                tmp = []
                for c1, p1 in ans:
                    for c2, p2 in generate_options(v, t):
                        if c1 + c2 <= self.budget:
                            tmp.append((c1 + c2, p1 + p2))
                tmp = cal(tmp)
                ans = tmp
                if not ans:
                    break
            return ans

        def generate_options(u, s):
            if s == 0 and u in self.pre0:
                return self.pre0[u]
            if s == 1 and u in self.pre1:
                return self.pre1[u]
            cost = self.present[u - 1]
            if s == 1:
                cost = self.present[u - 1] // 2
            tmp = []
            for c, p in merge_adj(u, 1):
                if cost + c <= self.budget:
                    tmp.append((cost + c, self.future[u - 1] - cost + p))
            tmp = cal(tmp)
            ans = cal(merge_adj(u, 0) + tmp)

            if s == 0:
                self.pre0[u] = ans
            else:
                self.pre1[u] = ans
            return ans

        options = generate_options(1, 0)
        res = 0
        for i, j in options:
            if i <= self.budget and j > res:
                res = j
        return res
#另一个快的：
class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        graph = defaultdict(list)
        for _u, _v in hierarchy:
            graph[_u-1].append(_v-1)

        def merge(f1, f2):
            f = defaultdict(lambda: -inf)
            for b1 in f1:
                for b2 in f2:
                    if b1 + b2 <= budget and f[b1+b2] < f1[b1] + f2[b2]:
                        f[b1 + b2] = f1[b1] + f2[b2]
            return f

        @cache
        def dfs(u: int, pb: int):
            cost = present[u] // (pb + 1)
            f = defaultdict(lambda: -inf)
            f[0] = 0
            # 不买当前的最大收益
            for child in graph[u]:
                f = merge(f, dfs(child, 0))
            if cost <= budget:
                dp = defaultdict(lambda: -inf)
                dp[cost] = future[u] - cost
                for child in graph[u]:
                    dp = merge(dp, dfs(child, 1))
                for b in dp:
                    if f[b] < dp[b]:
                        f[b] = dp[b]
            return f

        return max(dfs(0, 0).values())


#本来想要dijkstra来实现，每两个点都建立边，只是上下级的边有优惠，但是没有很好的办法使它每个点至多只走一次
#所以还是没有成功
class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        l=[{} for i in range(n)]
        for i in hierarchy:
            l[i[0]-1][i[1]-1]=(present[i[1]-1]/2,future[i[1]-1])
        for i in range(n):
            for j in range(n):
                if i!=j and j not in l[i]:
                    l[i][j]=(present[j],future[j])
        heap=[(-future[i]+present[i],i,present[i]) for i in range(n) if present[i]<=budget]
        heapify(heap)
        ans=0
        while heap:
            w,u,cost=heappop(heap)