n, m = map(int, input().split())
a = list(range(1, n + 1))
i = 0
while len(a) > 1:
    i = (i + m - 1) % len(a)
    print(a.pop(i),end=' ')
print(a[0])

