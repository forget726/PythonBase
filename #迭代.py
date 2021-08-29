# 迭代
def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    else:
        min = L[0]
        for n in L:
            if n <= min:
                min = n
        max = L[0]
        for i in L:
            if i >= max:
                max = i
    print(min, max)
    return min, max


s = (5, 6, 0, 9, 5, 7, 6, 1, 3)
findMinAndMax(s)
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
