for i in s:
        if i.isdigit() or i=='.':
            num+=i
        else:
            if num:
                ans.append(num)
                num=''
#之后再依据要求看是否转浮点数
