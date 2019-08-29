# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    n = int(input())
    sides = list(map(int, input().split()))
    i = 0
    while i < n - 1 and sides[i] >= sides[i + 1]:
        i += 1
    while i < n - 1 and sides[i] <= sides[i + 1]:
        i += 1
    print('Yes' if i == n - 1 else 'No')
