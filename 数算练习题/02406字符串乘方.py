while True:
    s=input()
    if s=='.':
        break
    n=len(s)
    ans=1
    def can(x):
        return s[0:n//x]*x==s
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            if can(i) and i>ans:
                ans=i
            if can(n//i) and n//i>ans:
                ans=n//i
    print(ans)
#法2，KMP：
def f(s):
    nxt=[0]*len(s)
    j=0
    for i in range(1,len(s)):
        while s[i]!=s[j] and j>0:
            j=nxt[j-1]
        if s[i]==s[j]:
            j+=1
        nxt[i]=j
    return nxt[-1]
while True:
    s=input()
    if s=='.':
        break
    n=len(s)
    k=n-f(s)
    if n%k==0:
        print(n//k)
    else:
        print(1)