#!/usr/bin/python3
import io
import ast
from random import shuffle
import sys
import os
from math import log

part = sys.argv[1]
vw = []
for i in io.open(part):
    a = ast.literal_eval(i.strip())
    if (a[1] != 0):
        vw.append(str(log(a[1])) + " '" + str(a[0]) + ' | ' + ' '.join(["f" +
                                                    str(j[0]) + ':' + str(j[1]) for j in a[2][1]]) + '\n')

#shuffle(vw)
open('regr/' + part.zfill(5) + '.vw', 'w').write(''.join(vw))
