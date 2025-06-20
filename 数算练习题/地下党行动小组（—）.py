class Node:
    def __init__(self,data,val,next=None):
        self.data,self.next,self.val=data,next,val
n,m=map(int,input().split())
nodea=Node(-1,-1)
nodeb=Node(-1,-1)
a,b=nodea,nodeb
for _ in range(n):
    x=input()
    y=input()
    a.next=Node(x,y)
    a=a.next
for _ in range(m):
    x=input()
    y=input()
    b.next=Node(x,y)
    b=b.next
x=input()
a=nodea.next
b=nodeb.next
y=input()
if x=='A':
    while a.data!=y:
        a=a.next
    print(a.next.data+' '+a.next.val)
else:
    while b.data!=y:
        b=b.next
    print(b.next.data+' '+b.next.val)