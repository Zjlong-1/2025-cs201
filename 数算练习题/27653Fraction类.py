from math import gcd
a,b,c,d=map(int,input().split())
x=a*d+b*c
y=b*d
t=gcd(x,y)
print(f'{x//t}/{y//t}')