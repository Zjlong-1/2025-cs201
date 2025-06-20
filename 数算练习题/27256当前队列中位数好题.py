#通法太困难了，只能无奈暴力模拟
#同时构造一个辅助栈来记录popleft
#一个小知识：
#如果 x 是一个元组（如 [v, 0]），bisect_left 会根据 v 的值与 a 中的每个元素的第一个值进行比较。
#cnt 或者元组的第二个元素在查找插入位置时不会被考虑，只有 v 被用来进行比较。
from bisect import bisect_left
n=int(input())
l1,l2,cnt,k=[],[],0,0
for _ in range(n):
    f=input().split()
    if f[0]=='add':
        a=int(f[1])
        l1.insert(bisect_left(l1,[a,0]),[a,cnt])
        l2.append(a)
        cnt+=1
    elif f[0]=='del':
        a=l2[k]
        k+=1
        l1.pop(bisect_left(l1,[a,0]))
    elif f[0]=='query':
        t=len(l1)
        if t%2==0:
            ans=(l1[t//2][0]+l1[t//2-1][0])/2
            print(ans if int(ans)!=ans else int(ans))
        else:
            print(l1[t//2][0])

