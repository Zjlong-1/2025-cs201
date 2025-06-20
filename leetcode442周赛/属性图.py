class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        def intersect(a,b):
            a1,b1=set(a),set(b)
            return len(a1)+len(b1)-len(a1|b1)>=k
        n=len(properties)
        s=[i for i in range(n)]
        def f(x):
            if x!=s[x]:
                s[x]=f(s[x])
            return s[x]
        ans=0
        ins=set()
        for i in range(n):
            for j in range(i,n):
                if intersect(properties[i],properties[j]):
                    x,y=f(i),f(j)
                    if x!=y:
                        s[x]=y
        for i in range(n):
            if f(i) not in ins:
                ans+=1
                ins.add(f(i))
        return ans