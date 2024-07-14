# 文件操作
"""
请编写一个程序，实现从文本文件中读取数据，并进行简单的处理和输出。

    首先，程序需要从文本文件中读取一串数字，每个数字占据一行。文本文件的名称为 numbers.txt。
    然后，程序需要将读取到的数字进行累加求和，并输出求和结果。

注意：

    文本文件中的每行只包含一个整数。
    文件中的数字可能有正数、负数或零。

"""
# f = open("numbers.txt", 'r')
# content = f.readlines()
# newcontent = [i.rstrip('\n') for i in content]
# print(newcontent)
# sum = 0
# while True:
#     content = f.readline()
#     content.rstrip('\n')
#     print(content)
#     if content == "":
#         break
#     sum += int(content)
# print(sum)
# f.close()
# 定义字典存储每个单词出现的次数
# dic = {}
# fin = open("output.txt", 'r')
# fout = open("result.txt", 'w')
# content = fin.read()
# wordlist = content.split(' ')
# for i in wordlist:
#     if i in dic.keys():
#         dic[i] += 1
#     else:
#         dic[i] = 1
# for key in dic.keys():
#     fout.write(key + ':' + str(dic[key]) + '\t\n')
# fin.close()
# fout.close()

# fin = open("output.txt", 'r')
# fout = open("result.txt", 'w')
# content = fin.readlines()
# newcontent = [int(i.rstrip('\n')) for i in content]
# print(newcontent)
# average = sum(newcontent)/len(newcontent)
# fout.write(str(average))

# 异常处理
# try:
#     f = open("python.txt", 'r')
#     while True:
#
#         content = f.readline()
#         if content == '':
#             break
#         print(content)
#     f.close()
# except Exception:
#     f = open("python.txt", 'w', encoding='utf-8')
#     f.write("开启文件失败，执行except中的代码!")
#     f.close()

"""
请编写一个程序，接受用户输入一个整数，并进行相应的处理。

    首先，程序需要提示用户输入一个整数。
    然后，程序尝试将用户输入的内容转换为整数类型，并计算它的平方。
    如果用户输入的内容无法转换为整数类型，程序将捕获异常，并输出错误信息："输入无效，请输入一个有效的整数！"。
    否则，在else逻辑块中将程序输出计算得到的平方结果。


"""


# import math
#
# number = 10
# number1 = math.pow(number,2)
# number3 = math.log(number)
# number4 = math.sin(number)
# number5 = math.cos(number)
# pi = math.pi
# print(str(pi))

# from MyMod import *
#
# print("圆的面积："+str(get_circle_area(4)))
# print("长方形面积："+str(get_rectangle_area(4, 5)))
class Student(object):
    def __init__(self, id, name, scores):
        self.id = id
        self.name = name
        self.scores = scores

    def __str__(self):
        print(f"学号：{self.id},姓名：{self.name},年龄：{self.age}")

    def __del__(self):
        print(f"学生{self.name}被删除！")


# class Rectangle(object):
#     def __init__(self, wides, height):
#         self.wides = wides
#         self.height = height
#
#     def calculate_area(self):
#         return self.wides * self.height


class Product(object):
    def __init__(self, product_id, name, stock):
        self.product_id = product_id
        self.name = name
        self.stock = stock

    def reduce_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            print(f"商品库存减少{quantity}件")
            return True
        else:
            print("商品库存不足")
            return False


products = [
    Product(1, "手机", 10),
    Product(2, "电视", 5),
    Product(3, "耳机", 20)
]


# for i in products:
#     if i.product_id == 1:
#         i.reduce_stock(5)

class Employee(object):
    def __init__(self, employee_id, name, age):
        self.employee_id = employee_id
        self.name = name
        self.age = age

    def get_employee_id(self):
        return self.employee_id


person = Employee(20210801, "张三", 25)
person.get_employee_id()

