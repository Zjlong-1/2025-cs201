import heapq
from collections import deque
n=int(input())
l=list(map(int,input().split()))
class Node:
    def __init__(self,w):
        self.w=w
        self.left=None
        self.right=None
    def __lt__(self, other):
        return self.w<other.w
heap=[Node(i) for i in l]
heapq.heapify(heap)
while len(heap)>1:
    a=heapq.heappop(heap)
    b=heapq.heappop(heap)
    merge=Node(a.w+b.w)
    merge.left=a
    merge.right=b
    heapq.heappush(heap,merge)
root=heap[0]
q=deque()
q.append((root,0))
ans=0
while q:
    node,d=q.popleft()
    if node.left:
        q.append((node.left,d+1))
    if node.right:
        q.append((node.right,d+1))
    if not node.right and not node.left:
        ans+=node.w*d
print(ans)
#还可以根据原理节省树的代码：
import heapq

def min_weighted_path_length(n, weights):
    heapq.heapify(weights)
    total = 0
    while len(weights) > 1:
        a = heapq.heappop(weights)
        b = heapq.heappop(weights)
        combined = a + b
        total += combined
        heapq.heappush(weights, combined)
    return total

# 读取输入
n = int(input())
weights = list(map(int, input().split()))
print(min_weighted_path_length(n, weights))
