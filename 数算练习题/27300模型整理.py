from collections import defaultdict
n=int(input())
l=defaultdict(list)
for i in range(n):
    a,b=input().split('-')
    l[a].append((b,float(b[:-1]),ord(b[-1])))
l1=sorted(l)
for k in l1:
    l[k].sort(key=lambda x:(-x[2],x[1]))
    ka=', '.join(l[k][i][0] for i in range(len(l[k])))
    print(f'{k}: {ka}')