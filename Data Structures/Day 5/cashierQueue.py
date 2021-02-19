'''
@author: aaronQuesnelle
2018 for ICS4U
'''


class CustomerListNode:
    
    def __init__(self, ID, items):
        self._id = ID
        self._items = items
        self._link = None

    def id(self):
        return self._id
    
    def items(self):
        return self._items

    def link(self):
        return self._link

    def newlink(self, node):
        self._link = node

    def __str__(self):
        return f'({self._id}, {self._items})'
    
    def __repr__(self):
        return f'CustomerListNode(id={self._id}, items={self._items})'



class CashierQueue:
    
    def __init__(self):
        self._length = 0
        self._totaltime = 0
        self._head = None
        self._tail = None

    def length(self):
        return self._length
    
    def totaltime(self):
        return self._totaltime
    
    def empty(self):
        return self._length == 0

    def insert(self, ID, items):
        newNode = CustomerListNode(ID, items)
        if (self._head == None):
            self._head = newNode
            self._tail = newNode
        else:
            self._tail.newlink(newNode)
            self._tail = newNode

        self._length += 1
        self._totaltime += items
    

    def remove(self):
        #checking if list is empty or not
        if self._length == 0:
            return None
        else:
            idVal = self._head.id()
            timeVal = self._head.time()
            #checking if list only has one item
            if self._length == 1:
                self._head = None
                self._tail = None

            #if list has more than one item
            else:
                p = self._head.link()
                self._head = p
    
            self._length -= 1
            self._totaltime -= timeVal
            
            return idVal


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
                if type(n.id()) == str:
                    s += "'" + str(n.id()) + "', "
                else:
                    s += str(n.id()) + ", "
            else:
                s += str(n.id())

            # advance to next item in list
            n = n.link()

        return ("[" + s + "]")
    
    
  
