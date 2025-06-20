# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        new=head.next
        head.next=self.swapPairs(new.next)
        new.next=head
        return new
#也可以直接循环
#事实上本题最重要的就是要时刻记住没法添加头，只能接尾巴，可以一开始有不想要的尾巴，只要重新接上新的即可
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        Head=ListNode()
        Head.next=head
        cur=Head
        while cur.next and cur.next.next:
            new=cur.next.next
            temp=cur.next
            cur.next=new
            temp.next=new.next
            new.next=temp
            cur=temp
        return Head.next