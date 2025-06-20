n=int(input())
stack=[]
cnt=1
ans=0
for _ in range(2*n):
    l=input().split()
    if l[0]=='add':
        stack.append(int(l[-1]))
    else:
        if cnt!=stack[-1]:
            stack.sort(reverse=True)
            ans+=1
        stack.pop()
        cnt+=1
print(ans)
