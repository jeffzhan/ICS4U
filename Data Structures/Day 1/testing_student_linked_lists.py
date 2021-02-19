from LinkedList import *

##or
##import LinkedList_Student_version as linked

alist = LinkedList()
alist.insertNewLastNode(6)
alist.insertNewLastNode(3)
alist.insertNewLastNode(0)

print(alist)


###TESTING insert new first node function
print("\nTESTING INSERT NEW FIRST NODE FUNCTION")
wordList = LinkedList()
wordList.insertNewFirstNode('hello')
print("\n\n")
print(wordList)
print("You should see this on the console: ['hello'] ")

wordList.insertNewFirstNode('world')
wordList.insertNewFirstNode('!!!')
print("\n\n")
print(wordList)
print("You should see this on the console:  ['!!!', 'world', 'hello']")

wordList.insertNewLastNode('The')
wordList.insertNewLastNode('quick')
wordList.insertNewLastNode('brown fox')
print("\n\n")
print(wordList)
print("You should see this on the console:  ['!!!', 'world', 'hello', 'The', 'quick', 'brown fox']")


###TESTING delete first node function
print("\nTESTING DELETE FIRST NODE FUNCTION")
wordList.deleteFirst()
print("\n\n")
print(wordList)
for i in range(3):
    wordList.deleteFirst()

print("\n\n")
print(wordList)
print("You should see this on the console:  ['quick', 'brown fox']")



###TESTING insert after function
print("\nTESTING INSERT AFTER FUNCTION")
alist = LinkedList()
alist.insertNewLastNode(0)
alist.insertNewLastNode(4)
alist.insertNewLastNode(7)
alist.insertNewLastNode(8)
alist.insertNewLastNode(12)
print(alist)

alist.insertAfter(4, 6)
alist.insertAfter(0, 1)
alist.insertAfter(12, 15)
alist.insertAfter(5, 'nope')
print("\n\n")
print(alist)
print("You should see this on the console:  [0, 1, 4, 6, 7, 8, 12, 15]")



# ###TESTING remove function
# print("\nTESTING REMOVE FUNCTION")
# alist.remove(6)
# alist.remove(0)
# alist.remove(15)
# alist.remove(5)
# print("\n\n")
# print(alist)
# print("You should see this on the console:  [1, 4, 7, 8, 12]")



# ###TESTING reverse function
# print("\nTESTING REVERSE")
# alist.reverse()
# print(alist)
# print("You should see this on the console: [12, 8, 7, 4, 1]")
