import random
import time


def Game(name):
    print(f"亲爱的【{name}】,让我们来玩石头剪刀布的游戏吧，三局两胜制！")
    c = 0
    u = 0
    i = 0
    dic = {1: "石头", 2: "剪刀", 3: "布"}
    while i < 3:
        i += 1
        if (c == 2) or (u == 2):
            break
        user = int(input(f"请选择你要出的手势数字(第{i}局)：\n"
                         f"1.石头 2。剪刀 3.布:\n"))
        computer = random.randint(1, 3)
        print(f"电脑出的是【{dic[computer]}】，"
              f"【{name}】出的是{dic[user]}")

        if ((user == 1 and computer == 3)
            or (user == 2 and computer == 1)
            or (user == 3 and computer == 2)):
            print(f"没猜中吧，加油哦，再来！\n")
            c += 1
        elif user == computer:
            print(f"哈哈，竟然这么心有灵犀！\n")
        else:
            print(f"可恶，竟然被你猜中了，我不服气！\n")
            u += 1

    print("\n\n正在统计结果，请稍等……")
    time.sleep(1)
    if c > u:
        print(f"最终结果：【电脑】{c}:【{name}】{u}，你还是不行啊！")
    elif u > c:
        print(f"最终结果：【电脑】{c}:【{name}】{u}，竟然输给你了！")
    else:
        print(f"打平了！青山不改，绿水长流，再见{name}！")


name = input("请输入您的名字开始游戏：")

while True:
    Game(name)
    choice = input(f"是否还要再来一局，【{name}】？请选择：（Y/N）")
    choice_l = choice.lower()

    if choice_l == "y":
        print(f"嘿嘿，【{name}】不怕死的还来？\n\n")
    elif choice_l == "n":
        print(f"棋逢对手，后会有期【{name}】！")
    # if choice_l in ["y","Y"]:
    #     print(f"嘿嘿，【{name}】不怕死的还来？\n\n")
    # elif choice_l\
    #         in ["n","N"]:
    #     print(f"棋逢对手，后会有期【{name}】！")
        break
    # else:
    #     print("\n\n输入有误，请重新输入")
