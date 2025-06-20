t=int(input())
for _ in range(t):
    stack = []
    output = []
    di = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    l = input()
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
            cnt+=1
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
    print(' '.join(map(str,output)))