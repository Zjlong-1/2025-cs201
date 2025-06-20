# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        slow = fast = head

        # 快慢指针找到链表中点
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        # 如果链表长度为奇数，跳过中间节点
        if fast:
            slow = slow.next

        # 比较栈中的值与后半部分链表的值
        while slow:
            if stack.pop() != slow.val:
                return False
            slow = slow.next

        # Definition for singly-linked list.
        # class ListNode:
        #     def __init__(self, val=0, next=None):
        #         self.val = val
        #         self.next = next
        class Solution:
            def isPalindrome(self, head: Optional[ListNode]) -> bool:
                l = []
                while head:
                    l.append(head.val)
                    head = head.next
                return l == l[::-1]
        return True
#快慢指针，速度之比为1：2。也可以用列表来实现：
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l,f=head,head
        stack=[]
        while f and f.next:
            stack.append(l.val)
            l=l.next
            f=f.next.next
        if f :
            l=l.next
        while l:
            if l.val!=stack.pop():
                return False
            l=l.next
        return True
