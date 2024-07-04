# 斐波那契数列
dic = {}


def func(num: int):
    if num == 1 or num == 2:
        return 1
    dic[num] = func(num - 1) + func(num - 2)
    return dic[num]


print(func(15))
print(dic)

# lambda 表达式
# 变量= lambda 参数: 表达式(函数体 return ***)
# 带有三目运算符的lambda表达式
# func1 = lambda a, b: a if a == b else b
# print(func1(3, 4))
# # 字典排序
# list1 = [
#     {"name": "小明", "age": 20, "male": "男"},
#     {"name": "大明", "age": 20, "male": "男"},
#     {"name": "二明", "age": 20, "male": "男"},
# ]
# # list1.sort(key=lambda x: x["name"])
# print(list1)

f = open("pyfile", 'a')
f.write("abcdefghijklmn")
f.close()

f = open("pyfile", 'rb')
f.seek(5)
# 可以理解为总是获取光标右边的值
conten = f.read(1)
print(conten)
