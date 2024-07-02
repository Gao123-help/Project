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
