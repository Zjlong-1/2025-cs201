n,k=map(int,input().split())
l1=[]
for i in range(n):
    a,b=map(int,input().split())
    l1.append((a,b,i+1))
l1.sort(key=lambda x:-x[0])
l1=l1[:k]
l1.sort(key=lambda x:-x[1])
print(l1[0][-1])