def solve(q, z):
    if not q:
        return []
    x = q[0]
    idx = z.index(x)
    leftz, rightz = z[:idx], z[idx + 1:]
    leftq, rightq = q[1:1 + idx], q[1 + idx:]
    lefth, righth = solve(leftq, leftz), solve(rightq, rightz)
    return lefth + righth + [x]
while True:
    try :
        a=list(input())
        b=list(input())
    except EOFError:
        break
    print(''.join(solve(a,b)))


