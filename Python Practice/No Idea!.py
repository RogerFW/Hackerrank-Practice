n, m = input().split()
array = input().split()
A = set(input().split())
B = set(input().split())
print(sum([(i in A) - (i in B) for i in array]))
#不用过度在意，A、B两个set的输入长度，虽说是根据m而确定的，但是如果多输入一个结果就会不对。
#但是这个题目本身test sample设定不会故意刁难你让你在输入上加条件，所以这个code可以直接使用。
