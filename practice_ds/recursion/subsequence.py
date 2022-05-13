
def subsequence(arr,i,res):
    if i >= len(arr):
        print(res)
        return
    res.append(arr[i])
    subsequence(arr,i+1,res) # take or picking the char
    res.pop()
    subsequence(arr,i+1,res) # note take or not picking element , we have removed the last element
    
arr = [3,1,2]
subsequence(arr,0,[])

def subsequence(string,i,res):
    if i >= len(string):
        print(res)
        return
    res+=string[i]
    subsequence(string,i+1,res) # take or picking the char
    res = res[:len(res)]
    subsequence(string,i+1,res) # note take or not picking element , we have removed the last element
    
string = 'abcs'
subsequence(string,0,"")




