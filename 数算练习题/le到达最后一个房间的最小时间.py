#意思是第多少秒之后门才会打开,这时才能从出发点出发历经1秒到达。
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n,m=len(moveTime),len(moveTime[0])
        dist=[[float('inf')]*m for _ in range(n)]
        di=[(0,1),(0,-1),(1,0),(-1,0)]
        dist[0][0]=0
        heap=[(0,0,0)]
        while heap:
            w,x,y=heapq.heappop(heap)
            if (x,y)==(n-1,m-1):
                return w
            for dx,dy in di:
                nx,ny=dx+x,dy+y
                if 0<=nx<n and 0<=ny<m :
                    t=max(w,moveTime[nx][ny])+1
                    if t<dist[nx][ny]:
                        dist[nx][ny]=t
                        heapq.heappush(heap,(t,nx,ny))