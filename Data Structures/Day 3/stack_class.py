class StackNode:
    '''
    Class of listNode is a data type which holds a value and a link to the next
    node in a list. This object is used in conjunction with linked list
    '''

    def __init__(self, value):
        self._value = value
        self._link = None

    def value(self):
        return self._value

    def link(self):
        return self._link

    def newlink(self, node):
        self._link = node

    def __str__(self):
        return self._value


class Stack:

    def __init__(self):
        self._length = 0
        self._top = None
        
    def top(self):
        return self._top

    def length(self):
        return self._length
    
    def empty(self):
        return self._top == None
   
    def push(self, value):
        newNode = StackNode(value)

        p = self._top
        newNode.newlink(p)

        self._top = newNode
        self._length += 1

    def pop(self):
        returnVal = self.peek()
        
        if self._top != None:

            if self._top.link() == None:
                self._top = None
            else:
                p = self._top.link()
                self._top = p

            self._length -= 1
        
        return returnVal

    def peek(self):
        if self._top == None:
            return None
        else:
            return self._top

    def __str__(self):
        s = ""
        n = self._top

        # iterate through list one item at a time until last item reached
        while (n != None):
            # check if last item in list has been reached
            # if so, do not place a comma after the item
            if n.link() != None:

                # check if item is type string. If so, place it in quotations
                if type(n.value()) == str:
                    s += "'" + str(n.value()) + "', "
                else:
                    s += str(n.value()) + ", "
            else:
                s += str(n.value())

            # advance to next item in list
            n = n.link()

        return ("[" + s + "]")


        
someStack = Stack()   
someStack.push('a')
someStack.pop( )
someStack.push('b')
someStack.push('c')
someStack.push('d')
someStack.push('e')
someStack.pop( )
d = someStack.pop( )

print(d)
print(someStack)

# b, d, c, a, e