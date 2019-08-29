#!/bin/python3

import math
import os
import random
import re
import sys
import datetime

# Complete the time_delta function below.

for t in range(int(input())):
    timestamp1 = input().strip()
    timestamp2 = input().strip()
    time_format = '%a %d %b %Y %H:%M:%S %z'
    time_second1 = datetime.datetime.strptime(timestamp1, time_format)
    time_second2 = datetime.datetime.strptime(timestamp2, time_format)
    print(int(abs((time_second1 - time_second2).total_seconds())))
#源代码直接跑不出来，重写了一遍
