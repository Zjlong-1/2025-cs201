#就是求逆序数
n=int(input())
l=[0]*n
for i in range(n-1,-1,-1):
    l[i]=int(input())
ans=0
def merge(l):
    global ans
    if len(l)<=1:
        return l
    mid=len(l)//2
    leftl,rightl=merge(l[:mid]),merge(l[mid:])
    left,right=0,0
    cnt=0
    while len(leftl)>left and len(rightl)>right:
        if leftl[left]<=rightl[right]:
            l[cnt]=leftl[left]
            left+=1
        else:
            l[cnt]=rightl[right]
            right+=1
            ans+=len(leftl)-left
        cnt+=1
    while len(leftl)>left:
        l[cnt] = leftl[left]
        left += 1
        cnt+=1
    while len(rightl)>right:
        l[cnt]=rightl[right]
        right+=1
        cnt+=1
    return l