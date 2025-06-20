import sys
sys.setrecursionlimit(100000)
while True:
    n=int(input())
    if n==0:
        break
    l3=list(map(int,input().split()))
    l4=list(map(int,input().split()))
    l3.sort()
    l4.sort()
    def solve(l1,l2):
        if not l1:
            return 0
        if len(l1)==1:
            if l1[0]>l2[0]:
                return 3
            elif l1[0]==l2[0]:
                return 2
            else:
                return 1

        if l1[0]>l2[0]:
            return 3+solve(l1[1:],l2[1:])
        if l1[0]<l2[0]:
            l2.pop()
            return 1+solve(l1[1:],l2)
        if l1[-1]>l2[-1]:
            l1.pop()
            l2.pop()
            return 3+solve(l1,l2)
        if l1[0]<l2[-1]:
            l2.pop()
            return 1+solve(l1[1:],l2)
        else:
            l2.pop()
            return 2 + solve(l1[1:], l2)
    ans1=solve(l4[:],l3[:])
    ans2=4*len(l3)-solve(l3[:],l4[:])
    print(ans1,ans2)
