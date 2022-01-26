from math import *

def getTime(d):
    # gets time it takes to fall distance d
    return sqrt(d * 2 / 9.8)


def timeDiff(h1, h2):
    # takes in two distances(in meters) an object has fallen and returns the time difference between the two
    #print h1,h2
    t1 = getTime(h1)
    t2 = getTime(h2)
    return abs(t2 - t1)


def nextFallPoint(dist, timeI):
    # gets the next point an object should be back based on distance fallen dist and the time interval timeI
    t = getTime(dist)
    t += timeI
    return 0.5 * 9.8 * t ** 2
