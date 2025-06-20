# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#一开始想的是第二个之后的都与第一个来一次merge，但这没有merge的精髓，肯定是二分两个两个弄（1/2的i次方求和）但细想两者好像差不多。
        if len(lists)==0:
            return None
        if len(lists)==1:
            return lists[0]
        def merge(a,b):
            t=ListNode()
            k=t
            while a and b:
                if a.val>b.val:
                    k.next=b
                    b=b.next
                else:
                    k.next=a
                    a=a.next
                k=k.next
            if a:
                k.next=a
            if b:
                k.next=b
            return t.next
        ans=lists[0]
        for i in range(1,len(lists)):
            ans=merge(ans,lists[i])
        return ans
#还是太小瞧分治了，虽然递归或者处理的次数一样，但是处理的长度不一样，分治每一次又是n,但是这个以一个为基点的方法，长度一直增加
#O(n)+O(2n)+O(3n)+...+O(kn)
#分治法：
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergetwo(self,l1,l2):
        cur=dum=ListNode()
        while l1 and l2:
            if l1.val<l2.val:
                cur.next=l1
                l1=l1.next
            else:
                cur.next=l2
                l2=l2.next
            cur=cur.next
        cur.next=l1 if l1 else l2
        return dum.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        m=len(lists)
        if m==0:
            return None
        if m==1:
            return lists[0]
        left=self.mergeKLists(lists[:m//2])
        right=self.mergeKLists(lists[m//2:])
        return self.mergetwo(left,right)

#还可以用堆来实现
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
ListNode.__lt__ = lambda x,y: x.val < y.val#非常重要的一步，定义大小
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = [ head for head in lists if head]
        heapify(h)
        dummy = cur = ListNode()
        while h:
            node = heappop(h)
            if node.next:
                heappush(h, node.next)
            cur.next = node
            cur = cur.next
        return dummy.next
