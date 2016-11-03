#!/usr/bin/python3
import os
import sys
from math import copysign

predictions = open('predictions.txt','r').readlines()
correct = os.popen('cut train/vw/%s.vw -d\' \' -f1'%(sys.argv[1].zfill(5))).readlines()

accurate = 0.0
total = 0.0

"""def specround(num):
    if abs(-1 - num) < abs(1 - num):
	return -10
    else:
	return 1
"""

for i in range(0,len(predictions)):
    if int(correct[i].strip()) == 1:
        total += 1
        if int(correct[i].strip()) == copysign(1, float(predictions[i].strip())):
            accurate += 1

print(accurate/total)
