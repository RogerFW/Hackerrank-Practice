n = int(input())
arr = map(int, input().split())
print(sorted(list(set(arr)))[-2])
#注意啊，第一行完全是没有用的，无论第多长的数列球第二大数，只需排序去倒数第二个数就行了
