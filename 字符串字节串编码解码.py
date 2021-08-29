# 我们Python3语言里面的字符串对象是unicode字符串，在内存中实际存储时，使用的是 UTF16 编码。
# 但是我们通常不会将UTF16编码的内容写到磁盘或者在网络进行传输， 因为utf16编码比较浪费空间。
# 特别是如果文字信息基本都是英文符号的情况下， utf16 都会用2个字节来代表英文符号。 一个字节其实就够了。
# 所以，Python语言要对字符串对象 进行存储和传输的时候，通常要使用字符串的encode方法，参数指定编码方式，编码为一个 bytes 对象。
# bytes对象的底层就是用一个个的字节来存储字符串中的文字的。
# 同样的字符串，用不同的编码方式，有时会产生不同的bytes结果。
# encode方法返回的是编码后的字节串对象bytes 编码为字节串对象 bytes 就可存储到文件或者传输到网络中去了。
# 我们后面的学习会讲如何进行文件存储和网络传输
pass  # Unicode编码成指定格式--参数指定要编码成的格式
print("编码".center(40, "*"))
print("你好".encode("utf8"))
print("你好".encode("gbk"))
pass  # 解码成Unicode--参数指定要解码的字符串格式
print("解码".center(40, "*"))
print(b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode('utf8'))
print(b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode('gbk'))  # 解码格式错误导致输出文字异常
# 解码格式错误--因为中文是占3个字节，而这个字节串是4个字节，所以应该是gbk
try:
    print(b'\xc4\xe3\xba\xc3'.decode('utf8'))
except UnicodeError:
    print("解码格式错误！")
pass  # 编码解码技巧
print("编解码技巧".center(40, "*"))
# 把 unicode数字转换为字符， 使用函数 chr() , 比如：
print(chr(50))
print(chr(20013))
print(chr(0x4e2d))  # 0x开头表示数字是16进制
# 反过来，要把 字符转换为对应的unicode数字，使用函数 ord()
# 该函数参数字符串里面只能有一个字符
print(ord("2"))
print(ord("中"))
# 字符串编码为 unicode转义数字
# 除了utf8，gbk 还有一种常见的编码方式，叫做 unicode-escape ，就是直接用unicode数字字符串表示字符，如下所示
print('白月黑羽'.encode('unicode-escape'))
# 用unicode转义数字 写字符串
print('\u767d\u6708\u9ed1\u7fbd')
# 直接用16进制数字创建 bytes
print(b'\xb0\xd7\xd4\xc2\xba\xda\xd3\xf0'.decode('gbk'))
# 字节串 和 16进制表示字节的字符串
print(b'hello,123'.hex())
# 反向操作，把 16进制表示字节的字符串 转化为 字节串就是
print(bytes.fromhex('68656c6c6f2c313233'))
