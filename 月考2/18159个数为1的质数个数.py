l=[]
def p(x):
    l1=[True]*(x+1)
    for j in range(2,x+1):
        if l1[j] and j%10==1:
            l.append(j)
        for k in range(j*j,x+1,j):
            l1[k]=False
p(10001)
t=int(input())
for i in range(1,1+t):
    n=int(input())
    print(f'Case{i}:')
    if l[0]>=n:
        print('NULL')
    else:
        for k in l:
            if k<n:
                print(k,end=' ')
        print()


