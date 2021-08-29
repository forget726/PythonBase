# 字节流读取


from io import BytesIO

pass  # 写入字节流
# b=BytesIO()
# b.write('字节流读取练习'.encode('utf-8'))
# print(b.tell())
# #读取字节流 和内存一样，需要初始化位置为0
# b.seek(0)
# print(b.tell())
# print(b.read())
pass  # 二进制读取文件头 PNG文件头是  89 50 4E 47 0D 0A 1A 0A
import os


def ispng(file):
    """"""
    with open(file, "rb") as f:
        head = ""
        for i in range(8):
            c = f.read(1)
            # print(type(c))
            # print(format(ord(c), "02x"))
            head += format(ord(c), "02x") + " "
        head = head.replace("0x", " ").upper()
        # 字符串打印出来一样，但是实际字符串是带换行符\n的，所以用strip来清理一下
        return head.strip()


c = 0
for root, dirs, files in os.walk(r"E:\Python", ):
    # 因为会遍历下面的所有子目录，所有设定一个计数器只遍历顶级目录
    if c == 1:
        break
    # print(files)
    for file in files:
        try:
            head = ispng(file)
            # print(head)
            # print(type(head))
            if head == "89 50 4E 47 0D 0A 1A 0A":
                print(f"{file}是PNG")
                pass
        except:
            pass
    c += 1
