# map reduce函数应用
# 1.利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
from functools import reduce


def normalize(name):
    l = [name[i].upper() if i == 0 else name[i].lower() for i in range(len(name))]
    print("l:", l)
    n = ""
    for i in l:
        n = n + i
    return n


'''
def normalize(name):
    n=1    
    for i in name[n]:
        str=i[:1]
        print(str)
        if ord(str)<=90:
            str=chr(ord(str)+32)
            k=i[1:]
        for j in k:
            if ord(j)>=97:
                j=chr(ord(j)-32)
                str=str+j
    return str
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
'''


# 2.Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(L):
    def mul(x, y):
        return x * y

    return reduce(mul, L)


# 3.利用map和reduce编写一个str2float函数
def s2l(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    def fn(x, y):
        return x * 10 + y

    def char2l(s):
        return digits[s]

    return reduce(fn, map(char2l, s))
