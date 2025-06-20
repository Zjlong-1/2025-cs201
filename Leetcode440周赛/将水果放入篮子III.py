#与二相比区别在于数据变得十分的大，要用比较精确的算法。
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n=len(fruits)
        tree=[-1]*(4*n)
        def build(idx,l,r):
            if l==r:
                tree[idx]=baskets[l]
                return
            m=(l+r)//2
            build(idx*2,l,m)
            build(idx*2+1,m+1,r)
            tree[idx]=max(tree[idx*2],tree[idx*2+1])
        build(1,0,n-1)
        ans=0
        def f(idx,l,r,x):
            if tree[idx]<x:
                return -1
            m=(l+r)//2
            if r==l:
                tree[idx]=-1
                return x
            k=f(idx*2,l,m,x)
            if k<0:
                k=f(idx*2+1,m+1,r,x)
            tree[idx]=max(tree[idx*2],tree[2*idx+1])
            return k
        for i in fruits:
            if f(1,0,n-1,i)==-1:
                ans+=1
        return ans