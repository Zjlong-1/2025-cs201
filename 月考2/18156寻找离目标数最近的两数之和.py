def solve():
    t = int(input())
    l = list(map(int, input().split()))
    l.sort()
    n = len(l)
    left = 0
    right = n - 1
    ans = -1
    while left < right:
        mid = l[left] + l[right]
        if abs(t - mid) < abs(t - ans):
            ans = mid
        elif abs(t - mid) == abs(t - ans):
            ans = min(ans, mid)
        if mid < t:
            left += 1
        elif mid==t:
            print(t)
            return
        else:
            right -= 1
    print(ans)
solve()