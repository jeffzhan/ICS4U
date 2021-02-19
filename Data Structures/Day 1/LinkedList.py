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


class LinkedList:
    '''
    Class linkedList is a data type which holds references to nodes in a list.
    Nodes are linked to each other through a pointer to the next node in the list.
    The list itself holds reference to the first node in the list and the list length.
    '''

    def __init__(self):
        '''
        Initialize a new list as empty.
        '''

        self._length = 0
        self._firstNode = None

    def firstNode(self):
        return self._firstNode

    def __len__(self):
        return self._length

    def insertNewFirstNode(self, value):
        newNode = ListNode(value)

        p = self._firstNode
        newNode.newlink(p)

        self._firstNode = newNode

    def deleteFirst(self):
        
        #checking if list is empty or not
        if self._firstNode != None:
            
            #checking if list only has one item
            if self._firstNode.link() == None:
                self._firstNode = None
   
            #if list has more than one item
            else:
                p = self._firstNode.link()
                self._firstNode = p
    
            self._length -= 1
            
    def insertNewLastNode(self, value):
        '''
        Function creates and inserts an item into the last position of the list.

        Params
        value is any value/object being stored in the list
        '''

        # create the new node to insert
        newNode = ListNode(value)

        # if list empty new node is first node
        if (self._firstNode == None):
            self._firstNode = newNode
        else:
            # locate last node in list
            p = self._firstNode
            while (p.link() != None):
                p = p.link()
            p.newlink(newNode)

        # increase length by 1
        self._length += 1
        
    def insertAfter(self, afterValue, newValue):
        newNode = ListNode(newValue)

        previousNode = self._firstNode
        currentNode = self._firstNode.link()

        while (currentNode.link() != None) and previousNode.value() != afterValue:
            previousNode = currentNode
            currentNode = currentNode.link()

        if previousNode.value() == afterValue:
            newNode.newlink(currentNode)
            previousNode.newlink(newNode)
            self._length += 1
        elif currentNode.value() == afterValue:
            currentNode.newlink(newNode)
            self._length += 1

    def deleteLastNode(self):
        '''
        Function deletes the last item in the list.
        '''

        # do nothing if list is empty
        if (self._firstNode != None):

            # if the list has one node, empty list and decrease length
            if (self._firstNode.link() == None):
                self._firstNode = None
                self._length -= 1

            # otherwise the list has two or more nodes
            else:
                # initialize pointers to previous and current node
                previousNode = self._firstNode
                currentNode = self._firstNode.link()

                # advance pointers along the list until current points
                # to last item in list
                while (currentNode.link() != None):
                    previousNode = currentNode
                    currentNode = currentNode.link()

                # now previous node points to new last node in list
                # length is decreased
                previousNode.newlink(None)
                self._length -= 1

    def __str__(self):
        '''
        Function returns the list contents as one line formatted [item, "string", etc]

        Returns
        A string in the format [item, item, item]
        '''

        s = ""
        n = self._firstNode

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

    def listSearch(self, value):
        '''
        Search the list for a given value.

        Returns
        A reference to the list node with the stored value.
        Return None if value not found.
        '''

        n = self._firstNode
        # iterate through list until end of list is reached
        while (n != None):
            # if value is found return it
            if (n.value() == value):
                return n
            else:
                n = n.link()
        # return None if end of list is reached
        return n

    def concat(self, otherList):
        '''
        Functions appends otherList to the end of self.

        Params
        otherList is a linkedList data type
        '''

        n = self._firstNode
        # self list has no items
        if self._firstNode == None:
            self._firstNode = otherList.firstNode()

        # self list has 1+ items
        else:

            # point to last item in list
            while (n.link() != None):
                n = n.link()

            m = otherList.firstNode()
            # if m is not an empty list
            if (m != None):
                # if m has one or more items in list
                n.newlink(m)
            else:
                n.newlink(None)

        # increase list lengths
        self._length += len(otherList)

