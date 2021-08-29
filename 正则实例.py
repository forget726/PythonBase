import re

# 取IP
ping_ss = ' Reply from 192.168.3.166: bytes=32 time=3ms TTL=47'

# FT大佬代码  取47
print(re.findall(r'((?<=TTL=)\d+)', ping_ss))

# print(res. group(0))
# mat=re.search(r'(time=)(\d+\w+) (TTL=)(.+)',ping_ss)
# mat=re.search(r'((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}',ping_ss)

# 网上搜索的方法 判断+取值
mat = re.search(r'([0,1]?\d{1,2}|2([0-4][0-9]|5[0-5]))(\.([0,1]?\d{1,2}|2([0-4][0-9]|5[0-5]))){3}', ping_ss)
with open("ip.txt", "a") as f:
    f.write(mat.group(0) + "\n")
# mat=re.search(r'(\d{1,3}.){3}\d{1,3}',ping_ss)
print(mat.group(0))

# ([0,1]?\d{1.2}|2([0-4][0-9]|5[0-5])) 取值分三部分 1~199 200~249 250~255
# (\.[0,1]?\d{1.2}|2([0-4][0-9]|5[0-5])){3}
