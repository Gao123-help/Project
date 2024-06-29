"""
    可以录入商品名称
    可以录入商品编号
    可以录入商品价格，要求商品的价格有零有整
    可以录入商品折扣，要求商品的折扣有零有整
    可以录入商品件数， 要求件数必须为整数
    打印，您购买了xx商品xx件，累计原价xx元，现价xx元，累计折扣xx折，欢迎下次光临！
    如果消费的总金额超过100元，请在控制台打印True，否则打印False
"""
# sName = input("请录入商品名称：")
# sSerious = input("请录入商品编号：")
# dPrice = float(input("请录入商品价格："))
# dDisCount = float(input("请录入商品折扣："))
# iAmount = int(input("请录入商品件数："))
#
# print(
#     f"您购买了{sName}商品{iAmount}件，累计原价{dPrice * iAmount}元，现价{dPrice * iAmount * dDisCount:.2f}元，累计折扣{dDisCount * 10}折，欢迎下次光临！")
# if dPrice * iAmount * dDisCount > 100:
#     print("True")
# else:
#     print("False")

"""
已知三角形三边分别为3，4，5，请按要求计算此三角形面积。
    控制台输入3，作为边a长度
    控制台输入4，作为边b长度
    控制台输入5，作为边c长度
"""

# num_list = [float(input(f"请输入第{i + 1}个数字: ")) for i in range(3)]
# print(f"此三角形的面积为{num_list[0] * num_list[1] * 0.5:.2f}")

import math

# fpi = math.pi
# r1 = 3.0
# r2 = 1.0
# print(f"阴影部分面积为{fpi * (r1 ** 2 - r2 ** 2):.2f}")
#
# # 计算点到直线的距离
# A = (-1.0, 1.0)
#
# tmp1 = abs(1 * A[0] - 1 * A[1])
# tmp2 = math.sqrt(1.0 + 1.0)
# print(f"点A到直线x-y=0的距离为：{tmp1 / tmp2:.2f}")
#
# a = 1
# b = 2
# c = 3
#
# print(not (a > b) or (b > c) and (a < c))
# print(not ((a > b) or (b > c)) and (a < c))

"""
【征兵标准】
性别要求：征收男兵
身高标准：男性160cm以上，女性158cm以上.
男性体重：男性不超过90kg，不低于60kg。
视力标准：右眼裸眼视力不低于4.6，左眼裸眼视力不低于4.5
"""

# sDataDic:sex:性别，height:身高，weight:体重，sightL:视力,sightR:右眼视力
# def Conscription_criteria(sDataDic: dict) -> bool:
#     if sDataDic['sex'] != "男":
#         print("性别要求为男，不符合要求！")
#         return False
#     if sDataDic['height'] < 160 and sDataDic['sex'] == "男":
#         print("男性身高要求160cm以上")
#         return False
#     if sDataDic["weight"] > 90 or sDataDic['weight'] < 60:
#         print("体重要求在60kg~90kg内")
#         return False
#     if sDataDic["sightL"] < 4.6 or sDataDic["sightR"] < 4.5:
#         print("要求右眼裸眼视力不低于4.6，左眼裸眼视力不低于4.5")
#         return False
#     return True
#
#
# sDataDic = {"sex": "男", "height": 0.0, "weight": 0.0, "sightL": 0.0, "sightR": 0.0}
# sDataDic["sex"] = input("请输入您的性别：")
# sDataDic["height"] = float(input("请输入您的身高："))
# sDataDic["weight"] = float(input("请输入您的体重："))
# sDataDic["sightL"] = float(input("请输入您的左眼视力："))
# sDataDic["sightR"] = float(input("请输入您的右眼视力："))
# if Conscription_criteria(sDataDic):
#     print("恭喜您符合征兵要求！")

