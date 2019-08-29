# Enter your code here. Read input from STDIN. Print output to STDOUT
K = int(input())
room_list = list(map(int, input().split()))
sum_room_list = sum(room_list)
sum_room_set = sum(set(room_list))
diff = sum_room_set * K - sum_room_list
print(diff // (K - 1))
