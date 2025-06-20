from functools import lru_cache
@lru_cache(maxsize=None)
def solve(t,mi):
    k=1
    if t<mi:
        return 0
    if t==mi:
        return 1
    for i in range(mi,t):
        if t%i==0:
            k+=solve(t//i,i)
    return k
n=int(input())
for _ in range(n):
    t=int(input())
    print(solve(t,2))
