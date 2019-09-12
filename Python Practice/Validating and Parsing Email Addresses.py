# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    s = input().strip()

    if re.match(r'^.*<[a-z][\w\.\-]*@[a-z]+\.[a-z]{1,3}>$', s, re.I):
        print(s)
