"""
Craps赌博游戏
规则：玩家和庄家，玩家掷两个骰子，每个骰子点数为1-6，如果第一次点数和为7或11，则玩家胜；
如果点数和为2、3或12，则玩家输庄家胜。
若和为其他点数，则记录第一次的点数和；
玩家继续掷骰子，如果两个骰子点数和等于刚才记录的第一次掷出的点数和，则玩家胜；若掷出的点数和为7则庄家胜；否则继续掷骰子直到分出胜负。
"""
from random import randint


def main():
    money = 1000
    while money > 0:
        print("你的赌资余额是：", money)
        needs_go_on = False  # 当前局是否需要下一轮

        while True:
            debt = int(input('请下注: '))
            if debt > 0 and debt <= money:  # 下注的钱要足够
                break

        first = randint(1, 6) + randint(1, 6)  # 两个骰子
        print("玩家摇出了%d点" % first)

        if first == 7 or first == 11:
            print("玩家胜")
            money += debt
        elif first == 2 or first == 3 or first == 12:
            print("庄家胜")
            money -= debt
        else:
            needs_go_on = True

        while needs_go_on:
            current = randint(1, 6) + randint(1, 6)
            print("玩家摇出了%d点" % current)
            if current == 7:
                print("庄家胜！")
                money -= debt
                needs_go_on = False
            elif current == first:
                print("玩家胜！")
                money += debt
                needs_go_on = False

    print("你没钱了，游戏结束！")


if __name__ == '__main__':
    main()