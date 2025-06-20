#最自然的想法还是用集合：
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s=set()
        while head:
            if head in s:
                return head
            s.add(head)
            head=head.next
        return None
#也可以用双指针节省空间，要注意到速度的两倍比，所以相遇点与头的中点就是环起点

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        slow = fast = head
        while slow.next is not None and fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while head != slow:
                    slow = slow.next
                    head = head.next
                return head
        return None