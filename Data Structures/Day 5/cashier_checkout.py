from cashierQueue import *


cashierQList = []

for i in range(6):
    cashierQList.append(CashierQueue())

with open("customerList.txt", encoding='utf8', errors='') as fileIn:

    for line in fileIn:
        customer = line.split()
        ID = customer[0]
        items = int(customer[1])
                
        times = []
        for cashier in cashierQList:
            times.append(cashier.totaltime())
            
        minTime = min(times)
        minTimeIndex = times.index(minTime)
        
        cashierQList[minTimeIndex].insert(ID, items)
        
for cashier in cashierQList:
    print(cashier, cashier.totaltime())      
        
        
        
    


