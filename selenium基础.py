import time

from selenium import webdriver

d = webdriver.Chrome()
d.get("https://www.baidu.com")
time.sleep(10)
d.close()