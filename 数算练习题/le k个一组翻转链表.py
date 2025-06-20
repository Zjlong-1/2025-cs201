# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#k如果比较大的话用while循环会绕死，所以直接干脆递归
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cnt=1
        temp=head
        while temp and cnt<k:
            temp=temp.next
            cnt+=1
        if not temp or cnt<k:
            return head
        x=self.reverseKGroup(temp.next,k)
        temp.next=None
#到这里就是反转head了
        b=x
        a=head
        while a:
            a.next,b,a=b,a,a.next
        return b
#有之前反转链表的经历，所以这个做的还是比较顺利的
#对于链表最大的认识就是，a.next是一种操作而不是赋值，就像append一样