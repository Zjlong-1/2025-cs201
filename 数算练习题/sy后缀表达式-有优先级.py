#事实上，我们只要注意到9 8 + 2 3 + *是一个合法的波兰表达式就比较好了，波兰表达式的优先级也可以通过分段来体现
#还有一个比较主要的点在于在加减乘除中只有两种优先级，而且加减与前面的无关，两不同优先级相遇可以把括号前面的全部pop掉
#1点也可以用于理解两个**，*/相遇的处理，分堆
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
print(' '.join(l))

#加括号升级版：
def infix_to_postfix(expression):
    # 定义操作符优先级
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    operators = set(precedence.keys())
    output = []  # 存储后缀表达式
    stack = []  # 存储操作符

    # 将输入字符串分割为标记（操作数、操作符、括号）
    tokens = expression.split()

    for token in tokens:
        if token.isdigit():  # 如果是操作数，直接加入到输出
            output.append(token)
        elif token == '(':
            stack.append(token)  # 左括号直接入栈
        elif token == ')':
            # 右括号则弹出栈中操作符，直到遇到左括号
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # 弹出左括号
        elif token in operators:
            # 比较当前操作符与栈顶操作符的优先级
            while stack and stack[-1] in operators and precedence[token] <= precedence[stack[-1]]:
                output.append(stack.pop())
            stack.append(token)  # 当前操作符入栈

    # 将栈中剩余操作符加入到输出
    while stack:
        output.append(stack.pop())

    return ' '.join(output)


# 测试示例
expression = "3 + 5 * ( 2 - 8 )"
print(infix_to_postfix(expression))  # 输出: "3 5 2 8 - * +"
