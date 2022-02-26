# codeList = [['apple', 'apple'], ['banana', 'anything', 'banana']] 
# shoppingCart = ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']

codeList = [['apple', 'apple'], ['banana', 'anything', 'banana']]
shoppingCart = ['banana', 'orange', 'banana', 'apple', 'apple']
def promotion():
    if not len(codeList):
        return 1
    p = 0 # code no
    i = 0 # shoppingCart
    while i < len(shoppingCart):
        j =0 # pattern index
        while j < len(codeList[p]):
            # print(p,j,i)
            # print(codeList[p][j],shoppingCart[i])
            if i < len(shoppingCart) and codeList[p][j] == 'anything'  or codeList[p][j] == shoppingCart[i]:
                i +=1
                j +=1
            elif i > len(shoppingCart):
                break
            else:
                i+=1
        p +=1
        # print('p------------->',p)
        if p == len(codeList):
            return 1
        else:
            return 0
        
promotion()   

import re
def freshPromotion(shoppingCart, codeList) -> int:
    s = ' '.join(shoppingCart)
    print(s)
    reg = ''
    for code in codeList:
        c = ' '.join(code)
        c = ' ' + c
        c = c.replace('anything', '\w+')
        reg += c + '[\w\s]*'
    r = re.compile(reg)
    res = r.findall(s)
    return min(1, len(res))

freshPromotion(shoppingCart, codeList)

