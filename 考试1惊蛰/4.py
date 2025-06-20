l=[[0]*1025 for i in range(1025)]
d=int(input())
for _ in range(int(input())):
    x,y,i=map(int,input().split())
    for k in range(max(x-d,0),min(x+d+1,1025)):
        for j in range(max(y-d,0),min(y+d+1,1025)):
            l[k][j]+=i
t=-1
for i in l:
    for j in i:
        if j>t:
            a=1
            t=j
        elif j==t:
            a+=1
print(str(a)+' '+str(t))