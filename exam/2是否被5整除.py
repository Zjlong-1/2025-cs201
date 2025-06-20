s=input()
ans=''
cur=0
for i in s:
    cur=cur*2+int(i)
    cur%=5
    if cur==0:
        ans+='1'
    else:
        ans+='0'
print(ans)