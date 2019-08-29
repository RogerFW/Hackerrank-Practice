# Enter your code here. Read input from STDIN. Print output to STDOUT
N = input()
A = set(map(int, input().split())) 

for _ in range(int(input())):
    command = input().split()[0]
    elements = input().split()
    command += '([' + ','.join(elements) + '])'
    eval('A.' + command)
print(sum(A))
