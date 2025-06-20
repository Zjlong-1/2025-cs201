#没事找事，用双端队列去写一下
from collections import deque
def solve(s):
    l=deque(s)
    while len(l)>1:
        a,b=l.popleft(),l.pop()
        if a!=b:
            return False
    return True
while True:
    try :
        n=input()
    except EOFError:
        break
    if solve(n):
        print('YES')
    else:
        print('NO')


