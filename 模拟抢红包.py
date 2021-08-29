import random

while True:
    print("如果要退出，请每次开始的时候输入0即可")
    s = input("输入金额和人数\n提示:中间用空格隔开：").split()

    if s == "0":
        break
    v = int(s[0])  # 金额
    n = int(s[1])  # 人数
    bag = []
    flag = int(input("输入1或2\n输入1为普通红包\n输入2为随机红包："))
    if flag == 1:
        bag = [round(v/n, 2) for i in range(n)]
        bag[n-1] = v - sum(bag[:-1])
        print("情况", bag)
    elif flag == 2:
        for i in range(n):
            t = random.uniform(v / (2*n), v / n)
            t = round(t, 2)
            bag.append(t)
            v = v - t
            v = round(v, 2)
        print("情况", bag)
    else:
        print("输入错误！！程序结束！")
