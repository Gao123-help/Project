"""

编写一个 Python 模块，包含两个函数 get_circle_area(radius) 和 get_rectangle_area(length, width)，用于计算圆和矩形的面积，并在另一个 Python 脚本中导入它进行测试。
要求：

    get_circle_area(radius) 函数接受一个参数 radius（半径），返回圆的面积。
    get_rectangle_area(length, width) 函数接受两个参数 length（长度）和 width（宽度），返回矩形的面积。
    此模块的两个函数需在本模块中进行测试。


"""
import math


def get_circle_area(radius):
    return math.pi * radius ** 2


def get_rectangle_area(length, width):
    return length * width

from FileSystem import name
age = 20
print(name,age)
if __name__ == "__main__":
    print("圆的面积："+str(get_circle_area(4)))
    print("长方形面积："+str(get_rectangle_area(4, 5)))
