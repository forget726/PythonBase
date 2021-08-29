import requests, time, hashlib, random

def sign_s(word):
    """模拟浏览器js生成签名信息"""
    nowtime = int(time.time() * 1000)
    salt = nowtime + random.randint(1, 10)
    sign = "fanyideskweb" + word + str(salt) + "Y2FYu%TNSbMCxc3t2u^XT"
    sign = hashlib.md5(sign.encode("utf-8")).hexdigest()
    return (salt, sign)

def translate(word):
    """
    传入关键字生成函数
    :param word: 传入要翻译的单词
    """
    salt, sign = sign_s(word)
    # print(salt,sign)
    url = "https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    data = {
        'i':word,
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':'dict',
        'client':'fanyideskweb',
        'salt':salt,
        'sign':sign,
        # 'lts':'1625902082718',
        # 'bv':'656f750600466990f874a839d9f5ad23',
        'doctype':'json',
        'version':'2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_REALTlME'
    }
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36',
        'Cookie':'OUTFOX_SEARCH_USER_ID_NCOO=399761432.8396654; OUTFOX_SEARCH_USER_ID=\"365903339@10.108.160.17\"; _ga=GA1.2.2090875399.1617605247; JSESSIONID=aaaeKPPNkHiMZecya7oQx; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abcMtSkSKSKy_-rWv9oQx; ___rl__test__cookies=1625901986468',
        'Referer':'https://fanyi.youdao.com/'
    }

    # 发送请求
    res = requests.post(url, data=data,headers=headers)
    if res.status_code == 200:
        json_data = res.json()
        # print(json_data)
        src = json_data["translateResult"][0][0]["src"]
        tgt = json_data["translateResult"][0][0]["tgt"]
        smartResult = json_data['smartResult']["entries"][1:]
        smartResult = "".join(smartResult)
        print(f'翻译结果：\n{src}----{tgt}')
        print(smartResult)
    else:
        print("请求失败，请检查原因！")

if __name__ == "__main__":
    while True:
        text = input("请输入要翻译的内容，回车确定输入Q退出：")
        if text.lower() == "q":
            break
        translate(text)
        print("翻译完成！")