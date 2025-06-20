import heapq
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.l=[]
    def __lt__(self, other):
        return self.val<other.val
n=int(input())
s={}
s1=set()
la=[]
for _ in range(n):
    l1=list(map(int,input().split()))
    la.append(l1[0])
    if l1[0] not in s:
        s[l1[0]]=TreeNode(l1[0])
    for i in range(1,len(l1)):
        if l1[i] not in s:
            s[l1[i]]=TreeNode(l1[i])
        s1.add(l1[i])
        heapq.heappush(s[l1[0]].l,s[l1[i]])
t=-1
for i in la:
    if i not in s1:
        t=i
        break
root=s[t]
def dfs(node):
    flag=False
    while node.l:
        x=heapq.heappop(node.l)
        if x.val>node.val and not flag:
            flag=True
            print(node.val)
        dfs(x)
    if not flag:
        print(node.val)
dfs(root)
#要细心！！！