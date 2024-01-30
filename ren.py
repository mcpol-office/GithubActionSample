import random
import sys
import time

print("+--------------------------------------+")
print("|                                      |")
print("|         花有重开日， 人无再少年          |")
print("|                                      |")
print("|               欢迎游玩                 |")
print("|            人生重开模拟器               |")
print("+--------------------------------------+")

"""
设置初始属性
颜值，体质，智力，家境
每一项最小值1，最大值10，总和不超过10
"""
print("设置初始属性（可用点数为20）")
appearance = int(input("请输入颜值点数(1 - 10)>:"))
physical = int(input("请输入体质点数(1 - 10)>:"))
intelligence = int(input("请输入智力点数(1 - 10)>:"))
family = int(input("请输入家境点数(1 - 10)>:"))

if appearance < 1 or appearance > 10:
    print("颜值点数设置错误，请输入正确点数(1 - 10)")
    while appearance < 1 or appearance > 10:
        appearance = int(input("请输入颜值点数(1 - 10)>:"))

if physical < 1 or physical > 10:
    print("体质点数设置错误，请输入正确点数(1 - 10)")
    while physical < 1 or physical > 10:
        physical = int(input("请输入体质点数(1 - 10)>:"))

if intelligence < 1 or intelligence > 10:
    print("智力点数设置错误，请输入正确点数(1 - 10)")
    while intelligence < 1 or intelligence > 10:
        intelligence = int(input("请输入智力点数(1 - 10)>:"))

if family < 1 or family > 10:
    print("家境点数设置错误，请输入正确点数(1 - 10)")
    while family < 1 or family > 10:
        family = int(input("请输入家境点数(1 - 10)>:"))

while appearance + physical + intelligence + family > 20:
    print("输入点数总和大于20，请重新输入！")
    appearance = int(input("请输入颜值点数(1 - 10)>:"))
    physical = int(input("请输入体质点数(1 - 10)>:"))
    intelligence = int(input("请输入智力点数(1 - 10)>:"))
    family = int(input("请输入家境点数(1 - 10)>:"))

print(f"当前 颜值：{appearance} 体质：{physical} 智力：{intelligence} 家境：{family} "
      f"成功设置初始点数！开始享受人生吧！\n")

# 使用random.randint(begin, end)，可以生成一个[begin, end]之间的随机数
# 使用1-6的随机数，产生类似骰子的效果
point = random.randint(1, 6)

# 设定角色的性别
if point % 2 == 1:
    sex = "boy"
    print("你出生了，是个男孩")
    print("")
    print("+--------------------------------------+")
else:
    sex = "girl"
    print("你出生了，是个女孩")

# 设定角色的出生点
if family == 10:
    print("你出生在市中心的别墅，你的父母都是达官显贵")
    intelligence += 3
    appearance += 2
    family += 1
elif family >= 7:
    if point >= 5:
        print("你出生在市中心的花儿洋房，你的父母是企业老板")
        appearance += 1
        physical += 1
    elif point >= 3:
        print("你出生在大城市的居民楼中，你的父母是公务员")
        appearance += 1
        physical += 1
        intelligence += 2
    else:
        print("你出生在大城市的房子里，你的父母是大学老师")
        physical += 1
        intelligence += 3
elif family >= 3:
    if point == 6:
        print("你出生在二线城市，你的父母是医生")
        physical += 3
    elif point >= 3:
        print("你出生在县上，你的父母是小学老师")
        intelligence += 2
    else:
        print("你出生在县上，你的父母是超市老板")
        family += 1
else:
    if point >= 5:
        print("你出生在农村，你的父母是村里书记")
        intelligence -= 1
        physical += 1
    elif point >= 3:
        print("你出生在中国最穷的村里，你的父母是无业游民")
        appearance -= 2
        intelligence -= 2
        physical -= 1
    else:
        print("你出生在公共厕所里，你的父母把你抛弃了")
        appearance -= 3
        intelligence -= 3
        physical -= 3
        family -= 3
print("")
print(f"当前 颜值：{appearance} 体质：{physical} 智力：{intelligence} 家境：{family} ")
print("+--------------------------------------+")
time.sleep(3)

# 童年阶段
for age in range(1, 11):
    info = f"你今年{age}岁了，"
    point = random.randint(1, 3)
    if sex == "girl" and family <= 3 and point == 1:
        info += "你家里重男轻女，家里吃不上饭，于是把你遗弃了"
        print(info)
        print(f"你活了{age}岁，游戏结束！")
        sys.exit(0)
    elif physical < 3 and point < 3:
        info += "你生了一场大病"
        if family > 6:
            info += "你父母给你花了很多钱，终于治好了"
            family -= 1
        else:
            info += "你父母没钱给你治病，你落下终身病根"
            family -= 1
            physical -= 2
    elif appearance < 3 and age < 3 and point > 2:
        info += "你父母觉得你太丑了，把你扔在厕所里了"
        print(info)
        print(f"你活了{age}岁，游戏结束！")
        sys.exit(0)
    elif appearance < 3 and age > 5 and point < 2:
        info += "你长得太丑了，小朋友们都不跟你玩，"
        if intelligence > 5:
            info += "你决定好好学习"
            intelligence += 1
        else:
            info += "你经常烦你的爸妈，你的家庭变得很不和谐"
            family -= 1
    elif family > 6 and point > 2:
        if sex == "girl":
            info += "你的父母经常给你买洋娃娃"
            appearance += 1
        else:
            info += "你的父母经常给你买变形金刚"
            intelligence += 1
    elif intelligence < 4 and point < 2:
        info += "你看起来很傻的样子，"
        if family > 7:
            if point > 2:
                info += "你的父母把你送到私立学校"
                intelligence += 2
            else:
                info += "你的父母给你找了一个私人辅导老师"
                intelligence += 1
        elif family > 4:
            info += "你的父母总是逼你学习"
            family -= 1
        else:
            if sex == "girl":
                info += "你的父亲骂母亲不会生"
                family -= 1
            else:
                info += "你经常出去打闹，成为了一个混混"
                physical += 1
                intelligence -= 3
    else:
        info += "又是平平无常的一年，"
        if point == 1:
            info += "你越来越活泼了"
            family += 1
        elif point == 2:
            if sex == "girl":
                info += "你越来越高了"
                physical += 1
            else:
                info += "你越来越好看了"
                appearance += 1
        else:
            pass
    print(info)
    print("")
    print(f"当前 颜值：{appearance} 体质：{physical} 智力：{intelligence} 家境：{family} ")
    print("+--------------------------------------+")
    time.sleep(3)
