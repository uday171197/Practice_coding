def longetCommonPrifix(strs):
    ismatched = True
    prefix = ""
    smallword = strs[0]
    for str in strs:
        if len(str) < len(smallword):
            smallword = str
    ch = 0
    while smallword and ch < len(smallword):
        for word in strs:
            if word[ch] != smallword[ch]:
                ismatched = False
        if ismatched:
            prefix += smallword[ch]
        else:
            break
        ch+=1
    return prefix
    # if len(strs) == 1:
    #     return strs[0]
    # for i in range(len(strs[0])):
    #     c = strs[0][i]
    #     for x in strs[1:]:
    #         if i == len(x) or c != x[i]:
    #             return x[:i]
    # return strs[0]
        
            




strs = ["flower","flow","flight"]
strs = ["b",""]
longetCommonPrifix(strs)




[1,1,1,1,3,3,4,5,6]

nim = 3
