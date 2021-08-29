# 内存读写

# 写入内存
from io import StringIO

f = StringIO()
f.write('string\n')
f.write('IO\n')
f.write('read and write')
print(f.getvalue())
# 读取内容  StringIO读取必须初始化位置为0
# f = StringIO('String\nIO\nRead and Write')

f.seek(0)
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
