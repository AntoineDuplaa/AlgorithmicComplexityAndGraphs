import numpy as np


def parcours(list): 

    #Initialisation
    snowplowIndex = 0
    #middleIndex = 0
    RelevantList = []
    list = sorted(list)

    # Separate Aray In 2 Arays
    i = 0
    while  (i < len(list) and (list [i] < snowplowIndex)):
        i += 1
    listLeft = list [:i]
    listRight = list [i:]


    while (len(listLeft) + len(listRight) > 0):
        totalRight = 0
        totalLeft = 0

        for index in listLeft:
            travelTime = abs(float(index - snowplowIndex))
            if (travelTime == 0):
                totalLeft += 99999999
            else:
                totalLeft += float(1/travelTime)

        for index in listRight:
            travelTime = abs(float(index - snowplowIndex))
            if (travelTime == 0):
                totalRight += 99999999
            else :
                totalRight += float(1/travelTime)

        if (totalLeft > totalRight):
            RelevantList.append(listLeft[-1])
            snowplowIndex = listLeft[-1]
            listLeft.pop(-1)
        else :
            RelevantList.append(listRight[0])
            snowplowIndex = listRight[0]
            listRight.pop(0)
    return (RelevantList)