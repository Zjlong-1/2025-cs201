#有点无语了，leetcode上tough全是dp
class Solution:
    def lexicographicallySmallestString(self, s: str) -> str:
        def can(a,b):
            d=abs(ord(a)-ord(b))
            return d==1 or d==25
        n=len(s)
        ca=[[False]*n for _ in range(n)]
        for i in range(n-2,-1,-1):
            ca[i+1][i]=True
            for j in range(i+1,n):
                if can(s[i],s[j]) and ca[i+1][j-1]:
                    ca[i][j]=True
                    continue
                for k in range(i+1,j-1):
                    if ca[i][k] and ca[k+1][j]:
                        ca[i][j]=True
                        break
        la=['']*(n+1)
        for i in range(n-1,-1,-1):
            cur=s[i]+la[i+1]
            for j in range(i+1,n):
                if ca[i][j]:
                    cur=min(cur,la[j+1])
            la[i]=cur
        return la[0]