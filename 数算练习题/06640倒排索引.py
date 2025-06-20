#有一个小坑点，要去重
from collections import defaultdict
n=int(input())
di=defaultdict(list)
for i in range(1,n+1):
    word=input().split()
    words=set(word[1:])
    for j in words:
        di[j].append(i)
t=int(input())
for _ in range(t):
    x=input()
    if x in di:
        print(*di[x])
    else:
        print('NOT FOUND')



