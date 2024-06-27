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

fpi = math.pi
r1 = 3.0
r2 = 1.0
print(f"阴影部分面积为{fpi * (r1 ** 2 - r2 ** 2):.2f}")

# 计算点到直线的距离
A = (-1.0, 1.0)

tmp1 = abs(1 * A[0] - 1 * A[1])
tmp2 = math.sqrt(1.0 + 1.0)
print(f"点A到直线x-y=0的距离为：{tmp1 / tmp2:.2f}")

a = 1
b = 2
c = 3

print(not (a > b) or (b > c) and (a < c))
print(not ((a > b) or (b > c)) and (a < c))
