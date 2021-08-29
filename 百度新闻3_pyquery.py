from pyquery import PyQuery as pq
# //*[@id="pane-news"]/div/ul/li[1]/strong/a
html = pq(url="http://news.baidu.com", encoding="utf-8")
items = html("#pane-news li a")
for item in items.items():
    href = item.attr('href')
    title = item.text()
    print(title+":"+href)