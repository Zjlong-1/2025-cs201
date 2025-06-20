#一开始卡在每一次都要除以4再取整，不知道最后的操作数具体怎么弄。后来解答说的比较好：
#就是移位操作，转二进制，长度/2取上整。
#而且可以想象最多溢出1
class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        def f(n):
            m=n.bit_length()
            res=sum((i+1)//2<<(i-1) for i in range(1,m))
            return res+(m+1)//2*(n+1-(1<<m>>1))
        return sum((f(r)-f(l-1)+1)//2 for l,r in queries)