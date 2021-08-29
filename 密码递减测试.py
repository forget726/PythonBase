def pwd_check(str):
    i = 1
    while i < 4:

        pwd = input("请输入密码：")
        if pwd == str:
            print("密码正确，等待跳转……")
            break
        else:
            print("密码错误，请重新输入。")
            print("您还有%d次机会" % (3 - i))
            if i == 3:
                print("密码输入错误次数超过3次，请30分钟后再试")
            i += 1

            continue
pwd_check('15225126382')