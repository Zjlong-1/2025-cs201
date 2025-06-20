class Node:
    def __init__(self, data, next=None):
        self.data, self.next = data, next

class LinkList:
    def __init__(self):
        self.head = None

    def initList(self, data):
        self.head = Node(data[0])
        p = self.head
        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next
    def insertCat(self):
        length = 0
        p = self.head
        while p:
            length += 1
            p = p.next
        mid = (length + 1) // 2
        cat = Node(6)
        p = self.head  # 注意这里应该是从 head 开始，而不是 `self.next`
        for _ in range(mid - 1):
            p = p.next
        cat.next = p.next
        p.next = cat

    def printLk(self):
        p = self.head
        while p:
            print(p.data, end=" ")
            p = p.next
            print()

lst = list(map(int,input().split()))
lkList = LinkList()
lkList.initList(lst)
lkList.insertCat()
lkList.printLk()