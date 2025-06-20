#没想到直接用栈就可以处理了，遇到更小的就Pop
n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    s=str(a)
    stack=[]
    for i in s:
        while stack and b and stack[-1]>i:
            stack.pop()
            b-=1
        stack.append(i)
    while b:
        stack.pop()
        b-=1
    print(int(''.join(stack)))