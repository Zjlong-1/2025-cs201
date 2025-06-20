n=int(input())
stack=[]
while n>=8:
    stack.append(n%8)
    n=n//8
stack.append(n)
ans=''
while stack:
    ans+=str(stack.pop())
print(ans)