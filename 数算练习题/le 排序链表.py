# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#要么全放在一个列表中用sort(这样会比较简单，但是没有了oop链表的精髓)要么就merge sort自己模拟实现（做多了题就比较自然了）
#但是比一般的merge要慢，中点要自己用快慢指针找
#pre是防止死循环的精髓。自己实现的merge，有点爽
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(head):
            if not head or not head.next:
                return head
            slow,fast=head,head
            pre=None
            while fast and fast.next:
                pre=slow
                slow=slow.next
                fast=fast.next.next
            k=merge(slow)
            pre.next=None
            t=merge(head)
            new=ListNode()
            temp=new
            while k and t:
                if k.val<t.val:
                    temp.next=k
                    k=k.next
                else:
                    temp.next=t
                    t=t.next
                temp=temp.next
            if k:
                temp.next=k
            if t:
                temp.next=t
            return new.next
        return merge(head)
#原版没有pre:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 要么全放在一个列表中用sort(这样会比较简单，但是没有了oop链表的精髓)要么就merge sort自己模拟实现（做多了题就比较自然了）
# 但是比一般的merge要慢，中点要自己用快慢指针找
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(head):
            if not head or not head.next:
                return head
            if not head.next.next:
                if head.val > head.next.val:
                    ans = head.next
                    head.next = None
                    ans.next = head
                    return ans
            slow, fast = head, head
            pre = None
            while fast and fast.next:
                pre = slow
                slow = slow.next
                fast = fast.next.next
            k = merge(slow)
            pre.next = None
            t = merge(head)
            new = ListNode()
            temp = new
            while k and t:
                if k.val < t.val:
                    temp.next = k
                    k = k.next
                else:
                    temp.next = t
                    t = t.next
                temp = temp.next
            if k:
                temp.next = k
            if t:
                temp.next = t
            return new.next

        return merge(head)

#无脑写法：
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = []
        pre = head
        while pre:
            cnt.append(pre.val)
            pre = pre.next

        cnt.sort()

        cur = head
        for c in cnt:
            cur.val = c
            cur = cur.next