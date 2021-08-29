#filter函数应用_筛选回数
#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。

def is_palindrome(n):
    n=str(n)
    return n==n[::-1]

#python真的很强大，一行解决战斗，其中-1是步长，如果为负数为倒着取
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000的回数:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')