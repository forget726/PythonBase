# pass  # 汉诺塔移动程序******
#
#
# def move(n, a, b, c):
#     if n == 1:
#         print(a, '----->', c)
#     else:
#         move(n - 1, a, c, b)
#         print(a, '----->', c)
#         move(n - 1, b, a, c)
#
#
# move(4, 'A', 'B', 'C')
pass  # 递归二分法查找
num = [1, 2, 4, 15, 19, 34, 45, 57, 66, 72, 89, 99, 100]


def f(l, n, left=0, right=None):
    if right is None:
        right = len(l) - 1
    mid_index = (left + right) // 2
    if l[mid_index] == n:
        print(f"你所查找的数据索引是{mid_index}")
        return
    elif n > l[mid_index]:
        return f(l, n, mid_index+1, right)
    else:
        return f(l, n, left, mid_index)


f(num, 100)
