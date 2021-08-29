# 问题描述
# 　　123321是一个非常特殊的数，它从左边读和从右边读是一样的。
# 　　输入一个正整数n， 编程求所有这样的五位和六位十进制数，满足各位数字之和等于n 。
# 输入格式
# 　　输入一行，包含一个正整数n。
# 输出格式
# 　　按从小到大的顺序输出满足条件的整数，每个整数占一行。
# 样例输入
# 52
# 样例输出
# 899998
# 989989
# 998899
# 数据规模和约定
# 　　1<=n<=54。
import time

n = int(input("input a number:"))
start = time.time()
for i in range(10000, 1000000):
    s = sum(map(int, str(i)))
    if (s == n) and (str(i) == str(i)[::-1]):
        print(i)
end = time.time()
print(end - start)
