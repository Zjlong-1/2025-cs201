#一开始看错题目了，可以隔着指
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        q = deque([root])  # 初始化队列，开始处理层序遍历

        while q:
            n = len(q)  # 当前层的节点数

            for i in range(n):
                t = q.popleft()  # 取出当前节点

                # 将当前节点的 next 指向队列中的下一个节点（如果不是当前层的最后一个节点）
                if i < n - 1:
                    t.next = q[0]  # 当前节点的 next 指向队列中的下一个节点

                # 把左子节点和右子节点加入队列
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)

        return root