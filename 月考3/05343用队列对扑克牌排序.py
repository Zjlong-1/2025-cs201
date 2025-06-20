n=int(input())
l=input().split()
di={'A':0,'B':1,'C':2,'D':3}
d={0:'A',1:'B',2:'C',3:'D'}
l1=[[] for _ in range(10)]
l2=[[]for _ in range(4)]
for i in l:
    l1[int(i[1])].append(i)
    l2[di[i[0]]].append(i)
for i in range(1,10):
    print(f'Queue{i}:',end='')
    print(*l1[i])
for i in range(4):
    print(f'Queue{d[i]}:',end='')
    l2[i].sort()
    print(*l2[i])
l.sort()
print(*l)
