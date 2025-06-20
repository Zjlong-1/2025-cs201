#第一次传送的时候传送到的点都是之前没有到的，所以至少是不慢的，多次就没有必要了，之前的传送到了而且所需时间短。
#其实传送门就是吓人的，实际上就是某些点多了一些路径，只能用一次用一次是显然的毕竟找最短距离，所以一遇到就直接用了（这肯定是最优的）其余的部分就是普通的bfs
class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        di=defaultdict(list)
        for i in range(n):
            for j in range(m):
                if 64<ord(matrix[i][j])<91:
                    di[matrix[i][j]].append((i,j))
        vi=[[False]*m for _ in range(n)]
        d=[(0,1),(0,-1),(1,0),(-1,0)]
        q=deque([(0,0,0)])
        if matrix[0][0]!='.':
            for a,b in di[matrix[0][0]]:
                if (a,b)!=(0,0):
                    q.append((a,b,0))
                    vi[a][b]=True
        vi[0][0]=True
        while q:
            x,y,w=q.popleft()
            if (x,y)==(n-1,m-1):
                return w
            for dx,dy in d:
                nx,ny=dx+x,dy+y
                if 0<=nx<n and 0<=ny<m and not vi[nx][ny] and matrix[nx][ny]!='#':
                    if matrix[nx][ny]!='.':
                            for a,b in di[matrix[nx][ny]]:
                                if (a,b)!=(nx,ny):
                                    q.append((a,b,w+1))
                                    vi[a][b]=True
                    vi[nx][ny]=True
                    q.append((nx,ny,w+1))
        return -1

#dfs超时了，感觉还是要要bfs，只是加入其他点之前先考虑穿越
class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        di=defaultdict(list)
        for i in range(n):
            for j in range(m):
                if 64<ord(matrix[i][j])<91:
                    di[matrix[i][j]].append((i,j))
        s=set()
        vi=[[False]*m for _ in range(n)]
        d=[(0,1),(0,-1),(1,0),(-1,0)]
        ans=[]
        def dfs(x,y,w):
            if (x,y)==(n-1,m-1):
                ans.append(w)
                return
            for dx,dy in d:
                nx,ny=dx+x,dy+y
                if 0<=nx<n and 0<=ny<m and not vi[nx][ny] and matrix[nx][ny]!='#':
                    if matrix[nx][ny]!='.':
                        if matrix[nx][ny] not in s:
                            for a,b in di[matrix[nx][ny]]:
                                if (a,b)!=(nx,ny):
                                    s.add(matrix[nx][ny])
                                    dfs(a,b,w+1)
                                    s.remove(matrix[nx][ny])
                    vi[nx][ny]=True
                    dfs(nx,ny,w+1)
                    vi[nx][ny]=False
        if matrix[0][0]!='.':
            for a,b in di[matrix[0][0]]:
                if (a,b)!=(0,0):
                    s.add(matrix[0][0])
                    dfs(a,b,0)
                    s.remove(matrix[0][0])
        vi[0][0]=True
        dfs(0,0,0)
        return min(ans) if ans else -1