class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        l = [[] for _ in range(n)]
        for i in flights:
            l[i[0]].append((i[1], i[2]))
        heap = [(0, src, -1)]
        vi = set()
        while heap:
            c, u, cnt = heapq.heappop(heap)
            if cnt > k:
                continue
            vi.add((u, cnt))
            if u == dst:
                return c
            if cnt == k:
                continue
            for v, w in l[u]:
                if (v, cnt + 1) in vi:
                    continue
                heapq.heappush(heap, (w + c, v, cnt + 1))
        return -1
#超时了，事实上用的vi条件还是太强了,用值来判断会好很多：
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        dct = defaultdict(dict)
        for a, b, p in flights:
            dct[a][b] = p

        visit = [n+1]*n
        stack = [[0, src, 0]]
        heapq.heapify(stack)
        while stack:
            cost, pos, cnt = heapq.heappop(stack)
            if pos == dst:
                return cost
            if cnt >= visit[pos] or cnt > k:#这是因为上界实际上是k+1,所以要终点前的都小于等于k
                continue
            visit[pos] = cnt
            for nex in dct[pos]:
                heapq.heappush(stack, [cost+dct[pos][nex], nex, cnt+1])
        return -1
#还可以类似bfs用中转站排序：
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = [[] for _ in range(n)]
        for i, j, w in flights:
            g[i].append((j, w))
        k += 1

        dis = [inf] * n  # money
        dis[src] = 0
        h = [(0, 0, src)]  # 次数，钱，地址

        while h:
            time, cost, dx = heappop(h)

            for y, w in g[dx]:
                new_dis = time + 1
                new_cost = cost + w
                if new_cost < dis[y] and new_dis <= k:
                    dis[y] = new_cost
                    heappush(h, (new_dis, new_cost, y))

        ans = dis[dst]
        return ans if ans < inf else -1
