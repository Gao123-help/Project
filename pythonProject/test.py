print("hello world!")
# 你好
"""

"""
"""
格式化输出
"""
# name = "小王"
# age = 30
# print("他的名字叫%s,今年%d岁" % (name, age))
#
# # format格式化
# print(f"姓名:{name},年龄:{age}")
# print("%.2f" % 12.111)
#
# tmp = "30"
# print("%d" % int(tmp))

sTmp = "[1,2,3]"
print(type(eval(sTmp)))

print(f"{9 / 2}")
# 短路运算
print(3 and 4)
# 三目运算符
a = 10 if 10 > 20 else 20
# 字符串拼接
slist = {"python", "linux", "C++"}
print("-".join(slist))
# 首字母大写：str.title()
# 字符串的判断语句：startwith()\endwith()
"""
del和pop的区别：pop会返回被删除的元素值，pop默认删除最后一个元素
"""
name_list =["小明","小王","小明"]
del name_list[0]
print(name_list)

