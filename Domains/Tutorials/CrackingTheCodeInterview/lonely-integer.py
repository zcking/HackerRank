#!/bin/python3

import sys

def lonely_integer(a):
    
    num = 0
    for i in a:
        num = num ^ i
        
    return num
    

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))
