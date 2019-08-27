#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    result = list(s.title())
    for index in range (len(s)-1):
      if s[index].isdigit () and s[index+1].islower ():
        result[index+1] = result[index+1].lower()
    result = ''.join([char for char in result])
    return (result)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
