def f(x):
    return x**3-5*x**2+10*x-80
left,right=2,10
while right-left>10**-10:
    mid=(left+right)/2
    if f(mid)>0:
        right=mid
    else:
        left=mid
print(f'{left:.9f}')
#要精确到9位则必须算到10位（防止差距小但是第9位不同）