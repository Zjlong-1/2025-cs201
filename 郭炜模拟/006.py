import math
n=int(input())
def f(t):
    return int((math.isqrt(1 + 8* n) - 1) // 2)
print(f(n))