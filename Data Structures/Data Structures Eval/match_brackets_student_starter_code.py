
import my_stack as mS

def is_parentheses_matched(expression):
    #( a + b ) / (a - b)
    parenthesesList = ['(', ')', '{', '}', '[', ']']
    
    s = mS.Stack()
    
    for char in expression:        
        if (char in parenthesesList):
                if char == '(' or char == '{' or char == '[':
                    s.push(char)
                else:
                    if s.empty():
                        return False

                    top = s.peek()
                    if parenthesesList.index(top) + 1 == parenthesesList.index(char):
                        s.pop()

    return s.empty()

print(is_parentheses_matched('((()]))'))