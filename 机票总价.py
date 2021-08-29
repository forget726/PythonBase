import requests
from lxml import etree


url = 'http://match.yuanrenxue.com/api/match/1?m=8ed5f41106667f8d341640318d8d17d7%E4%B8%A81626598465'
headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'http://match.yuanrenxue.com/match/1',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Pragma': 'no-cache',
    'pragma': 'no-cache',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36',
    'accept': '*/*',
    'cache-control': 'no-cache',
    'authority': 'cdn.jsdelivr.net',
    'referer': 'http://match.yuanrenxue.com/match/1',
    'Origin': 'http://match.yuanrenxue.com',
    'origin': 'http://match.yuanrenxue.com',
    'If-None-Match': '7c0faa0757b38b496ec4e56e01725536',
    'X-Requested-With': 'XMLHttpRequest',
}
res = requests.get(url,headers = headers)
print(res.status_code)