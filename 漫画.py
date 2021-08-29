import requests

url = 'https://www.dm5.com/m1166643/'
res = requests.get(url)
print(res.content.decode())