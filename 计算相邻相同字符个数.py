import itertools
x = ['A', 'A', 'A', 'B', 'B', 'C', 'B']
num = []
# 把相邻相同的元素放在列表，分别储存 key:元素 group:对应列表元素
for key, group in itertools.groupby(x):
    a = list(group)
    # 元素个数和元素字符串拼接并加入新的列表
    b = str(len(a))+key
    num.append(b)
num_c = "".join(num)
print(num_c)