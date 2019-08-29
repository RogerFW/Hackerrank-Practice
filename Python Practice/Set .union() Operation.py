# Enter your code here. Read input from STDIN. Print output to STDOUT
n,A = input(), set(map(int, input().split())) 
m,B = input(), set(map(int, input().split())) 
print(len(A.union(B)))
