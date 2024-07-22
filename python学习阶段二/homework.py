"""
假设你是一名网站开发者，你需要设计一个函数 login_counter()，用于统计用户登录的次数和最近一次登录的时间。

要求：

    login_counter() 返回一个闭包 login()。
    每次调用 login()，它将累加用户登录的次数，并记录最近一次登录的时间。
    需要返回一个字典，包含累计的登录次数（total_count）和最近一次登录的时间（last_login_time）。

设计思路：

    在 login_counter() 函数外部定义一个变量 count，用于记录累计的登录次数。
    在 login_counter() 函数内部定义一个变量 last_login，用于记录最近一次登录的时间戳。
    在 login() 函数内部更新 count 和 last_login 的值，并返回字典形式的结果。


"""
import time


# count = 0  # 登录次数
#
#
# def login_counter():
#     last_login = 0
#
#     def login():
#         nonlocal last_login
#         global count
#         last_login = time.ctime()
#         count += 1
#         return {last_login: count}
#
#     return login


# f = login_counter()
# f()
# f()
# print(f())

# def discount_calculator(discount_rate):
#     def calculate_discounted_price(price):
#         return price * discount_rate / 100
#
#     return calculate_discounted_price
#
#
# # 创建折扣计算器
# f90 = discount_calculator(90)
# f80 = discount_calculator(80)
#
# # 使用折扣计算器进行计算
# price1 = 100
# price2 = 50
#
# discounted_price1 = f90(price1)
# discounted_price2 = f80(price2)
#
# print("打九折后的价格：", discounted_price1)
# print("打八折后的价格：", discounted_price2)

# def calculator_factory(operation):
#     if operation == "+":
#         def add(a, b):
#             return a + b
#
#         return add
#
#     elif operation == "-":
#         def subtract(a, b):
#             return a - b
#
#         return subtract
#
#     elif operation == "*":
#         def multiply(a, b):
#             return a * b
#
#         return multiply
#
#     elif operation == "/":
#         def divide(a, b):
#             try:
#                 result = a / b
#                 return result
#             except Exception as e:
#                 print(e)
#
#         return divide
#
#
# # 创建加法计算器
# add_calculator = calculator_factory("+")
# result1 = add_calculator(5, 3)
# print("加法计算结果：", result1)
#
# # 创建减法计算器
# subtract_calculator = calculator_factory("-")
# result2 = subtract_calculator(8, 4)
# print("减法计算结果：", result2)
#
# # 创建乘法计算器
# multiply_calculator = calculator_factory("*")
# result3 = multiply_calculator(6, 2)
# print("乘法计算结果：", result3)
#
# # 创建除法计算器
# divide_calculator = calculator_factory("/")
# result4 = divide_calculator(10, 0)
# print("除法计算结果：", result4)

# 请实现一个装饰器，把如下函数func的返回值结果+100后再返回。

def add(fn):
    def inner(*args, **dic):
        return fn(*args, **dic) + 100

    return inner


# 请实现一个装饰器，每次调用函数时，将函数名字及调用函数的时间点写入文件中。
# def writetofile(fn):
#     log_time = None
#
#     def inner(*args, **dic):
#         nonlocal log_time
#         file = open('functime.txt', 'w', encoding='utf-8')
#         log_time = time.ctime()
#
#         file.write(f"函数名称：{fn}，调用时间：{log_time}")
#         file.close()
#         return fn(*args, **dic)
#
#     return inner
#
#
# @writetofile
# def func(number):
#     return int(number)
#
#
# print(func(10))

"""
根据如下说明，编写代码完成相关需求
1、
不带装饰器的基础功能：entry_grade
可以完成『成绩录入功能』
1.1可以重复录入成绩，默认所有输入都是合法的(1~100之间的数)
1.2当录入成绩为0时，结束成绩的录入
1.3将录入的成绩保存在列表中并返回给外界，例如：[90, 80, 50, 70]

2、
选择课程装饰器：choose_course
为『成绩录入功能』新增选择课程的拓展功能，达到可以录入不同学科的成绩
2.1可以重复输入要录入的学科名，然后就可以进入该门学科的『成绩录入功能』，录入结束后，可以进入下一门学科成绩录入
2.2当输入学科名为q时，结束所有录入工作
2.3将学科成绩保存在字典中并返回给外界，例如：{'math': [90, 80, 50, 70], 'english': [70, 50, 55, 90]}

3、
处理成绩装饰器：deal_fail
可以将所有录入的成绩按60分为分水岭，转换为 "通过" | "不通过"进行存储
3.1，如果只对原功能装饰，结果还为list返回给外界，例如：["通过", "通过", "不通过", "通过"]
3.2，如果对已被选择课程装饰器装饰了的原功能再装饰，结果就为dict返回给外界，
例如：{'math': ["通过", "通过", "不通过", "通过"],'english': ["通过", "不通过", "不通过", "通过"]}

"""


def choose_course(fn):
    course_scores = {}

    def inner(*args, **dic):
        nonlocal course_scores
        while True:
            course = input("请输入课程名称：")
            if course == "q":
                break
            course_scores[course] = fn(*args, **dic)
        print(course_scores)
        return course_scores

    return inner


def deal_fail(fn):
    dic1 = {}

    def inner(*args, **dic):
        nonlocal dic1
        dic1 = fn(*args, **dic)
        print(dic1)
        for i in dic1.keys():
            for j in range(len(dic1[i])):
                if dic1[i][j] >= 60:
                    dic1[i][j] = '通过'
                else:
                    dic1[i][j] = '不通过'
        print(dic1)
        return dic1

    return inner


# 先定义函数实现成绩录入、处理成绩
@deal_fail
@choose_course
def entry_grade():
    grades = []
    while True:
        grade = int(input("请输入成绩："))
        if grade == 0:
            break
        grades.append(grade)
    return grades


# 再定义装饰器分别为成绩录入和处理成绩添加功能
entry_grade()
