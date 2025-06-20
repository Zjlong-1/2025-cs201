s=input().split()
stack=[]
for i in s:
    if i.isdigit():
        stack.append(int(i))
    else:
        a,b=stack.pop(),stack.pop()
        stack.append(eval(f'{b}{i}{a}'))
print(f'{stack[0]:.2f}')

#计算机的运行原理：先转换为波兰表达式，再将波兰表达式进行计算：即只需结合两者
s=input().split()
l=[]
stack=[]
di={'-':1,'+':1,'*':2,'/':2}
for i in s:
    if i in di:
        while stack and di[stack[-1]]>=di[i]:
            l.append(stack.pop())
        stack.append(i)
    else:
        l.append(i)
while stack:
    l.append(stack.pop())
stack1=[]
for i in l:
    if i.isdigit():
        stack1.append(int(i))
    else:
        a,b=stack1.pop(),stack1.pop()
        stack1.append(eval(f'{b}{i}{a}'))
print(f'{stack1[0]:.2f}')