
def push(stack,val):
    stack.append(val)

def pop(stack):
    stack.pop()

def peek(stack):
    if len(stack):
        return stack[len(stack)-1]
    else:
        return None

def main():
    inputs = input('Enter the patter')
    stack = []
    paran_dict = {'{':'}','(':')','[':']'}
    if inputs:
        for par in inputs:
            print(len(stack))
            if peek(stack):
                last_value= peek(stack)
                matching_val = paran_dict.get(last_value,'')
                if par == matching_val:
                    pop(stack)
                else:
                    push(stack,par)
            else:
                push(stack,par)
        if len(stack):
            print(False)
        else:
            print(True)
    else:
        print('please enter the value')
        
main()