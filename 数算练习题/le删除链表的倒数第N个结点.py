# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt=0
        x=head
        while x:
            x=x.next
            cnt+=1
        t=0
        x=head
        if cnt==1:
            return
        if cnt==n:
            return head.next
        for _ in range(cnt-1-n):
            x=x.next
        x.next=x.next.next
        return head