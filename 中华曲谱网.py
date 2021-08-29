import requests
import re
import execjs
from lxml import etree

url = "http://www.qupu123.com/qiyue/dixiao/p335848.html"

headers = {
    'referer': 'http://www.qupu123.com/qiyue/dixiao/p335848.html',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36'
}

res = requests.get(url, headers=headers)
content = res.text
html = etree.HTML(content)
img_html1 = html.xpath('//*[@class="imageList"]//img/@src')
# print(img_html1[0])


prefix = 'http://www.qupu123.com'
pat1 = r'<script>showopern\((.*?),"(.*?)"\);</script>'
items = re.findall(pat1, content)
a, key = items[0][0], items[0][1]
pat2 = f'{a}="(.*?)";var opernTitle'
string = re.findall(pat2, content)
# print(string, key)
with open('./qupu.js', encoding='utf-8') as f:
    jscode = f.read()
# print(jscode)
# js = execjs.compile(jscode)
img_html = execjs.compile(jscode).call("showopern", string[0], key)
img_html = img_html.split("|")[0]
img = prefix + img_html
img_start = prefix + img_html1[0]
print(img_start, "\n", img)