"""
假设我们正在创建一个银行账户管理系统，设计一个银行账户类（BankAccount），具有以下功能：

    每个人都有：账号号码（account_number）和账户余额（balance），因为账户号码和账户余额都是隐身信息，所以只有账户持有人才有查看权限。
    每个账户都可用于验证用户输入的PIN码是否正确validate_pin(self, pin)，因为对密码安全性保护较高，只有账户持有人才有输入密码，尝试密码是否正确的权限。
    每个账户都可以被存款deposit(amount)
    每个账户都可以被取款，即从账户中取款指定金额，取款时需要输入PIN码进行验证withdraw(amount, pin)
        余额充足，则可以取款
        余额不足，则提示余额不足
        密码错误，则提示Pin错误

在主程序中，创建一个银行账户对象，并调用公有方法进行存款和取款操作。

要求：

    存款操作：直接将指定金额加到账户余额中
    取款操作：先调用方法验证PIN码，若验证通过则将指定金额从账户余额中减去；若验证不通过则输出错误提示信息

参考如下方式创建账户对象
account = BankAccount("123456789", 1000)

"""


class BankAccount(object):
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self._balance = balance

    def _getAccountNum(self):
        return self._account_number

    def _getBalance(self):
        return self._balance

    def setBalance(self, balance):
        self._balance = balance

    def validate_pin(self, pin):
        if pin == 'PIN':
            print("密码验证通过")
            return True
        else:
            print("密码验证失败")
            return False

    # 存款
    def deposit(self, amount):
        balance1 = self._getBalance()
        balance1 += amount
        self.setBalance(balance1)
        print("存款成功！")
        print(f"当前账户余额：{self._getBalance()}")

    # 取款
    def withdraw(self, amount, pin):
        # 密码验证通过
        if self.validate_pin(pin):
            balance = self._getBalance()
            balance -= amount
            if balance < 0:
                print("余额不足")
            else:
                print("余额充足可以取款")
                self.setBalance(balance)
                print(f"当前账户余额：{self._getBalance()}")


account = BankAccount("123456789", 1000)
account.deposit(1000)
account.withdraw(3000, 'PIN')

"""
假设我们要设计一个图形计算器，其中包含两种图形：矩形和圆形。请基于面向对象的思想，设计相应的类，并编写计算面积和周长的方法。

要求：

    矩形类（Rectangle）具有属性：长（length）和宽（width），以及计算面积和周长的方法。
    圆形类（Circle）具有属性：半径（radius），以及计算面积和周长的方法。
    两个类都具有构造方法和字符串表示方法（str()），用于打印图形的属性。
    使用继承关系，确保代码的复用性。
    在主程序中，创建一个矩形对象和一个圆形对象，并调用相应的方法打印其面积和周长
"""

import math


class Graphic(object):
    # def coculate_area(self,):
    def __str__(self):
        return f"面积为：{self.area},周长为{self.length}"


class Rectangle(Graphic):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = 0
        self.length = 2 * (width + height)

    def coculate_area(self, width, height):
        self.area = width * height


class Circle(Graphic):
    def __init__(self, redious):
        self.redious = redious
        self.area = 0
        self.length = 2 * math.pi * redious

    def coculate_area(self, redious):
        self.area = math.pi * redious ** 2


rectangle = Rectangle(4, 5)
rectangle.coculate_area(4, 5)
circle = Circle(4)
circle.coculate_area(4)
print(rectangle)
print(circle)

