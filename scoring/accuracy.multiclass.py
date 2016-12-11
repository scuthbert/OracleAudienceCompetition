#!/usr/bin/python3
import os
import sys
from math import copysign

predictions = os.popen('cut predictions.txt -d \' \' -f1', 'r').readlines()
correct = os.popen('cut %s -d\' \' -f1' % (sys.argv[1].zfill(5))).readlines()

accurate = 0.0
spendcorrect = 0.0
total = 0.0
spendtotal = 0.0
count = 0.0
falses = 0.0

for i in range(0, len(predictions)):
    count += 1
    if float(correct[i].strip()) == 1:
        spendtotal += 1
	if float(predictions[i].strip()) == 1:
		spendcorrect += 1
    else:
	if float(predictions[i].strip()) == 1:
            falses += 1
	total += 1
	if int(correct[i].strip()) == float(predictions[i].strip()):
	    accurate += 1

print("Not ones: " + str(accurate / total))
print("Ones: " + str(spendcorrect / spendtotal))
print("False Positive: " + str(falses / count))
