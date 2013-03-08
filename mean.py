#!/usr/bin/env python

import sys
# $:-D <- elvis
sum = 0
n = 0

# Sum the input.

file_name = "data_2.txt"
for num in open(file_name):
    sum += float(num)
    n += 1
    
print sum / n
       
