d={'(':0,')':1}
while True:
    try:
        s=input()
    except EOFError:
        break
    stack1=[]
    stack2=[]
    n=len(s)
    ans=[' ']*n
    for i in range(n):
        if s[i] in d:
            if d[s[i]]==0:
                stack1.append(i)
            else:
                if stack1:
                    stack1.pop()
                else:
                    stack2.append(i)
    for i in stack1:
        ans[i]='$'
    for i in stack2:
        ans[i]='?'
    print(s)
    print(''.join(ans))



