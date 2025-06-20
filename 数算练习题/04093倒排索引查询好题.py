#基础不扎实，导致被迷惑了好久，None!=set(),一个空的集合是存在的，不是None。事实上,none只是用来判断第一步的
#又犯下了一个基础的错误，列表，集合等赋值要用拷贝，不然的话指的是一个东西，会改变原有的属性
from collections import defaultdict
n=int(input())
di=defaultdict(set)
file=set()
for i in range(n):
    l=list(map(int,input().split()))
    for k in l[1:]:
        di[i].add(k)
        file.add(k)
t=int(input())
for _ in range(t):
    l=list(map(int,input().split()))
    ans=None
    for i in range(n):
        if l[i]==1:
            if ans is None:
                ans=di[i].copy()
            else:
                ans&=di[i]
        elif l[i]==-1:
            if ans is None:
                ans=file.copy()
            ans-=di[i]
    if ans:
        print(*sorted(ans))
    else:
        print('NOT FOUND')


