def solve():
    n1, m1 = map(int, input().split())
    matrix1 = [list(map(int, input().split())) for _ in range(n1)]
    n2, m2 = map(int, input().split())
    matrix2 = [list(map(int, input().split())) for _ in range(n2)]
    n3, m3 = map(int, input().split())
    matrix3 = [list(map(int, input().split())) for _ in range(n3)]
    if m1!=n2 or n1!=n3 or m2!=m3:
        print('Error!')
        return
    ans = [[0] * m2 for _ in range(n1)]
    for i in range(n1):
        for j in range(m2):
            ans[i][j] = sum(matrix1[i][t] * matrix2[t][j] for t in range(n2)) + matrix3[i][j]
        print(*ans[i])
solve()