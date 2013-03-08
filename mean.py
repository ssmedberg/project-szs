#!/usr/bin/env python

import sys

sum = 0
n = 0

#comment
for num in sys.stdin:
    sum += float(num)
    n += 1
    
print sum / n
       
