# ABCDEFG
# BABCDEF
# CBABCDE
# DCBABCD
# EDCBABC

# n = int(input("请输入要打印的星星金字塔行数:"))
# for i in range(0, n + 1):  # 倒叙取值可输出倒三角
#     print(("*" * (2 * i - 1)).center((2 * n - 1), " "))
# for i in range(n - 1, 0, -1):  # 倒叙取值可输出倒三角
#     print(("*" * (2 * i - 1)).center((2 * n - 1), " "))


n = int(input("请输入要打印的星星金字塔行数:"))
# 星星之间加空格，最后一行总数为2n-1+2n-2
for i in range(0, n + 1):  # 倒叙取值可输出倒三角
    print(("* " * (2 * i - 1)).center((4 * n - 3), " "))
for i in range(n - 1, 0, -1):  # 倒叙取值可输出倒三角
    print(("* " * (2 * i - 1)).center((4 * n - 3), " "))