"""
假设我们正在开发一个电商平台，需要设计一个父类（Product）用于表示商品信息，同时还需要设计两个子类（Book、Clothing）分别表示图书和服装商品。要求使用面向对象的思想和多态的方式，设计并实现这三个类。

要求：

    父类（Product）具有以下属性和方法：
        属性：名称（name）、价格（price）
        方法：获取商品名称（get_name()）、获取商品价格（get_price()）
    子类（Book、Clothing）继承自父类，并分别具有以下特有的属性和方法：
        Book类特有属性：作者（author）、出版社（publisher）
        Clothing类特有属性：尺码（size）、颜色（color）
    假设电商平台上有一本书名为《Python入门教程》（name = "Python入门教程"），价格为50元，作者为"张三"，出版社为"A出版社"；还有一件衣服名为"时尚T恤"（name = "时尚T恤"），价格为100元，尺码为"M"，颜色为"红色"。请设计并实现上述类，并编写主程序输出以下信息：
        《Python入门教程》的名称、价格、作者和出版社；
        "时尚T恤"的名称、价格、尺码和颜色。

参考如下方式创建实例
python_book = Book("Python入门教程", 50, "张三", "A出版社")
fashion_clothing = Clothing("时尚T恤", 100, "M", "红色")

"""

# class Product(object):
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def get_name(self):
#         return self.name
#
#     def get_price(self):
#         return self.price
#
#
# class Book(Product):
#     def __init__(self, name, price, author, publisher):
#         super().__init__(name, price)
#         self.author = author
#         self.publisher = publisher
#
#     def __str__(self):
#         return f"name:{self.name},price:{self.price},author{self.author},publisher{self.publisher}"
#
#
# class Clothing(Product):
#     def __init__(self, name, price, size, color):
#         super().__init__(name, price)
#         self.size = size
#         self.color = color
#
#     def __str__(self):
#         return f"name:{self.name},price:{self.price},size{self.size},color{self.color}"
#
#
# class DateUtils(object):
#     @staticmethod
#     def is_leap_year(year):
#         if year % 4 == 0:
#             return True
#         else:
#             return False
#
#
# li = [1, 2, 3, 4, 6, 7, 8, 10, 12]
# index = 0
# lg = len(li)
#
# for i in li:
#     if i % 2 == 0:
#         li.remove(i)
#
# print(li)


"""
请同学实现一个可以递归删除指定目录下面的固定格式的文件的程序：
示例： remove（myproject，'pyc'） , 表示删除myproject目录中的所有以pyc文件结尾的文件
"""
import os
import shutil

# def remove_files(directory, extension):
#     for filename in os.listdir(directory):
#         file_path = os.path.join(directory, filename)
#         if os.path.isfile(file_path) and file_path.endswith(extension):
#             os.remove(file_path)
#         elif os.path.isdir(file_path):
#             remove_files(file_path, extension)


# 使用示例
# directory_to_clean = 'myproject'
# file_extension = 'pyc'
# remove_files(directory_to_clean, file_extension)

"""
在电商业务场景中，需要设计商品类、购物车类和用户类。具体描述如下：

    商品类（Product）：每个商品对象应具有以下属性和方法：
        属性：名称（name）、价格（price）、库存数量（stock）
        方法：获取商品名称（get_name()）、获取商品价格（get_price()）、获取商品库存数量（get_stock()）、更新商品库存数量（update_stock(quantity)）
    普通商品类（RegularProduct）：继承自商品类，每个普通商品对象应具有以下特有的方法：
        方法：购买商品（buy_product(quantity)）：根据购买的数量减少商品库存量；如果库存不足，则输出"库存不足，无法购买该商品"；否则，减少库存数量。
        方法：添加到购物车（add_to_cart(cart, quantity)）：将商品添加到指定购物车对象中，同时指定购买的数量。
    折扣商品类（DiscountProduct）：继承自商品类，每个折扣商品对象应具有以下特有的属性和方法：
        属性：折扣（discount）
        方法：购买商品（buy_product(quantity)）：根据购买的数量减少商品库存量；如果库存不足，则输出"库存不足，无法购买该商品"；否则，减少库存数量。
        方法：添加到购物车（add_to_cart(cart, quantity)）：将商品添加到指定购物车对象中，同时指定购买的数量。
    购物车类（Cart）：每个购物车对象应具有以下属性和方法：
        属性：商品项（items）,提示：考虑用字典进行存储
        方法：添加商品（add_item(product, quantity)）：将指定数量的商品添加到购物车中；如果商品已存在于购物车，则增加该商品的数量；否则，添加新的商品项。
        方法：删除商品（remove_item(product, quantity)）：从购物车中删除指定数量的商品；如果商品数量不足以删除，则直接删除该商品项；否则，减少商品数量。
        方法：查看购物车内容（view_items()）：输出购物车中的商品项及其对应的数量。
        方法：清空购物车（clear()）：将购物车中的商品项清空。
    用户类（User）：每个用户对象应具有以下属性和方法：
        属性：用户名（name）、购物车（cart）
        方法：添加商品到购物车（add_to_cart(product, quantity)）：将指定数量的商品添加到用户的购物车中。
        方法：查看购物车内容（view_cart()）：输出用户购物车中的商品项及其对应的数量。
        方法：结算订单并支付（checkout()）：根据购物车中的商品项生成订单对象，并进行支付；支付成功后，清空购物车。
    订单类（Order）：每个订单对象应具有以下属性和方法：
        属性：购物车（cart）、总价（total_price）
        方法：计算总价（calculate_total_price()）：根据购物车中的商品项计算订单的总价。
        方法：支付（pay()）：执行支付逻辑，输出支付成功信息，并显示支付金额。

请使用面向对象的思想，设计并实现这些类，并编写主程序测试上述功能。请确保代码的正确性和健壮性，并合理处理各类之间的关系。

提示：在如下代码的基础上完善后续逻辑，需补充代码的部分都写了TODO。

"""


