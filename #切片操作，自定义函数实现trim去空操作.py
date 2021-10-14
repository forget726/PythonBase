# 切片操作，自定义函数实现trim去空操作
'''
def trim(s):
    if(s==None or s == ''):
        return ''
    # 左侧空格
    while(s[:1] == ' ' ):
        s = s[1:]
    # 右侧空格
    while(s[-1:] == ' ' ):
        s = s[:-1]
    return s'''


# 上面网上复制例子，加入了非空和无效判断，下面自己写的没加也正常！
def trim(s):
    while (s[:1] == ' '):
        s = s[1:]
    while (s[-1:] == ' '):
        s = s[:-1]
    return s


if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print('测试失败6!')
else:
    print('测试成功!')

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

d = {'a': 1, 'b': 2, 'c': 3}

# 格式化参数复习 format方式
for k, v in d.items():
    print('这个dict中{0}对应的元素为：{1}'.format(k, v))

# 格式化参数复习 %方式
for i, value in enumerate(['A', 'B', 'C']):
    print('该list中第%s位的元素为：%s' % (i, value))

# 格式化参数复习 f-string方式

for i, value in enumerate(['A', 'B', 'C']):
    print(f'该list1中第{i}位的元素为：{value}')
