import requests
from Crypto.Cipher import AES

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64'
                        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73'}
url = 'https://v10.dious.cc/20210819/lVZEP1AV/1000kb/hls/index.m3u8'
key = 'f2095ba0bfdafeff'.encode('utf-8')
response1 = requests.get(url).text
print(response1)
# exit()
m3u8 = []
with open('mulu','w+',encoding='utf-8') as file:
    file.write(response1)
    file.seek(0,0)
    lst = file.readlines()
    for i in lst:
        i = i.strip()
        if i.startswith('#'):
            continue
        else:
            m3u8.append(i)
print(f'目标文件数共{len(m3u8)}个')
print(m3u8)
exit()
for i in range(len(m3u8)+1):
    print(f'第{i+1}个ts文件准备下载中。')
    while True:
        try:
            with open(f'{i+1}.ts','wb') as file:
                response = requests.get(m3u8[i],headers=headers).content
                # 加密，会出问题
                # cryptor = AES.new(key, AES.MODE_CBC, key)
                # file.write(cryptor.decrypt(response))
                file.write(response)
            break
        except:
            continue
    print(f'第{i+1}个ts片段已下载完成!')