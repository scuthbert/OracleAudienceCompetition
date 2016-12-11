#!/usr/bin/python3
import os
import sys
from math import copysign

predictions = os.popen('cut predictions-regr.txt -d\' \' -f1').readlines()
correct = os.popen('cut %s -d\' \' -f1' % (sys.argv[1])).readlines()

distance = 0.0
total = 0.0
threshold = 6.968
#99% threshold is 6.968

for i in range(0, len(predictions)):
    if float(predictions[i].strip()) > threshold:
        total += 1
        distance += abs(float(correct[i].strip()) - float(predictions[i].strip()))

print("Avg distance: " + str(distance / total))
