#!/usr/bin/python3
import io
import ast
from random import shuffle, randint
import sys
import os

part = sys.argv[1]
final = open('vw/' + part.zfill(5) + '.mc.vw', 'w')
for i in io.open(part):
    a = ast.literal_eval(i.strip())
    final.write(str(randint(2,10) if a[1] == 0 else 1) + " '" + str(a[0]) + ' | ' + ' '.join(["f" + str(j[0]) + ':' + str(j[1]) for j in a[2][1]]) + '\n')

#shuffle(vw)
