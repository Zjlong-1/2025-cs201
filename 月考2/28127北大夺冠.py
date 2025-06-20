m=int(input())
di1={}
di2={}
for _ in range(m):
    a,b,c=input().split(',')
    if a not in di1:
        if c=='yes':
            di1[a]=(1,1,a)
            di2[a]=set()
            di2[a].add(b)
        else:
            di1[a]=(0,1,a)
            di2[a] = set()
    else:
        if c=='yes' and b not in di2[a]:
            di1[a]=(di1[a][0]+1,di1[a][1]+1,a)
            di2[a].add(b)
        elif c=='yes':
            di1[a] = (di1[a][0] , di1[a][1] + 1, a)
        else:
            di1[a]=(di1[a][0], di1[a][1] + 1, a)
l=sorted(di1.values(),key=lambda x:(-x[0],x[1],x[2]))
if len(l)<12:
    for i in range(len(l)):
        print(f'{i+1} {l[i][2]} {l[i][0]} {l[i][1]}')
else:
    for i in range(12):
        print(f'{i+1} {l[i][2]} {l[i][0]} {l[i][1]}')

