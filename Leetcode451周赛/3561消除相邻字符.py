class Solution:
    def resultingString(self, s: str) -> str:
        stack=[]
        for i in s:
            if stack:
                t=stack[-1]
                if (i,t)==('z','a') or (i,t)==('a','z') or abs(ord(t)-ord(i))==1:
                    stack.pop()
                    continue
            stack.append(i)
        return ''.join(i for i in stack)

#之前是想要用deque来像模拟约瑟夫问题一样模拟的，但是有一个比较大的漏洞，就是一整个循环实际上只能
#消除一对，要重拍后才能消除另外的，所以下面的代码一个循环可能多个确实是有问题的
class Solution:
    def resultingString(self, s: str) -> str:
        q=deque([i for i in s])
        while True and len(q)>1:
            a=q.popleft()
            flag=False
            for _ in range(len(q)):
                b=q.popleft()
                if (a,b)==('z','a') or (a,b)==('a','z') or abs(ord(a)-ord(b))==1:
                    flag=True
                    a='A'
                elif a=='A':
                    a=b
                else:
                    q.append(a)
                    a=b
            if a!='A':
                q.append(a)
            if not flag:
                break
        return ''.join(i for i in q)