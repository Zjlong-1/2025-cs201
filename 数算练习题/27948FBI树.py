class Node:
    def __init__(self,v):
        self.v=v
        self.left=None
        self.right=None
n=int(input())
l1=list(input())
def solve(l):
    if not l:
        return None
    t=len(l)
    if '0' not in l:
        root=Node('I')
    elif '1' not in l:
        root=Node('B')
    else:
        root=Node('F')
    if len(l)==1:
        return root
    left,right=solve(l[:t//2]),solve(l[t//2:])
    root.left=left
    root.right=right
    return root
def h(node):
    if not node.left and not node.right:
        print(node.v,end='')
        return
    if node.left:
        h(node.left)
    if node.right:
        h(node.right)
    print(node.v,end='')
h(solve(l1))

#没有必要建树，直接跳过中间步骤直奔主题：
def construct_FBI_tree(s):
    # 判断当前字符串的类型
    if '0' in s and '1' in s:
        node_type = 'F'
    elif '1' in s:
        node_type = 'I'
    else:
        node_type = 'B'

    if len(s) > 1:  # 如果字符串长度大于1，则继续分割
        mid = len(s) // 2
        # 递归构建左右子树，并将结果按后序遍历拼接
        left_tree = construct_FBI_tree(s[:mid])
        right_tree = construct_FBI_tree(s[mid:])
        return left_tree + right_tree + node_type
    else:  # 如果字符串长度为1，直接返回该节点类型
        return node_type


N = int(input())
s = input()
print(construct_FBI_tree(s))