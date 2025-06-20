import heapq
from collections import deque
class Node:
    def __init__(self,w,v):
        self.w=w
        self.v=v
        self.left=None
        self.right=None
    def __lt__(self, other):
        if  self.w==other.w:
            return self.v<other.v
        return self.w<other.w
n=int(input())
heap=[]
for _ in range(n):
    v,w=input().split()
    w=int(w)
    heapq.heappush(heap,Node(w,v))
while len(heap)>1:
    a=heapq.heappop(heap)
    b=heapq.heappop(heap)
    merge=Node(a.w+b.w,min(a.v,b.v))
    merge.left=a
    merge.right=b
    heapq.heappush(heap,merge)
root=heap[0]
codes={}

def solve(node,code):
    if not node:
        return
    if not node.left and not node.right :
        codes[node.v]=code
    else:
        solve(node.left,code+'0')
        solve(node.right,code+'1')
solve(root,'')
def h_encode(s):
    ans=''
    for i in s:
        ans+=codes[i]
    return ans
def decode(s):
    ans=''
    node=root
    for i in s:
        if i=='0':
            node=node.left
        else:
            node=node.right
        if not node.left and not node.right:
            ans+=node.v
            node=root
    return ans
while True:
    try:
        s=input()
    except EOFError:
        break
    if s[0]=='0' or s[0]=='1':
        print(decode(s))
    else:
        print(h_encode(s))

