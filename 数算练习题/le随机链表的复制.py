"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
#难点在于random我只知道指的是什么，而不知道位置，要在deepcopy中体现是比较棘手的，但是题目数据的呈现就是用索引，所以不妨就依照这样自己弄一个索引（n循环）,写着写着发现还可以简化，不要索引只要一个1：1字典复刻即可。再一想好像又不行，因为还要与新的相关，所以还是要用索引来确定，又想其实可以之间建立新旧之间的联系，又不要索引了。算了，不小丑了，不得不索引。其实真的不要。
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        di={}
        a=head
        new=Node(-1)
        b=new
        while a:
            b.next=Node(a.val)
            b=b.next
            di[a]=b
            a=a.next
        a=head
        b=new.next
        while a:
            if a.random:
                b.random=di[a.random]
            a=a.next
            b=b.next
        return new.next