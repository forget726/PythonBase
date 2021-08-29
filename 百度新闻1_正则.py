import re
import requests

url = "http://news.baidu.com"
#发送请求
req = requests.get(url)
#获取响应
#print(f"网页响应状态码：{req.status_code}")
#获取响应并解析
# text直接获取文件，content获取二进制文件，需要解码
# html = req.content.decode("utf-8")
html = req.text
# print(html)
#解析内容
#<a href="http://www.xinhuanet.com/politics/2021-07/08/c_1127635669.htm" target="_blank" class="a3" mon="ct=1&a=1&c=top&pn=0">恢宏史诗耀千秋</a>
#<a href="https://news.cctv.com/2021/07/08/ARTIHj3Tbivc9wTS1jJ1xpRW210708.shtml" target="_blank"  mon="r=1"><b>习近平引领南南合作释放新潜力</b></a>
#<a href="http://www.xinhuanet.com/comments/2021-07/05/c_1127624530.htm" target="_blank" class="a3" mon="ct=1&a=1&c=top&pn=1">今天的中国，多希望你们能看到</a>
#<a href="http://baijiahao.baidu.com/s?id=1704744267764412405" mon="ct=1&amp;a=2&amp;c=top&pn=7" target="_blank">中方回应欧洲议会通过涉港决议</a>
#<a href="3" target="_blank"  mon="2323">“三个深刻领悟” </a>
#      <a href="(.*?)" target="_blank"  mon=".*?">(.*?)</a>
# ct=1&amp;a=1&amp;c=top&amp;pn=0   热搜新闻mon
# r=1
# r=1
# ct=1&amp;a=1&amp;c=top&amp;pn=1
# ct=1&amp;a=2&amp;c=top&amp;pn=8
# ct=1&amp;a=2&amp;c=top&amp;pn=7
# ct=1&amp;c=top&amp;a=30&amp;pn=1   热搜词mon
# ct=1&amp;c=top&amp;a=30&amp;pn=2
# pat = '<a href="(https?://(?!www.baidu.com).*?)".*? mon=(?!"62a=9").*?>(.*?)</a>'#
#正则匹配
pat = r'<a href="(https?://(?!www.baidu.com).*?)".*?mon=(?!"&?a=9").*?>(.*?)(?!<span class="related-video-icon"></span>)</a>'
result = re.findall(pat,html)
#结果写入文件
num = 1
with open("./news.txt", "w", encoding="utf-8") as f:
    for i in result:
        if i[1] !="":
            title = i[1].replace("</b>","").replace('<span class="related-video-icon"></span>',"").replace("<b>","")
            f.write(f"{num}:{title},{i[0]}\n")
            # f.write(f"{num}:{i[1]},{i[0]}\n")
            print(f'{num}:{title},{i[0]}')
            num += 1



