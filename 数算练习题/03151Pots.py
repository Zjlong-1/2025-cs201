#真的没想到是bfs，还以为有数学解法，直接被答案坑了.不同的是要手动把循环写出来
from collections import deque
a,b,c=map(int,input().split())
def bfs():
    inq = set()
    q = deque()
    q.append((0, 0, []))
    inq.add((0,0))
    while q:
        i,j,l=q.popleft()
        if i==c or j==c:
            print(len(l))
            for k in l:
                print(k)
            return
        if i<a and (a,j) not in inq:
            q.append((a,j,l+['FILL(1)']))
            inq.add((a,j))
        if j<b and (i,b) not in inq:
            q.append((i,b,l+['FILL(2)']))
            inq.add((i,b))
        if i>0 and (0,j) not in inq:
            q.append((0,j,l+['DROP(1)']))
            inq.add((0,j))
        if j>0 and (i,0) not in inq:
            q.append((i,0,l+['DROP(2)']))
            inq.add((i,0))
        if i<a and j>0:
            if a-i>j and (i+j,0) not in inq:
                q.append((i+j,0,l+['POUR(2,1)']))
                inq.add((i+j,0))
            if a-i<=j and (a,i+j-a) not in inq:
                q.append((a,j+i-a,l+['POUR(2,1)']))
        if j<b and i>0:
            if b-j>i and (0,i+j) not in inq:
                q.append((0,i+j,l+['POUR(1,2)']))
                inq.add((0,i+j))
            if b-j<=i and (i+j-b,b) not in inq:
                q.append((i+j-b,b,l+['POUR(1,2)']))
    print('impossible')
    return
bfs()




