import csv
from GravityPhysics import *

path1 = r'C:\Users\ColtM\Desktop\Coding Projects\TAMU\Validation\camera_pos.csv'
path2 = r'C:\Users\ColtM\Desktop\Coding Projects\TAMU\Validation\lidarTest.csv'

camera = open(path1, "r")
lidar = open(path2, "r")
lines1 = camera.readlines()
lines2 = lidar.readlines()

for l1, l2 in zip(lines1, lines2):
    cy = l1.split(",")
    ly = l2.split(",")
    avg = 0
    count = 0
    for i, j in zip(cy, ly):
        print(i, j)
        diff = timeDiff(float(i), float(j))
        print(diff)
        avg += diff
        count += 1
    avg /= count
    print("Average:", avg) #todo add standard deviation
