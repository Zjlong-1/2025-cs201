from functools import lru_cache
@lru_cache(maxsize=None)
def f(n,k):
    if n==1:
        return 1
    if (f(n-1,k)+k)%n==0:
        return n
    else:
        return (f(n-1,k)+k)%n
while True:
    a,b=map(int,input().split())
    if a==b==0:
        break
    print(f(a,b))
#或者双端队列直接模拟：
from collections import deque

# 先使用pop从列表中取出，如果不符合要求再append回列表，相当于构成了一个圈
def hot_potato(name_list, num):
    queue = deque()
    for name in name_list:
        queue.append(name)

    while len(queue) > 1:
        for i in range(num):
            queue.append(queue.popleft()) # O(1)
        queue.popleft()
    return queue.popleft()


while True:
    n, m = map(int, input().split())
    if {n,m} == {0}:
        break
    monkey = [i for i in range(1, n+1)]
    print(hot_potato(monkey, m-1))