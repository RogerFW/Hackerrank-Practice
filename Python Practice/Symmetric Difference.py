# Enter your code here. Read input from STDIN. Print output to STDOUT
m = input()
a = set(map(int, input().split()))
n = input()
b = set(map(int, input().split()))

print(*sorted(a.symmetric_difference(b)), sep='\n')
# 此处考验的是 对symmetric_difference的直接使用，这是set中的函数
