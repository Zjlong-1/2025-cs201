def f(s):
    nxt=[0]*len(s)
    j=0
    for i in range(1,len(s)):
        while s[i]!=s[j] and j>0:
            j=nxt[j-1]
        if s[i]==s[j]:
            j+=1
        nxt[i]=j
    return nxt
cnt=1
while True:
    n=int(input())
    if n==0:
        break
    s=input()
    print(f'Test case #{cnt}')
    cnt+=1
    nxt=f(s)
    for i in range(2,len(s)+1):
        k=i-nxt[i-1]
        if i%k==0 and i//k>1:
            print(i,i//k)
    print()
