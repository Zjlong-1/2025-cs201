class Node:
    def __init__(self):
        self.child={}
t=int(input())
for _ in range(t):
    n=int(input())
    root=Node()
    l=[input() for i in range(n)]
    l.sort(reverse=True)
    ans=0
    for s in l:
        def solve(root,s):
            for i in s:
                if i not in root.child:
                    return 0
                root=root.child[i]
            return 1
        ans+=solve(root,s)
        node=root
        for i in s:
            if i not in node.child:
                node.child[i]=Node()
            node=node.child[i]
    if ans>0:
        print('NO')
    else:
        print('YES')
#自己实现的：
t=int(input())
for _ in range(t):
    s = {}
    s2 = s
    n=int(input())
    l=[input() for i in range(n)]
    l.sort(reverse=True)
    for j in l[0]:
        s2[j]={}
        s2=s2[j]
    def solve():
        for i in l[1:]:
            flag = True
            s1 = s
            for j in range(len(i)):
                if i[j] not in s1:
                    flag = False
                    s1[i[j]] = {}
                    s1 = s1[i[j]]
                    for k in range(j + 1, len(i)):#还可以这样：if i[j] not in s1:
                        s1[i[k]] = {}             #       flag=True
                        s1 = s1[i[k]]             #      s1[i[j]] = {}
                    break                           #然后直接继续循环，反正是空的，所以每次第一个if都成立
                else:
                    s1=s1[i[j]]

            if flag:
                print('NO')
                return
        print('YES')
    solve()




