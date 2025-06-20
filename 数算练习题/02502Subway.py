#每两个点之间都连边，只是地铁和走路导致的时间区别而已，最优化肯定是走已经存在的点。
# 而且由于只考虑时间的加和，同一轨道上面的点只需要记录相邻的点连边即可
#题目没有讲清楚输入的终止条件
import heapq
import math
a,b,c,d=map(int,input().split())
s={}
way=set()
while True:
    try:
        l=list(map(int,input().split()))
        if l==[-1,-1]:
            break
        l1=[(l[2*i],l[2*i+1]) for i in range(len(l)//2-1)]
        for j,x in enumerate(l1):
            s[x]=float('inf')
            if j!=len(l1)-1:
                way.add((x,l1[j+1]))
                way.add((l1[j+1],x))
    except EOFError:
        break
def di(x1,y1,x2,y2):
    return math.sqrt(((x1-x2)**2+(y1-y2)**2))
s[(a,b)],s[(c,d)]=0,float('inf')
heap=[(0,a,b)]
while heap:
    w,x,y=heapq.heappop(heap)
    if (x,y)==(c,d):
        break
    for i in s.keys():
        if i!=(x,y):
            chu=40000 if ((x,y),i) in way else 10000
            t=di(x,y,i[0],i[1])/chu+w
            if t<s[i]:
                s[i]=t
                heapq.heappush(heap,(t,i[0],i[1]))
print(round(s[(c,d)]*60))

