#!/usr/bin/python3
import sys

zero_file = open('zeroes.txt', 'a')
with open('predictions.txt', 'r') as predictions:
    with open(sys.argv[1], 'r') as regrfull:
        for line in predictions:
            predline = line.split()
            if int(predline[0]) == 1:
                print(regrfull.readline(), end="")
            #if int(predline[0] in range(2, 11)):
            else:
                regrfull.readline()
                zero_file.write(predline[1] + ',0\n')

zero_file.close()
