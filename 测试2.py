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

import requests,re

url = "https://ntrl.ntis.gov/NTRL/"
session = requests.session()
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36',
    # 'cookie': 'JSESSIONID=ea055607b3f8e3308d2ffd9b2aa9; _ga=GA1.2.1599422909.1633943581; _gid=GA1.2.1800619834.1633943581; _ga=GA1.3.1599422909.1633943581; _gid=GA1.3.1800619834.1633943581; _gat_gtag_UA_146094634_1=1; _gat_UA-146094634-1=1; AWSALB=OeJ0WNB00+8G29pZ79gJ+6QrZhHFJjQzG/j6WqwnVpAR/XsHKY1g/MXiT66aoAiI0j949vga6sx8clMmfCoFRKxBWktu2nUwTkHZGplUPPBC8mVwRoY54EWoHtMO; AWSALBCORS=OeJ0WNB00+8G29pZ79gJ+6QrZhHFJjQzG/j6WqwnVpAR/XsHKY1g/MXiT66aoAiI0j949vga6sx8clMmfCoFRKxBWktu2nUwTkHZGplUPPBC8mVwRoY54EWoHtMO'
}
html = session.get(url,)
res = html.text
pat = 'name="javax.faces.ViewState" value="(.*?)"'
txt = re.findall(pat, res)
print(txt[0])

data = {
    'javax.faces.partial.ajax': 'true',
    'javax.faces.source': 'searchResultsForm:searchResultsTable',
    'javax.faces.partial.execute': 'searchResultsForm:searchResultsTable',
    'javax.faces.partial.render': 'searchResultsForm:searchResultsTable',
    'javax.faces.behavior.event': 'page',
    'javax.faces.partial.event': 'page',
    'searchResultsForm:searchResultsTable_pagination': 'true',
    'searchResultsForm:searchResultsTable_first': '20',
    'searchResultsForm:searchResultsTable_rows': '10',
    'searchResultsForm:searchResultsTable_skipChildren': 'true',
    'searchResultsForm:searchResultsTable_encodeFeature': 'true',
    'searchResultsForm': 'searchResultsForm',
    'searchResultsForm:searchResultsTable:globalFilter': '',
    'searchResultsForm:searchResultsTable:sortByDropDown_focus': '',
    'searchResultsForm:searchResultsTable:sortByDropDown_input': 'searchRelevance',
    'searchResultsForm:searchResultsTable:sortOrderDropDown_focus': '',
    'searchResultsForm:searchResultsTable:sortOrderDropDown_input': 'DESC',
    'searchResultsForm:searchResultsTable_rppDD': '10',
    'searchResultsForm:searchResultsTable_rppDD': '10',
    'searchResultsForm:searchResultsTable_selection': 'PB2000103486',
    'javax.faces.ViewState': txt[0]
}
html2 = session.post(url, data=data, headers=headers)
print(html2.text)
