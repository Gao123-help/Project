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

# order = "iPhone, 2, 6999.99, Macbook Pro, 1, 12999.99, iPad, 3, 3299.99"
# list1 = order.split(",")
# total_cost = 0
# print(list1)
# i = 0
# while i + 3 < len(list1):
#     total_cost = int(list1[i + 1]) * float(list1[i + 2])
#     i += 3
#
# print(total_cost)

# python变量的引用关系
# 不可变数据类型：数字、字符串、元组；可变：列表、字典
# a = " abcdefg"
# print(f"地址a：{id(a)}")
#
# print(f"地址a：{id(a)}")
# a = [1, 11, 3, 4]
# b = a
# b[1] = 12
# print(f"地址a：{id(a)},a:{a}")


"""

 已知有一个购物车商品列表 cart = [("Apple", 2), ("Banana", 3), ("Orange", 4), ("Pear", 1)]，其中每个元组表示一种商品及其数量。请使用列表推导式编写代码，实现以下功能：

    创建一个新列表 cart_items，其中仅包含购物车中的商品名称（即去除商品数量信息）。
    创建一个新列表 expensive_items，其中仅包含购物车商品数量>=3的商品名称。
    将购物车中每个商品的数量加倍，并创建一个新的购物车列表 cart_doubled。

请编写上述要求的代码，并输出最终的列表 cart_items、expensive_items 和 cart_doubled。

"""

# cart = [("Apple", 2), ("Banana", 3), ("Orange", 4), ("Pear", 1)]
# cart_items = [i[0] for i in cart]
# expensive_items = [i[1] for i in cart if i[1] >= 3]
# print(f"cart_items:{cart_items}")
# print(f"expensive_items:{expensive_items}")
#
# li = [1, 2, 4, None, 5, None]
# li1 = [i for i in li if i != None]
# new_li = [num for num in li if str(num).isdigit()]
# print(li1)

#
# def findall(s, sun_str: str):
#     result_list = []
#     len1 = len(sun_str)
#     for i in range(len(s)):
#         if s[i:i + len1] == sun_str:
#             result_list.append(i)
#     return tuple(result_list)
#
#
# s = findall("helloworldhellopythonhelloc++hellojava", "hello")
# print(s)

global_var = 100

"""
请编写一个函数 print_info，接受以下参数：
    name：表示一个人的姓名（必须）
    age：表示一个人的年龄（必须）
    city：表示一个人所在的城市（可选，默认值为 "未知"）
    gender：表示一个人的性别（可选，默认值为 "未知"）
    函数内部根据提供的参数打印人物信息，输出格式如下：
    姓名：xxx
    年龄：xxx
    城市：xxx
    性别：xxx
可变长参数
"""

# def print_info(**vardict):
#     for i in vardict.items():
#         print("姓名:" if i[0] == 'name' else "年龄:" if i[0] == "age" else "城市:" if i[0] == "city" else "性别:")
#
#
# print_info(name="xiaoming", age=17, city="hangzhou", gender="male")

"""
假设你正在开发一个餐厅点餐系统，需要编写 Python 代码来处理订单信息和菜品库存。请完成以下要求：

    创建一个函数place_order(table_number, *dishes, serving_time=None, **requirements)，用于记录订单信息和处理菜品库存。
        参数 table_number 是位置参数，表示桌号。
        参数 dishes 是不定长参数，表示顾客所点的菜品列表。
        参数 serving_time 是关键字参数，表示就餐时间，默认为 None。
        参数 requirements 是关键字参数，表示顾客对菜品的特殊要求。
    在函数内部，根据菜品的库存数量和要求，判断是否能够满足顾客的点餐需求。
    如果库存充足且满足要求，打印订单信息，并将对应菜品的库存数量减少；如果库存不足或不能满足要求，打印相应提示信息。
    在主程序中，调用函数 place_order() 并传入相应的参数值，模拟一次实际点餐操作，并观察输出结果。

请编写上述要求的代码，并输出订单信息。

模拟菜品库存如下

menu = {
    '鱼香肉丝': 5,
    '宫保鸡丁': 3,
    '糖醋排骨': 0,
    '回锅肉': 4,
    '水煮鱼': 2
}

传递参数方式如下：

place_order(10, '鱼香肉丝', '宫保鸡丁', '糖醋排骨', '回锅肉', '水煮鱼', serving_time='19:00', 鱼香肉丝='少辣', 回锅肉='加蒜')

最终呈现结果为：

# 桌号：10
# 所点菜品：
#   - 鱼香肉丝
#     - 特殊要求：少辣
#   - 宫保鸡丁
#   - 糖醋排骨 点餐失败，该菜品不存在或库存不足
#   - 回锅肉
#     - 特殊要求：加蒜
#   - 水煮鱼
# 就餐时间：19:00

# 提示：
def demo(**requirements):
    if '鱼香肉丝' in requirements:
        print(requirements['鱼香肉丝'])
demo(鱼香肉丝='少辣')
"""
menu = {
    '鱼香肉丝': 5,
    '宫保鸡丁': 3,
    '糖醋排骨': 0,
    '回锅肉': 4,
    '水煮鱼': 2
}


def print_menu():
    print(f'鱼香肉丝:{5}')
    print(f'宫保鸡丁:{3}')
    print(f'宫保鸡丁:{0}')
    print(f'回锅肉:{4}')
    print(f'水煮鱼:{2}')


