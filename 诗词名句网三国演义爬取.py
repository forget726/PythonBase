import requests
from lxml import etree

url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
res = requests.get(url)
html = etree.HTML(res.content.decode())
content = html.xpath('//*/div[@class="book-mulu"]//a/text()')
for i in content:
    print(i)
