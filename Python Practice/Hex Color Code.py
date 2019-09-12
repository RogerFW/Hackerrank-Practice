# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    s = input()
    if re.match(r'^(.*\:|\s)', s, re.I):
        for m in re.finditer(r'(\#(?:[0-9a-f]{3}){1,2})', s, re.I):
            print(m.group(1))
