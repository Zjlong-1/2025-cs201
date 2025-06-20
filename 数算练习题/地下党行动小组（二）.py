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
n=int(input())
for _ in range(n):
    x,y=input().split()
    if x=='A':
        a=nodea
        while a.next.data!=y:
            a=a.next
        a.next=a.next.next
    if x=='B':
        b=nodeb
        while b.next.data!=y:
            b=b.next
        b.next=b.next.next
a=nodea.next
while a:
    print(a.data,end=' ')
    a=a.next
print()
b=nodeb.next
while b:
    print(b.data,end=' ')
    b=b.next