"""
考试成绩的问题：提示用户输入成绩，判断是属于哪个水平，将结果打印到控制台。60以下不及格，
60分以上为及格，70分至80分为合格，80分至90分为良好，90分以上为优秀。
例如：请输入考试成绩：85，打印“你的成绩是良好”
"""

# def GetMarkLevel(score: int):
#     if score == 6 or score == 7:
#         print("周末")
#     elif 0 < score < 6:
#         print("工作日")
#     else:
#         print("输入数字不合法，请重新输入！")
#
#
# while True:
#     dScore = (input("请输入数字："))
#     if dScore == 'q':
#         exit()
#     else:
#         GetMarkLevel(int(dScore))

"""
设计一款足球游戏，共有左中右三个方向用于射门或者扑救动作，玩家直接输入方向射门，
电脑随机挑选方向扑救，如果方向相同，那么电脑得分，如果方向相反，那么玩家得分。
0-左路/1-右路/2-中路:
"""
import random

# c = int(input("请输入c的值"))
# d = int(input("请输入d的值"))
# print("c大于d" if c > d else "c小于d" if c < d else "c等于d")
chicken = 0
rabbit = 0
while (2 * chicken + 4 * rabbit) != 94:
    chicken += 1
    rabbit = 35 - chicken
print(f"鸡的数量为{chicken}，兔的数量为{rabbit}")


# 判断一个数是否为质数
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i) == 0:
            return False
    return True


# num = int(input("请输入一个数字："))
# print(is_prime(num))

"""
某快递公司有多个配送点，用户可自行输入，每天需要统计每个配送点的快递数量。
请编写一个程序，输入每个配送点每天的快递数量，直到输入完成。
然后，计算每个配送点的平均每天快递数量，并输出结果。
要求：

    配送点数量为正整数。
    每天的快递数量为非负整数。
"""


# 数据结构设计：一个列表存站点，每个元素是一个列表，表示站点的快递数量
# 参数为站点序号
def calculate(tag: int) -> list:
    iTotalDay, iTotalnum = 0, 0
    while True:
        num = input(f"请输入配送站点{tag + 1}的快递数量（每天）：")
        if num == "结束":
            break
        iTotalDay += 1
        iTotalnum += int(num)
    return [iTotalDay, iTotalnum]


# num1 = int(input("请输入配送点数量："))
# for i in range(num1):
#     list1 = calculate(i)
#     print(f"配送点{i+1}的平均每天快递数量为：{list1[1] / list1[0]}")

"""
编写一个程序，实现一个简单的登录系统。用户需要输入用户名和密码进行登录，
最多允许输入错误的次数为3次。如果用户名和密码都正确，则输出 "登录成功！" 并结束程序；
如果输入错误次数超过了3次，则输出 "登录失败，错误次数过多，账号已锁定"。
要求：
正确的用户名为 "admin"，正确的密码为 "password"。
编写程序实现以上需求，使用 while...else... 语句来判断用户登录是否成功，并限制最大错误次数为3次。
"""
# right_name = "admin"
# right_pas = "password"
# for i in range(3):
#     sName = input("请输入用户名：")
#     sPasWord = input("请输入密码：")
#     if sName == right_name and sPasWord == right_pas:
#         print("登陆成功！")
#         break
#     else:
#         print("用户名或密码错误")
# else:
#     print("登陆失败！")

# str1 = input("请输入标题：")
# list1 = str1.split(" ")
# print(list1)
# strresult = ""
# if str1.endswith("series"):
#     str2 = list1.pop()
#     list1.insert(0, str2)
#     strresult = list1[0] + ": "
#     for i in range(1, len(list1)):
#         strresult += list1[i]
#         strresult += " "
# print(strresult.title())

order = "iPhone, 2, 6999.99, Macbook Pro, 1, 12999.99, iPad, 3, 3299.99"
list1 = order.split(",")
total_cost = 0
print(list1)
i = 0
while i + 3 < len(list1):
    total_cost = int(list1[i + 1]) * float(list1[i + 2])
    i += 3

print(total_cost)
