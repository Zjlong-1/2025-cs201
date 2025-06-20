def solve(s):
    di={'*':1,'/':1,'-':0,'+':0}
    d1={'(',')'}
    stack=[]
    ans=[]
    num=''
    for i in s:
        if i.isdigit() or i=='.':
            num+=i
        else:
            if num:
                ans.append(num)
                num=''
            if i in di:
                while stack and stack[-1] in di and di[stack[-1]]>=di[i]:
                    ans.append(stack.pop())
                stack.append(i)
            elif i=='(':
                stack.append(i)
            elif i==')':
                while stack[-1]!='(':
                    ans.append(stack.pop())
                stack.pop()
    if num:
        ans.append(num)
    while stack :
        ans.append(stack.pop())
    print(' '.join(ans))
n=int(input())
for _ in range(n):
    s=input()
    solve(s)