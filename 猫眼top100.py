import time
import json
from requests.exceptions import RequestException
import re
import requests


# https://maoyan.com/board/4?offset=0

def get_Page(url):
    """发送网页额请求并返回响应"""
    try:
        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/63.0.3239.132 Safari/537.36',
            'Accept': '*/*',
            'Referer': 'https://maoyan.com/board/4?offset=0',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'If-None-Match': '15e37e710a93e240395866235206ed53',
            'Origin': 'https://maoyan.com',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': '__mta=149254409.1625969242610.1625973004505.1625973007274.15; uuid_n_v=v1; '
                      'uuid=B9E70A70E1EC11EBAD8677F166774E1CF3038B9E8F184C0090263A58379EFB22; '
                      '_csrf=5f729f7ab517eeba7677cf29c69246f767bba2d103c074800db2fc509455a316; '
                      'Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1625969242; '
                      '_lx_utm=utm_source%3Dbaidu%26utm_medium%3Dorganic%26utm_term%3D%25E7%258C%25AB%25E7%259C'
                      '%25BCtop100; _lxsdk_cuid=17a9351b030c8-0b9e4e2769b86d-366b4108-1fa400-17a9351b031c8; '
                      '_lxsdk=B9E70A70E1EC11EBAD8677F166774E1CF3038B9E8F184C0090263A58379EFB22; '
                      'Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1625973007; _lxsdk_s=17a9351b032-64-38-909%7C%7C31 '
        }
        res = requests.get(url, headers=headers)
        # print(res.status_code)
        if res.status_code == 200:
            html = res.text
            return html
        else:
            return None
    except RequestException:
        return None


def parse_Page(html):
    """解析网页返回结果"""
    pat = '<dd>.*?board-index-.*?">(.*?)</i>.*?title="(.*?)".*?<img data-src="(.*?)@.*?star">[\n\s]*(.*?)[\n\s]*</p>.*?releasetime">' \
          '(.*?)</p>.*?integer">(.*?)</i><i class="fraction">(.*?)</i>.*?</dd>'
    content = re.findall(pat, html, re.S)
    for movie in content:
        # print(f'No.{movie[0]}【{movie[1]}】,{movie[3]},{movie[4]},得分：{movie[5] + movie[6]}')
        yield {
            'number':movie[0],
            'tile':movie[1],
            'image':movie[2],
            'actor':movie[3],
            'time':movie[4],
            'score':movie[5]+movie[6],
        }


def write_File(content):
    '''数据写入文件'''
    with open("./猫眼top100.txt","a",encoding="utf-8") as f:
        f.write(json.dumps(content,ensure_ascii=False)+"\n")
    # pass


def main(offset):
    '''爬虫调度器，主函数'''
    url = f"https://maoyan.com/board/4?offset={offset}"
    html = get_Page(url)
    if html:
        for movie in  parse_Page(html):
            print(movie)
            write_File(movie)


if __name__ == "__main__":
    for i in range(10):
        print(f"获取第{i + 1}页信息：")
        main(i * 10)
        time.sleep(1)
    print("结束")