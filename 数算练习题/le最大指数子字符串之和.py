class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        def p(x):
            for i in range(2, min(int(x ** 0.5) + 1, x)):
                if x % i == 0:
                    return False
            return x>=2
        sp=set()
        for i in range(len(s)):
            x=0
            for j in s[i:]:
                x=x*10+int(j)
                if p(x):
                    sp.add(x)
        return sum(sorted(sp)[-3:])