class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_stock(self):
        return self.stock

    def update_stock(self, quantity):
        self.stock = quantity


class RegularProduct(Product):
    def __init__(self, name, price, stock):
        super().__init__(name, price, stock)

    def buy_product(self, quantity):
        if self.stock < quantity:
            print("库存不足，无法购买该商品")
        else:
            self.stock -= quantity

    def add_to_cart(self, cart, quantity):
        cart.add_item(self, quantity)


class DiscountProduct(Product):
    def __init__(self, name, price, stock, discount):
        super().__init__(name, price, stock)
        self.discount = discount
        #

    def buy_product(self, quantity):
        if self.stock < quantity:
            print("库存不足，无法购买该商品")
        else:
            self.stock -= quantity

    def add_to_cart(self, cart, quantity):
        cart.add_item(self, quantity)


class User:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()

    def add_to_cart(self, product, quantity):
        self.cart.add_item(product, quantity)

    def view_cart(self):
        self.cart.view_items()

    def checkout(self):
        order = Order(self.cart)

        # 进行支付
        order.pay()


class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    # TODO

    def remove_item(self, product, quantity):
        if product in self.items:
            if self.items[product] <= quantity:
                print("库存不足")
            else:
                self.items[product] -= quantity
        else:
            print("该商品不存在")

    def view_items(self):
        for product, quantity in self.items.items():
            print(f"{product.get_name()} - 数量：{quantity}")

    def clear(self):
        self.items.clear()


class Order:
    def __init__(self, cart):
        self.cart = cart
        self.total_price = self.calculate_total_price()

    def calculate_total_price(self):
        total_price = 0
        for i in self.cart.items.keys():
            if isinstance(i, RegularProduct):
                total_price += self.cart.items[i] * i.price
            else:
                total_price += self.cart.items[i] * i.price * i.discount

        return total_price

    def pay(self):
        # 实现支付逻辑
        # 先计算总金额，支付总金额并清空购物车
        self.calculate_total_price()
        self.cart.clear()
        print(f"支付成功！支付金额：{self.total_price}")


# 创建普通商品对象和折扣商品对象
regular_product = RegularProduct("iPhone 12", 6999, 100)
discount_product = DiscountProduct("Apple Watch", 1999, 50, 0.8)

# 创建用户对象
user = User("John")

# 用户添加商品到购物车，并查看购物车
user.add_to_cart(regular_product, 2)
user.add_to_cart(discount_product, 3)
user.view_cart()

# 用户结算订单并支付
user.checkout()
