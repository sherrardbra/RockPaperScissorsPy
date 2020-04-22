from random import random
from time import time

def meanMedianMode(sensorList):
    """
    Takes a list of numbers, returns tuple of statistics
    """
    mean = 0
    median = 0
    mode = 0

    # find mean, median and mode
    runningTotal = 0
    for elem in sensorList:
        runningTotal += elem
    mean = runningTotal / len(sensorList)
    
    return mean, median, mode

testList = []

for i in range(0, 10000):
    num = int(random()*100)
    testList.append(num)

#for elem in testList:
#    print(elem)

#for j in range(0, len(testList)):
#    print(testList[j])

compMean, compMedian, compMode = meanMedianMode(testList)
print(compMean)

