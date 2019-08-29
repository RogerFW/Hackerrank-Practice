# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
X = int(input())
Size = Counter(map(int, input().split()))
N = int(input())
cost = 0
for _ in range(N):
    size, price = map(int, input().split())
    if Size[size]:
        cost += price
        Size[size] -= 1
print(cost)
