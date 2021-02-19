'''
@author: aaronQuesnelle
2018 for ICS4U

'''


class ListNode:
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


    

class Queue:
    
    def __init__(self):
        self._length = 0
        self._head = None
        self._tail = None

    
    def empty(self):
        return self._length == 0


    def insert(self, value):
        newNode = ListNode(value)
        if (self._head == None):
            self._head = newNode
            self._tail = newNode
        else:
            self._tail.newlink(newNode)
            self._tail = newNode

        self._length += 1
    

    def remove(self):
        #checking if list is empty or not
        if self._length == 0:
            return None
        else:
            removeVal = self._head
            #checking if list only has one item
            if self._length == 1:
                self._head = None
                self._tail = None

            #if list has more than one item
            else:
                p = self._head.link()
                self._head = p
    
            self._length -= 1
            
            return removeVal


    def peek(self):
        if self._head == None:
            return None
        else:
            return self._head


    def __str__(self):
        s = ""
        n = self._head

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
    
q = Queue()
q.insert('x')
q.insert('y')
q.insert('z')
q.insert('p')

q.remove()
q.remove()

q.insert('a')

print(q)

    
    
  
