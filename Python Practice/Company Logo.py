#!/bin/python3
#import math
#import os
#import random
#import re
#import sys
#给了一堆废物包，不知道它怎么想的
import collections

if __name__ == '__main__':
    s = sorted(input().strip())
s_counter = collections.Counter(s).most_common()

s_counter = sorted(s_counter, key=lambda x: (x[1] * -1, x[0]))
for i in range(0, 3):
    print(s_counter[i][0], s_counter[i][1])
