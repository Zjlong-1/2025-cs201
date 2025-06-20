while True:
    try:
        s=input()
    except EOFError:
        break
    def pan(s):
        if s[0]=='.' or s[0]=='@' or s[-1]=='.' or s[-1]=='@':
            return False
        flag=0
        c=-1
        t=-1
        for i in range(1,len(s)-1):
            if s[i]=='@' and s[i+1]=='.':
                return False
            if s[i]=='@' and s[i-1]=='.':
                return False
            if s[i]=='@' and flag==1:
                return False
            if s[i]=='@':
                flag+=1
                c=i
            if s[i]=='.':
                t=i
        return t>c and flag==1
    if pan(s):
        print('YES')
    else:
        print('NO')




