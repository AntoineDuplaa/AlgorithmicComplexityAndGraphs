import numpy as np
import random
from math import *
import sys

def greedy (houses : list):
    snowplowIndex = 0;
    dist = -1
    closest = 0
    RelevantList = []

    while houses:
        for i in range (0, len(houses)):
            distTMP = abs(houses[i] - snowplowIndex)
            if (dist == -1 or dist > distTMP):
                dist = distTMP
            closest = i

        RelevantList.append(houses[i])
        houses.pop(i)
    return RelevantList