# # 判断菜品是否在菜单中，若在，库存减少1
# def existmenu(dishes: tuple, requirements: dict):
#     count = 0
#     for i in dishes:
#         # 若在菜单中，且有库存则数量减一
#         if i in menu.keys() and menu[i] > 0:
#             menu[i] -= 1
#         else:
#             count += 1
#             requirements[i] = "点菜失败，该菜品库存不足或不存在"
#     if count == len(dishes):
#         print("所有菜品都已售罄！")
#         return False
#     return True
#
#
# # 打印每个菜品的拼接信息，菜品名称和对应的特殊性要求
# def print_perfood(dishes: tuple, requirements: dict):
#     for i in dishes:
#         print(f"  -{i}")
#         if i in requirements.keys():
#             print(f"   -{requirements[i]}")
#
#
# def place_order(table_number, *dishes, serving_time=None, **requirements):
#     print("---------欢迎点菜--------")
#     if existmenu(dishes,requirements):  # 点菜成功
#         print(f"桌号：{table_number}")
#         print("所有菜品：")
#         print_perfood(dishes, requirements)
#         print(f"就餐时间：{serving_time}")
#
#
# place_order(10, '鱼香肉丝', '宫保鸡丁', '糖醋排骨', '回锅肉', '水煮鱼', serving_time='19:00', 鱼香肉丝='少辣',
#             回锅肉='加蒜')

"""
请编写两个函数，实现以下功能：

    第一个函数名为 calculate_rectangle_area，接受两个参数 length 和 width，分别为矩形的长度和宽度。
        函数内部计算并返回矩形的面积。
    第二个函数名为 calculate_composite_area，接受两个参数 a 和 b，分别为两个矩形的长度和宽度。
        函数内部调用 calculate_rectangle_area 函数，计算两个矩形的面积之和，并返回结果。
    调用函数 calculate_composite_area，将矩形1的长度为 3，宽度为 4，矩形2的长度为 5，宽度为 6，作为参数传入，并输出结果。


"""

# def calculate_rectangle_area(length, width: float):
#     return length * width
#
#
# def calculate_composite_area(a, b: tuple):
#     sum1 = 0
#     for i in range(len(a)):
#         sum1 += calculate_rectangle_area(a[i], b[i])
#     print(sum1)
#
#
# calculate_composite_area((3, 5), (4, 6))

"""
请编写一个程序，定义一个元组 student，包含学生的信息，包括姓名、年龄和性别。
然后，使用元组拆包的方式将学生的信息提取出来，并分别存储到对应的变量中。最后，分别输出学生的姓名、年龄和性别。
"""
# student = ("小明", 20, "男")
# name, age, gender = student
# print(f"姓名：{name}")
# print(f"年龄：{age}")
# print(f"性别：{gender}")
"""
你正在开发一个图书管理系统，需要编写 Python 代码来处理图书信息。

已知有一个图书列表 books，记录图书编号(book_id)和书名(book_name)，一个作者列表，记录作者名称(author)和图书编号(book_id)。
请使用函数嵌套调用的方式编写代码，实现以下功能：

    创建一个函数 search_book_by_author(authors, author)，根据作者名称获取其编写的所有图书名
    创建一个函数 get_book_info(books, book_id)，根据图书编号获取图书的名称。
    在 search_book_by_author(authors, author) 函数内部，通过调用 get_book_info(books, book_id) 函数来获取每本图书的图书名。
    在主程序中调用 search_book_by_author(authors, author) 函数，并输出符合要求的图书名称。

请编写上述要求的代码，并输出符合要求的图书名称。
"""

# authors = [
#     {
#         "book_id": 1,
#         "author": "张三"
#     },
#     {
#         "book_id": 2,
#         "author": "李四"
#     },
#     {
#         "book_id": 3,
#         "author": "张三"
#     },
#     {
#         "book_id": 4,
#         "author": "王五"
#     },
#
# ]
# books = [
#     {
#         "book_id": 1,
#         "book_name": "Python编程入门",
#     },
#     {
#         "book_id": 2,
#         "book_name": "Java从入门到精通",
#     },
#     {
#         "book_id": 3,
#         "book_name": "数据结构与算法",
#     },
#     {
#         "book_id": 4,
#         "book_name": "深入理解计算机系统",
#     }
# ]
#
#
# def search_book_by_author(authors: list, author):  # ，根据作者名称获取其编写的所有图书名
#     for i in authors:
#         if i["author"] == author:
#             print(get_book_info(books, i["book_id"]))
#
#
# def get_book_info(books: list, book_id):
#     for i in books:
#         if i["book_id"] == book_id:
#             return i["book_name"]
#
#
# search_book_by_author(authors, "张三")

# def sum_digits(n):
#     if n % 10 == n:
#         return n
#     return sum_digits(int(n / 10)) + (n % 10)
#
#
# print(sum_digits(12345))
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# num1 = list(filter(lambda a: a % 2 != 0, num))
# print(num1)

func = lambda s: s.upper()
print(func("hello py"))

num = ["xiaoming", "zhangsan", "lala", "orange"]
print(sorted(num, key=lambda i: len(i)))

is_even = lambda i: i % 2 == 0
print(is_even(17))
