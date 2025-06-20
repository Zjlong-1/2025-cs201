l=input().split()
di={'+':1, '-':1, '*':2, '/':2, '^':3}
stack=[]
for i in l:
    if i not in di:
        stack.append((i,4))
    else:
        right,rightv=stack.pop()
        left,leftv=stack.pop()
        curv=di[i]
        if leftv<curv:#优先级小，加括号
            left=f'({left})'
        if rightv<curv or (i=='^' and curv==rightv):
            right=f'({right})'
        new=f'{left}{i}{right}'
        stack.append((new,curv))
print(stack[-1][0])
