from urllib import request
import re

#创建url对象
url = "http://www.baidu.com"
#req = request.Request(url)

#发送请求
res = request.urlopen(url)

#获取响应
html = res.read().decode("utf-8")
#print(html)

#解析内容
content = re.search("<title>(.*)</title>",html).group(1)
print(content)
