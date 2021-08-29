import turtle

pass  # 写入二进制字符
# s = "1100011011011111110011111010011010111111111011001100000011010110"
# # n = [int(s[i:i + 8], 2) for i in range(0, len(s), 8)]
# # content = bytes(n)
# content = s.encode("utf8")
# print(type(content))
# print(content)
# # print(bytes(s, "ascii"))
# # exit()
# fp = open("./text.txt", "wb")
# print(content, file=fp)
# fp.close()
pass  # 字符串的转化
# import requests
#
# if __name__ == "__main__":
#     # 1.指定url
#     url = 'https://www.mxbc.com/api/nearby_stores?latitude=34.511949&longitude=109.761417'
#
#     # 3.进行UA伪装
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko Core/1.70.3870.400 QQBrowser/10.8.4405.400'
#     }
#
#     # 2.访问参数设置 post访问
#     # name = input('请输入地名')
#
#     data = {
#         'cname': '',
#         'keyword': '',
#         'pageIndex': '1',
#         'pageSize': '10',
#         'pid': '',
#     }
#
#     # 4.请求发送
#     response = requests.get(url=url, headers=headers)
#     # response.encoding = 'utf8'
#
#     # 5.获取响应数据
#     data_text = response.text
#     # print(data_text)
#
#     # 正则表达式
#     import re
#
#     data = ""
#     r = re.compile(r'"name":"(.+?)".+?:"(.+?)".+?:"(.+?)".+?:(".+?"|null).+?:"(.+?)"')
#
#     for dic in r.findall(data_text):
#         a = dic[0]
#         # data+= "编号:"+a+"\t店名:"+dic[1]+"\t地址:"+dic[2]+"\t待遇:"+eval(dic[3])+"\t."+dic[4]+"\n"
#         data += dic[0] + dic[1] + dic[2] + dic[3] + dic[4] + "\n"
#     # print(data.encode().decode("unicode_escape"))
#     # print(s)
#     # print(data.encode())
#     print(data.encode().decode("unicode_escape"))
#
#
#     # # 6.进行持久化存储
#     # fileName = 'name' + '.json'
#     # with open('D:\软件\Python\python案例\wy-' + fileName, 'w', encoding='utf-8') as fp:
#     #     fp.write(data_text)
#     # print('写入完成')

v = 10
n = 3
aver = [round(v/n, 2) for i in range(n)]
aver[n - 1] = v - sum(aver[:-1])
print(aver)
