def f(l):
    stack = []
    output = []
    di = {'+': 1, '-': 1, '*': 2, '/': 2}
    cnt = 0
    n = len(l)
    while cnt < n:
        if l[cnt].isdigit():
            x = int(l[cnt])
            cnt += 1
            while cnt < n and l[cnt].isdigit():
                x = x * 10 + int(l[cnt])
                cnt += 1
            output.append(x)
        elif l[cnt] == '(':
            stack.append(l[cnt])
            cnt += 1
        elif l[cnt] == ')':
            cnt += 1
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and di[l[cnt]] <= di[stack[-1]]:
                output.append(stack.pop())
            stack.append(l[cnt])
            cnt += 1
    while stack:
        output.append(stack.pop())
    return output
def g(l):
    di = {'+': 1, '-': 1, '*': 2, '/': 2}
    stack = []
    l
    for i in l:
        if i not in di:
            stack.append((i, 4))
        else:
            right, rightv = stack.pop()
            left, leftv = stack.pop()
            curv = di[i]
            if leftv < curv:
                left = f'({left})'
            if rightv < curv :
                right = f'({right})'
            new = f'{left}{i}{right}'
            stack.append((new, curv))
    print(stack[-1][0])
while True:
    try:
        l=input()
    except EOFError:
        break
    g(f(l))
