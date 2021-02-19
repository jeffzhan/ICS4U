from stack_class import *
import math

rpnStack = Stack()
operators = ['+', '-', '*', '/', '√', '^']

def calc(operand):
    
    if (operand == '+') or (operand == '-') or (operand == '*') or (operand == '/') or (operand == '^'):
        val1 = rpnStack.pop()
        val2 = rpnStack.pop()

        if operand == '^':
            return val2 ** val1
        else:
            return eval(f'{val2} {operand} {val1}')

    elif (operand == '√'):
        val2 = int(rpnStack.pop())
        return math.sqrt(val2)

equation = "4 18 3 / 2 ^ +"
equation = equation.split()

for item in equation:
    if item.isdigit():
        rpnStack.push(int(item))
    elif item in operators:
        rpnStack.push(int(calc(item)))
    else:
        print(f'{item} is not a valid number or operand')

if rpnStack.length() == 1:
    print(rpnStack.peek())
else:
    print('Error.')

    

    