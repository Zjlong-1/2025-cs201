from collections import deque
while True:
    n=int(input())
    if n==0:
        break
    def bfs(n):
        q=deque()
        q.append(1)
        while q:
            x=q.popleft()
            if x%n==0:
                print(x)
                return
            q.append(10*x+1)
            q.append(10*x)
    bfs(n)
#bfs的简化时间复杂度，记录加加剪枝：
from collections import deque


def find_smallest_multiple(n):
    # 队列中每个元素为 (当前余数, 构造的数字字符串)
    queue = deque()
    start = 1 % n
    queue.append((start, "1"))
    visited = set([start])

    while queue:
        remainder, num_str = queue.popleft()
        if remainder == 0:
            return num_str

        # 计算加 '0' 后的新余数
        r0 = (remainder * 10) % n
        if r0 not in visited:
            visited.add(r0)
            queue.append((r0, num_str + "0"))

        # 计算加 '1' 后的新余数
        r1 = (remainder * 10 + 1) % n
        if r1 not in visited:
            visited.add(r1)
            queue.append((r1, num_str + "1"))


if __name__ == "__main__":
    while True:
        n = int(input().strip())
        if n == 0:
            break
        print(find_smallest_multiple(n))
