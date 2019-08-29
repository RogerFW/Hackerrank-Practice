#!/bin/python3
n, m = map(int, input().split())
arr = [input() for _ in range(n)]
k = int(input())

for row in sorted(arr, key=lambda row: int(row.split()[k])):
    print(row)
#源代码很繁琐
