#ASCII码判断大小写，然后转换

def normalize(name):

    # 初始化首字母大写
    str = name[0]
    if ord(str) >= 97:
        str = chr(ord(str) - 32)
    # 遍历首字母外的每个字符，大小写转换
    for j in name[1:]:
        if ord(j) <= 90:
            k = chr(ord(j) + 32)
            j = k
        str = str + j
    return str

L1 = ['adam', 'LISA', 'barT', 'long']
L2 = list(map(normalize, L1))
print(L2)