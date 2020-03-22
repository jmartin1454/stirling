#!/usr/bin/python

# Calculates the error in Stirling's approximation
# incrementally until it is less than 1%

from math import *

delta=1.

z=10

while (delta>0.01):
    f_true=log(factorial(z))
    f_approx=z*log(z)-z
    delta=(f_true-f_approx)/f_true
    print("%2d %3.5f"%(z,delta))
    z=z+1
