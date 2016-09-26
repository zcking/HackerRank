#!/bin/python3

import sys


n = int(input().strip())
B = input().strip()

total = 0
while '010' in B:
    total += 1
    i = B.index('010')
    B = B[:i] + '111' + B[i+3:]
    
print(total )