# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 定义一个 ListNode 类
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 构造链表 1 -> 2 -> 3 -> 4 -> 5 -> None
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a,b=head,None
        while a:
            a.next,b,a=b,a,a.next
        return b
#还可以递归，但是很难理解
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def recur(cur, pre):
            if not cur: return pre  # 终止条件
            res = recur(cur.next, cur)  # 递归后继节点
            cur.next = pre  # 修改节点引用指向
            return res  # 返回反转链表的头节点

        return recur(head, None)  # 调用递归并返回
#第一次弄oop,在我看来直接tough了

