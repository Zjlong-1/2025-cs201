class Node:
    def __init__(self,data,val,next=None):
        self.data,self.next,self.val=data,next,val
n,m=map(int,input().split())
nodea=Node(-1,-1)
nodeb=Node(-1,-1)
a,b=nodea,nodeb
for _ in range(n):
    x=input()
    y=int(input())
    a.next=Node(x,y)
    a=a.next
for _ in range(m):
    x=input()
    y=int(input())
    b.next=Node(x,y)
    b=b.next
n=int(input())
for _ in range(n):
    x = input()
    y = int(input())
    if y<nodea.next.val:
        k=nodea.next
        nodea.next=Node(x,y)
        nodea.next.next=k
    else:
        a=nodea.next
        while a and a.next and not a.val<y<a.next.val:
            a=a.next
        if a.next:
            k=a.next
            a.next=Node(x,y)
            a.next.next=k
        else:
            a.next=Node(x,y)
a,b=nodea.next,nodeb.next
while a and b:
    if a.val<b.val:
        print(a.data+' '+str(a.val))
        a=a.next
    else:
        print(b.data + ' ' + str(b.val))
        b= b.next
while a:
    print(a.data + ' ' + str(a.val))
    a = a.next
while b:
    print(b.data + ' ' + str(b.val))
    b = b.next

