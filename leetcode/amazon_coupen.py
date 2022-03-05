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

from copy import copy
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


codeList = [['apple', 'apple'], ['banana', 'anything', 'banana']]
shoppingCart = ['banana','banana', 'orange', 'banana','apple', 'apple']
start = 0
j = 0
patert_match = 0
import copy
for code in codeList:
    # code = codeList[1]
    print('code -------->',code)
    while j < len(shoppingCart[start:]):
        # j = 0
        if code[0] in shoppingCart[start:]:
            ind = shoppingCart.index(code[0],start)
            pair = shoppingCart[ind:ind+len(code)]
            if 'anything' in code:
                codevalue = copy.deepcopy(code)
                anyind = code.index('anything')
                codevalue[anyind] = pair[anyind]
                print()
                if codevalue == pair:
                    print(pair)
                    patert_match+=1 
                    start = ind+len(code)
                    break
                else:
                    start +=1
            elif code == pair:
                print(pair)
                patert_match+=1
                start = ind+len(code)
                break
            else:
                start = ind+1
        j +=1
if patert_match == len(codeList):
    print('1')
else:
    print('0')
    
    
queue = []
queue.insert(0,'app')
queue.pop(0)


def solution(s):
    try:
        left = s.index('a')
        s.index('b')
    except Exception:
        # One of the index operations didnt work
        return 0

    # We get one point for free :)
    result, current = 1, 1
    result_contains_b, current_contains_b = False, False

    for i in range(left+1, len(s)):
        c = s[i]

        if c == 'a':
            current += 1
            if current > result:
                result = current
                result_contains_b = current_contains_b
        elif c == 'b':
            current -= 1
            current_contains_b = True
            if current < 0:
                current = 0
                current_contains_b = False
        else:
            # These characters mean nothing to us,
            # despise them!11
            continue

    if current_contains_b == True:
        return result
    else:
        return result-1
    
solution('abdbcdacbcadbbc')
allsubstring = []
for i in range(len('abdbcdacbcadbbc')):
    subStr = "";
    # Second loop is generating sub-String
    for j in range(i,len(str)):
        subStr += str[j];
        allsubstring.append(subStr)

print('string',s)

for ind in range(2,len(s)):
    substring = s[:ind]
    wordcount = [substring.count(i) for i in substring]
    diff = max(wordcount) - min(wordcount)
    print(substring,diff)
    if diff > maxvalue:
        maxvalue = diff
print('max------------>',maxvalue)
    # return maxvalue

def findSubStrings(str):
    allsubstring = []
    # First loop for starting index
    maxvalue=0
    for i in range(len(str)):
        subStr = "";
 
        # Second loop is generating sub-String
        for j in range(i,len(str)):
            subStr += str[j];
            print(subStr)
            substring = list(subStr)
            wordcount = [substring.count(i) for i in substring]
            diff = max(wordcount) - min(wordcount)
            if diff > maxvalue:
                maxvalue = diff
    return maxvalue
    
allsubstring = findSubStrings('aabb')
wordcount = [substring.count(i) for i in substring]

maxvalue=0
for substring in allsubstring:
    substring = list(substring)
    
print(substring,diff)
if diff > maxvalue:
    maxvalue = diff

