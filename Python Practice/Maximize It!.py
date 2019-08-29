# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
K, M = map(int, input().split())
arr = []
for _ in range(K):
    arr.append(list(map(int, input().split()))[1:])
result = 0
for combination in product(*arr):
    result = max(sum([pow(x,2) for x in combination]) % M, result)
print(result)
