n=int(input())
cnt=0
def solve(t,stack):
    global cnt
    if t==n+1:
        cnt+=1
        return
    solve(t+1,stack+[t])
    while stack:
        stack.pop()
        solve(t+1,stack+[t])
solve(1,[])
print(cnt)


