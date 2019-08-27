def commdr(arr, instruct): 
    if instruct[0] == 'insert':
        arr.insert(int(instruct[1]), int(instruct[2]))
    elif instruct[0] == 'print':
        print(arr)
    elif instruct[0] == 'remove':
        arr.remove(int(instruct[1]))
    elif instruct[0] == 'append':
        arr.append(int(instruct[1]))
    elif instruct[0] == 'sort':
        arr.sort()
    elif instruct[0] == 'reverse':
        arr.reverse()
    elif instruct[0] == 'pop':
        arr.pop()
    else: 
        print("Command not recognized!")

N = int(input()) 
arr = []
for command in range(0,N):
    temp = [str(i) for i in input().strip().split()]
    commdr(arr, temp)
