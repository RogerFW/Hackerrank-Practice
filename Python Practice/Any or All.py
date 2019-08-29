# Enter your code here. Read input from STDIN. Print output to STDOUT
_ = input()
n = input().split()
print(all([int(i) > 0 for i in n]) and any([j == j[::-1] for j in n]))
#专门查一下palindromic number是什么意思，就是按照书写，从左往右也是这么样，从右往左也一样，左右对称的数据，0，1，2...101,111,121...
