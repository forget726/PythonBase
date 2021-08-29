# -*- coding: utf-8 -*-
h = float(input("请输入身高（米）："))
w = float(input("请输入体重（kg）："))
bmi =w/(h*h)
if bmi>32:
    print("严重肥胖")
elif bmi>=28:
    print("肥胖")
elif bmi>=25:
    print("过重")
elif bmi>=18.5:
    print("正常")
else:
    print("过轻")
