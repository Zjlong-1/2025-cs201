# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x=y=0
        a,b=l1,l2
        cnt1=cnt2=0
        while a:
            x+=a.val*(10**cnt1)
            a=a.next
            cnt1+=1
        while b:
            y+=b.val*(10**cnt2)
            cnt2+=1
            b=b.next
        k=x+y
        ans=ListNode(k%10)
        k//=10
        t=ans
        while k!=0:
            t.next=ListNode(k%10)
            t=t.next
            k//=10
        return ans
#还可以一个while循环一起处理：
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry //= 10
        return dummy.next
