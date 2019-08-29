# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
N = int(input())
arr = input().split()
K = int(input())
comb_list = list(combinations(arr, K))
a_list = [e for e in comb_list if 'a' in e]
print(len(a_list) / len(comb_list))
