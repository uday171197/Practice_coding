s = "(((()))))"

def isValid( s):
    stack = []
    maps = {')':'(',']':'[','}':'{'}
    for i in list(s):
        if i in ['(','[','{']:
            stack.append(i)
        else:
            if not stack or stack[-1] != maps[i]:
                return False
            else:
                stack.pop()
    if stack:
        return False
    else:
        return True

isValid(s)


