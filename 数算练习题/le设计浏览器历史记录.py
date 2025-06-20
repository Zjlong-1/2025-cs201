#用双向链表：
class Node:
    def __init__(self, val=None, pre=None, next=None):
        self.val = val
        self.next = None
        self.pre = None


class BrowserHistory:
    def __init__(self, homepage: str):
        self.cur = Node(homepage)

    def visit(self, url: str) -> None:
        self.cur.next = Node(url)
        self.cur.next.pre = self.cur
        self.cur = self.cur.next

    def back(self, steps: int) -> str:
        k = self.cur
        while k.pre and steps:
            k = k.pre
            steps -= 1
        self.cur = k
        return k.val

    def forward(self, steps: int) -> str:
        k = self.cur
        while k.next and steps:
            steps -= 1
            k = k.next
        self.cur = k
        return k.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
#关于visit的小优化：

    def visit(self, url: str) -> None:
        self.cur.nxt = DNode(url, self.cur)
        self.cur = self.cur.nxt
        return url


#也可以只是套用oop的写法，用列表实现：
class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]  # 初始化历史记录列表
        self.current = 0           # 当前页面指针

    def visit(self, url: str) -> None:
        # 访问新页面时，删除当前指针之后的所有历史记录
        self.history = self.history[:self.current + 1]
        # 将新页面添加到历史记录中
        self.history.append(url)
        # 更新指针
        self.current += 1

    def back(self, steps: int) -> str:
        # 计算后退后的指针位置
        self.current = max(self.current - steps, 0)
        # 返回后退后的页面
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        # 计算前进后的指针位置
        self.current = min(self.current + steps, len(self.history) - 1)
        # 返回前进后的页面
        return self.history[self.current]