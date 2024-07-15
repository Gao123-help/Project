"""
1、闭包三步走
  1.1 有函数嵌套
  1.2 内层函数引用了外层函数中定义的局部变量
  1.3 外层函数将内层函数作为返回值
2、内部函数修改外层函数的局部变量，使用nonlocal关键字
"""


def fun_outer():
    b = 10
    print(b)

    def fun_inner():
        nonlocal b
        b = 20
        print(f"fun_inner-b={b}")

    fun_inner()
    print(b)
    # 将内层函数地址返回
    return fun_inner


f = fun_outer()
f()

"""
1、装饰器
  1.1 作用：给函数增加额外的功能
  1.2 不需要改变原函数的实现方式
  1.3 不需要改变函数的调用方式
  1.4 本质上是一个闭包函数
"""


# 想要给函数comment增加一个登录的功能，但是不想直接修改函数


# 将被修饰的函数地址当作参数传入装饰器
def check(fn):
    def fun_inner():
        # 实现想要增加的功能
        print("请先登录")
        # 调用被修饰的函数
        fn()

    return fun_inner


@check
def comment():
    print("请输入评论")


# 按照闭包的方式调用装饰器
# f = check(comment)
# f()

# 装饰器有专门的使用方法：@check
# 调用函数时，先执行的装饰器，走到装饰器内部调用函数的地方才是真正执行comment函数的时候
# comment()

"""
1、装饰器修饰带参数的函数，通用型，可修饰定长和不定长参数
"""


# 定义装饰器用来输出日志
def print_log(fn):
    def inner(*args, **dic):
        print(f"日志信息：函数{fn}正在执行")
        fn(*args, **dic)

    return inner


@print_log
def sum1(a, b):
    print(a + b)


sum1(10, 20)
