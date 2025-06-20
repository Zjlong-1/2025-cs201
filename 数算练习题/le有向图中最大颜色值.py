# 实际上可以用拓扑排序把所有的路径遍历一遍但是没有显性的表达式,所以要用dp来统计，着十分巧妙。
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        ind = [0] * n
        l = [[] for _ in range(n)]
        la = [[0] * 26 for _ in range(n)]  # 以v为结束点时每一个字母出现的最大次数
        for a, b in edges:
            l[a].append(b)
            ind[b] += 1
        cnt = 0
        q = deque([i for i in range(n) if ind[i] == 0])
        while q:
            a = q.popleft()
            la[a][ord(colors[a]) - ord('a')] += 1
            cnt += 1
            for i in l[a]:
                ind[i] -= 1
                for c in range(26):
                    la[i][c] = max(la[i][c], la[a][c])
                if ind[i] == 0:
                    q.append(i)
        if cnt == n:
            ans = 0
            for i in range(n):
                ans = max(ans, max(la[i]))
            return ans
        else:
            return -1
