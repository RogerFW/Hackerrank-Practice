# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(input().split())
for _ in range(int(input())):
    if not A.issuperset(set(input().split())):
        print(False)
        break
else:
    print(True)
