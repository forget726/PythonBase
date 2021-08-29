# 问题描述
# 　　153是一个非常特殊的数，它等于它的每位数字的立方和，即153=1^3+5^3+3^3(python中几次方用**表示)。编程求所有满足这种条件的三位十进制数。
# 输出格式
# 　　按从小到大的顺序输出满足条件的三位十进制数，每个数占一行。

i = 100
while i <= 999:
    a = sum(map(lambda x:int(x)**3,str(i)))
    if a == i:
        print(i)
    i +=1