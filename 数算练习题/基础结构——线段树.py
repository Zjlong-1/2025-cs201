class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)  # 预分配 4n 空间（最坏的情况，每个叶子都只有一片）
        self.build(arr, 1, 0, self.n - 1)  # 从根节点 1 开始构建

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
            return
        mid = (start + end) // 2
        self.build(arr, node * 2, start, mid)  # 左子树
        self.build(arr, node * 2 + 1, mid + 1, end)  # 右子树
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]  # 维护区间和
