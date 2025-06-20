#有一点吃惊，交换的次数竟然是逆序对的个数，但是细想也是，每次交换都可以使得逆序数减一，而且排序好了等价于逆序数为0
#所以只要算逆序数即可，用merge sort
while True:
    n=int(input())
    if n==0:
        break
    l=[int(input()) for _ in range(n)]
    ans=0
    def merge(l):
        global ans
        if len(l)<=1:
            return
        mid=len(l)//2
        l1,l2=l[:mid],l[mid:]
        merge(l1)
        merge(l2)
        left=right=0
        while len(l1)>left and len(l2)>right:
            if l1[left]>l2[right]:
                l[left+right]=l2[right]
                ans+=len(l1)-left
                right+=1
            else:
                l[left+right]=l1[left]
                left+=1
        cnt=left+right
        while len(l1)>left :
            l[cnt]=l1[left]
            left+=1
            cnt+=1
        while len(l2)>right:
            l[cnt]=l2[right]
            right+=1
            cnt+=1
    merge(l)
    print(ans)


