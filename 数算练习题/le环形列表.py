# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s=set()
        while head:
            if head in s:
                return True
            s.add(head)
            head=head.next
        return False
#还可以用快慢指针来节省空间
#基于一个比较显然的事实，如果有环的话，两个不同速度的指针一定会再次相遇
#没有环就都走到尽头：
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast,slow=head,head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if slow == fast:
                return True
        return False
