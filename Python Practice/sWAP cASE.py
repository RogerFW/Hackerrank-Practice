def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
#其实上面这行没什么用，有人说会防止程序跑错，但删了也没什么区别
    s = input()
    result = swap_case(s)
    print(result)
