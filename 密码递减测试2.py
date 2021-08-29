msg='请输入密码：'
i = 3
while i > 0:
    pwd = int(input(msg))
    if pwd == 123:
        break
    else:
        i -=1
        msg = f'密码错误，你还有{i}次机会'

if i == 0:
    print("密码次数已经用完，已锁定")
else:
    print("密码正确")