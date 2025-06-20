def solve():
    from collections import deque
    n, p = map(int, input().split())
    ind = [0] * (n + 1)
    ind1 = [0] * (n + 1)
    c = [0] * (n + 1)
    l = [{} for _ in range(n + 1)]
    ans = [0] * (n + 1)
    flag = True
    for i in range(1, 1 + n):
        a, b = map(int, input().split())
        c[i] = a
        ans[i]=b
    for _ in range(p):
        i, j, w = map(int, input().split())
        if i==j:
            print('NULL')
            return
        if j not in l[i]:
            ind[j] += 1
            ind1[j] += 1
            l[i][j] = w
        else:
            l[i][j] += w
    ru=deque([i for i in range(1,n+1) if ind1[i] == 0])
    for i in ru:
        c[i]+=ans[i]
    q = deque([i for i in range(1,n+1) if ind1[i] == 0])
    cnt = 0
    while q:
        x = q.popleft()
        cnt += 1
        for i in l[x]:
            ind1[i] -= 1
            if ind1[i] == 0:
                q.append(i)
    if cnt!=n:
        print('NULL')
        return
    while ru:
        x = ru.popleft()
        c[x]-=ans[x]
        for j in l[x]:
            w = l[x][j]
            ind[j] -= 1
            if c[x]>0:
                c[j] += c[x] * w
            if ind[j] == 0 :
                ru.append(j)

    cnt = 0
    for i in range(1, n + 1):
        if ans[i] > 0 and len(l[i])==0:
            cnt += 1
            print(i, c[i])
    if cnt==0:
        print('NULL')
solve()

