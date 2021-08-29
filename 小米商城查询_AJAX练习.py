from pyquery import PyQuery as pq
import time
import requests
import ssl
import re

ssl._create_default_https_context = ssl._create_unverified_context  ##33 close certified

# url:https://api2.order.mi.com/product/view?product_id=10000280&version=2&t=1626157305


headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36',
    'Accept': '*/*',
    'Referer': 'https://www.mi.com/buy/detail?product_id=10000280',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'If-Modified-Since': 'Wed, 18 Apr 2018 07:05:29 GMT',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36',
    'accept': '*/*',
    'referer': 'https://www.mi.com/buy/detail?product_id=10000280',
    'authority': 'api2.service.order.mi.com',
    'cookie': 'xmuuid=XMGUEST-230DEDB0-9D97-11EB-AF14-BDFF3A94B217; mstuid=1618455802307_6491; axmuid=1eZxY4FhcEXJk9s2BfOSc47FWXxjtD6ePGbVlU0t^%^2BUQ^%^3D; deviceId=xmdevice_6f7azuf0khvm7umv; XM_agreement=0; Hm_lvt_c3e3e8b3ea48955284516b186acf0f4e=1623895433,1626153976; api_order_www_mi_com.minicart.xm_user_www_num=0; pageid=0e5519feb6002210; xm_vistor=1618455802307_6491_1626153976650-1626155145136; mstz=^|^|1524169929.230^|^|https^%^253A^%^252F^%^252Fwww.mi.com^%^252Fredmik40ultra-k40pro^|https^%^25253A^%^25252F^%^25252Fwww.mi.com^%^25252Fredmik40ultra-k40pro; Hm_lpvt_c3e3e8b3ea48955284516b186acf0f4e=1626155145',
    'origin': 'https://www.mi.com',
    'If-None-Match': '24602097cdd9d54ac1ae5b234eb405c2',
    'content-type': 'application/json;charset=UTF-8',
    'Pragma': 'no-cache',
}
phoneheaders = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36',
    'Accept': '*/*',
    'Referer': 'https://www.mi.com/p/1915.html',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'If-Modified-Since': 'Tue, 18 May 2021 02:06:43 GMT',
    'If-None-Match': '24602097cdd9d54ac1ae5b234eb405c2',
    'access-control-request-method': 'POST',
    'origin': 'https://www.mi.com',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36',
    'accept': 'application/json, text/plain, */*',
    'authority': 'tk.d.mi.com',
    'access-control-request-headers': 'content-type',
    'content-type': 'application/json;charset=UTF-8',
    'referer': 'https://www.mi.com/p/1915.html',
}


def gettime():
    '''生成时间戳'''
    timetamp = int(time.time() * 1000) + int(18e5)
    # print(timetamp)
    return (timetamp // 1000)


# 获取主页所有手机名称和对应的product_id
phonepage = 'https://www.mi.com/p/1915.html'
doc = pq(url=phonepage)
# print(doc)
info = doc('[type="text/javascript"]').text()
# print(info)
pat = 'product_id":"(.*?)","product_name":"(.*?)","product_org_price":'
info_n = re.findall(pat, info)

info_dic = {}
for i in info_n:
    info_dic[i[1]] = i[0]
    print(i[1],end=",")
c = input("\n请输入你要查询的商品:")
if c not in info_dic:
    print("输入有误，程序结束！")
else:
    pid = info_dic[c]


# 获取页面商品信息
nowtime = gettime()
url = 'https://api2.order.mi.com/product/view?product_id='+pid+'&version=2&t='+str(nowtime)
# print(url)
res = requests.get(url,headers=headers)
print(res.json())
