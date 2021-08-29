# 文件读写

f = r'E:\3.txt'

pass  # 1.全部读写

# with open(f,'r',encoding='utf-8') as s:
#     print(s.read())


pass  # 2.readlines()全部读取

# with open(f,'r',encoding='utf-8') as s:
#     for l in s.readlines():
#         print(l.strip())

pass  # 3.readline读取一行
with open(f, 'r', encoding='utf-8') as s:
    print(s.read())
    s.seek(0)
    print(s.readlines())
    s.seek(0)
    print(s.read().splitlines())

