#!/usr/bin/env python

import sys
# $:-D <- elvis
sum = 0
n = 0

# Sum the input.
for num in open('data_2.txt'):
    sum += float(num)
    n += 1
    
print sum / n
       
