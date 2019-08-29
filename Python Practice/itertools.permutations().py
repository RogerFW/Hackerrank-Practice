# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
string, permutation_size = input().split()
for permutation in itertools.permutations(sorted(string), int(permutation_size)):
    print(''.join(permutation))
