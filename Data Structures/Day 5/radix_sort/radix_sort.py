import queueClass as q
import math

aList = [802, 150, 42, 370, 143, 98, 7, 1420, 3]

queueList = []

for i in range(11):
    queueList.append(q.Queue())
    
numberDigits = int(math.log(abs(max(aList)), 10) + 1)
#3

secondaryList = []

for i in range(numberDigits): #3
    
    for num in aList:
        index = (num // 10 ** i) % 10

        if int(math.log(abs(num), 10) + 1) >= i: # if length of num is larger/equal to the current numDigits
            queueList[index+1].insert(num)
        else:
            queueList[0].insert(num)
        
    for queue in queueList:
        for i in range(queue.length()):
            secondaryList.append(queue.remove())
    
    aList = secondaryList
    secondaryList = []
    
print(aList)