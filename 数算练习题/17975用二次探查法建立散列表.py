#这个题目有一个很难想到的坑点，同一个数据可以多次询问插入
import sys
input = sys.stdin.read
data = input().split()
index = 0
n = int(data[index])
index += 1
m = int(data[index])
index += 1
num_list = [int(i) for i in data[index:index+n]]
s={}
ans=[]
for i in num_list:
    t=i%m
    cnt=1
    if t not in s or s[t]==i:
        s[t]=i
        ans.append(t)
        continue
    while True:
        if (t+cnt**2)%m not in s:
            s[(t+cnt**2)%m]=i
            ans.append((t+cnt**2)%m)
            break
        elif (t-cnt**2)%m not in s:
            s[(t-cnt**2)%m]=i
            ans.append((t-cnt**2)%m)
            break
        cnt+=1
print(*ans)