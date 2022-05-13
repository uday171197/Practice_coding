
def is_ngram(a,b):
    if len(a)!= len(b):
        return 
    ad,bd = {},{}
    for i in range(len(a)):
        ad[a[i]] = 1 + ad.get(a[i],0)
        bd[b[i]] = 1 + bd.get(b[i],0)
    for j in ad:
        if j not in bd or bd.get(j) !=  ad[j]:
            return 
    return b
is_ngram('','')

    
def group_ngram(strs):
    res = []
    used= []
    for i in range(len(strs)):
        ans = []
        if strs[i] not in used:
            ans.append(strs[i])
            for j in range(i+1,len(strs)):
                rest = is_ngram(strs[i],strs[j])
                if rest != None and rest not in used:
                    ans.append(rest)
                    used.append(rest)
                    # strs.remove(rest)
            if ans: 
                res.append(ans)
    return res
                
            
            
    





strs = ["",""]
group_ngram(strs)
