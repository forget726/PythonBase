import re
import requests
from lxml import etree

url = "http://news.baidu.com"
#发送请求
req = requests.get(url)

html = req.text
html1 = etree.HTML(html)
title = html1.xpath('//*[@id="pane-news"]//li//a//text()')
addr = html1.xpath('//*[@id="pane-news"]//li//a//@href')

n = 1
for i in zip(title,addr):
    print(f'【{n}】:{i[0]} {i[1]}')
    n +=1
# 结果写入文件
# num = 1
# with open("./news.txt", "w", encoding="utf-8") as f:
#     for i in result:
#         if i[1] !="":
#             title = i[1].replace("</b>","").replace('<span class="related-video-icon"></span>',"").replace("<b>","")
#             f.write(f"{num}:{title},{i[0]}\n")
#             # f.write(f"{num}:{i[1]},{i[0]}\n")
#             print(f'{num}:{title},{i[0]}')
#             num += 1



