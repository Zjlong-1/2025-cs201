n=int(input())
d={'+','/','-','*'}
for _ in range(n):
    s=input().split()
    stack=[]
    for i in s:
        if i not in d:
            stack.append(float(i))
        else:
            b,a=stack.pop(),stack.pop()
            stack.append(eval(f'{a}{i}{b}'))
    print(f'{stack[0]:.2f}')
