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

    
    def insertNewLastNode(self, value):
        '''
        Function creates and inserts an item into the last position of the list.
    
        Params
        value is any value/object being stored in the list
        '''
        #create the new node to insert
        newNode = ListNode(value)
        
        #if list empty new node is first node
        if (self._firstNode == None):
            self._firstNode = newNode
        else:
            #locate last node in list
            p = self._firstNode
            while (p.link() != None):
                p = p.link()
            p.newlink(newNode)
        
        #increase length by 1
        self._length += 1


    def insertNewFirstNode(self, value):
        newNode = ListNode(value)
        
        #link firstnode to the rest of the list
        newNode.newlink(self._firstNode)
    
        #new node is first node
        self._firstNode = newNode
        
        self._length += 1
   

    def deleteFirst(self):
    
        if self._firstNode != None:
            self._firstNode = self._firstNode.link()

        self._length -= 1

        
    def deleteLastNode(self):
        '''
        Function deletes the last item in the list.
        '''
        #do nothing if list is empty
        if (self._firstNode != None):
            
            #if the list has one node, empty list and decrease length
            if (self._firstNode.link() == None):
                self._firstNode = None
                self._length -= 1
                
            #otherwise the list has two or more nodes
            else:
                #initialize pointers to previous and current node
                previousNode = self._firstNode
                currentNode = self._firstNode.link()
                
                #advance pointers along the list until current points
                #to last item in list
                while(currentNode.link() != None):
                    previousNode = currentNode
                    currentNode = currentNode.link()
                
                #now previous node points to new last node in list
                #length is decreased
                previousNode.newlink(None)
                self._length -=1
        

    def __str__(self):
        '''
        Function returns the list contents as one line formatted [item, "string", etc]

        Returns
        A string in the format [item, item, item]
        '''
        s = ""
        n = self._firstNode
        
        #iterate through list one item at a time until last item reached
        while (n != None):
            #check if last item in list has been reached
            #if so, do not place a comma after the item
            if n.link() != None:
                
                #check if item is type string. If so, place it in quotations
                if type(n.value()) == str:
                    s += "'" + str(n.value()) + "', "
                else:
                    s+= str(n.value()) + ", "
            else:
                #check if item is type string. If so, place it in quotations
                if type(n.value()) == str:
                    s += "'" + str(n.value()) + "'"
                else:
                    s+= str(n.value())
                
            #advance to next item in list
            n = n.link()
        
        return("[" + s + "]")


    def count(self, item):
        '''
        Counts the number of time an item appears in the list.
        '''
        count = 0
        currentNode = self._firstNode

        while currentNode != None:        
            if currentNode.value() == item:
                count += 1
            
            currentNode = currentNode.link()

        return count


    def index(self, item):
        '''
        Returns the index of the item's first occurence in the list. If it is not found, returns -1
        '''
        currentIndex = 0
        currentNode = self._firstNode

        while currentNode != None:
            if currentNode.value() == item:
                return currentIndex
           
            currentNode = currentNode.link()
            currentIndex += 1
            
        return -1


    def extend(self, other):
        if type(other) == str or type(other) == list:
            for item in other:
                self.insertNewLastNode(item)
            
        elif type(other) == LinkedList:
            currentNode = other.firstNode()
            while currentNode != None:
                self.insertNewLastNode(currentNode.value())
                currentNode = currentNode.link()
        else:
            print('Invalid data type')


    def copy(self):
        liCopy = LinkedList()
        
        currentNode = self._firstNode
        while currentNode != None:
            liCopy.insertNewLastNode(currentNode.value())
            currentNode = currentNode.link()
        
        return liCopy   