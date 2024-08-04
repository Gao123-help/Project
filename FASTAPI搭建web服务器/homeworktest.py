"""
编写一个游戏类，同时可以支持多种游戏，目前支持游戏类型如下：
1，数字比大小游戏
2，扑克牌比大小游戏

游戏规则：
1，数字比大小：随机生成一个1~100的数字，让游戏者猜，再猜的过程提示比实际的数字大还是小了，猜中则胜利。注意我们需要设置猜测次数（如：10次）
2，扑克牌比大小游戏：一副扑克牌一共54张，
2.1 第一轮发牌，电脑与用户各发5张牌，
第一次电脑和用户各拿出一张牌比较大小，赢家把输家的牌吃掉（即赢家牌数量加1，输家牌数量减1）
第二次电脑和用户各拿出二张牌比较大小，比较规则为，两张牌点数相加，赢家把输家的牌吃掉（即赢家牌数量加2，输家牌数量减2）
第三次电脑和用户依然拿出剩余二张牌比较大小，比较规则为，两张牌点数相加，赢家把输家的牌吃掉（即赢家牌数量加2，输家牌数量减2）
注意：赢过来的纸牌不能作为后续比较大小的使用牌，仅作为赢过来的筹码计数使用。
2.2 第二轮发牌，电脑与用户每次发5张牌，比赛规则同上
2.3 第n轮发牌时，如果总牌数量不足10张，则用现有牌数均分给电脑和用户，直接比较均分的牌的点数大小
2.4 54张牌发完后，手上持有牌数最多的人获胜。

注意：

    纸牌可以定义一个类
    为了方便处理比较大小，我们可以用数字代替A J Q K 大小王，显示给用户是A J Q K 大小王
    里面会用到random.sample 方法，用于打乱纸牌，请同学自己查找用法

"""

import socket
import threading
import random


# def send_message(client_socket, data):
#     senddata = data.encode(encoding='utf-8')
#     client_socket.sendall(senddata)
#
#
# # 客户端
# # 1 创建套接字
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 2 绑定端口,建立连接
# client_socket.connect(('127.0.0.1', 8000))
# # 3 发送消息
# data = '你好我需要建立连接'
# send_message(client_socket,data)
# # 4、接收消息（服务器端返回的数据，默认类型是字节流类型，必须进行解码）
# recv_data = client_socket.recv(1024).decode(encoding='utf-8')
# if recv_data:
#     print(recv_data)
# else:
#     print('断开连接')
#     client_socket.close()

# 服务器端
# def handle_client_request(new_socket, ip_port):
#     # 接收客户端发来的消息
#     recv_data = new_socket.recv(1024)
#     # 判断数据是否为空
#     if recv_data:
#         recv_data = recv_data.decode('utf-8')
#         print(recv_data)
#         # 关闭新产生的套接字，相当一个请求已经处理完毕了
#         new_socket.close()
#
#
# if __name__ == '__main__':
#     # 1 创建套接字
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     # 端口复用
#     server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
#     # 2 绑定ip和端口
#     server_socket.bind(("", 8000))
#     # 3 开始监听
#     server_socket.listen()
#     # 4 等待客户端连接
#     while True:
#         new_socket, ip_port = server_socket.accept()
#         # 创建子线程
#         sub_thread = threading.Thread(target=handle_client_request, args=(new_socket, ip_port))
#         # 启动子线程
#         sub_thread.start()

# def check_role_permission(func):
#     def decorated_func(user, item):
#         role = user.role
#         # 检查用户角色是否具备访问权限
#         if role in 'admin':
#             return f'User {user.name} successfully accessed item {item}'
#         else:
#             return f'User {user.name} does not have permission to access item {item}'
#
#     return decorated_func
#
#
# @check_role_permission
# def access_item(user, item):
#     return f'User {user.name} successfully accessed item {item}'
#
#
# class User:
#     def __init__(self, name, role):
#         self.name = name
#         self.role = role
#
#
# user1 = User('John', 'admin')
# user2 = User('Alice', 'customer')
#
# print(access_item(user1, 'item001'))  # 只有具有 'admin' 角色的用户才能访问，所以成功访问
# print(access_item(user2, 'item002'))  # 'customer' 角色没有权限访问，所以返回无权限的提示
# def save_to_file(func):
#     def inner(a, b):
#         result = str(func(a, b))
#         with open('output.txt', 'w') as f:
#             f.write(result)
#
#     return inner
#
#
# @save_to_file
# def calculate_sum(a, b):
#     return a + b
#
#
# calculate_sum(1, 8)

def menu():
    print('==========游戏==========')
    print('1. 猜数字游戏')
    print('2. 猜纸牌大小游戏')
    print('3. 退出游戏系统')
    print('=======================')


def game_gussnumber():
    print('----------欢迎来玩猜数字游戏--------')
    count = 10
    # 随机生成电脑的数字
    number_comput = random.randint(1, 100)
    while count > 0:
        number = int(input('请输入你要猜的数字,数字范围[1-100]:'))
        if number > number_comput:
            print('数字大了')
        elif number < number_comput:
            print('数字小了')
        else:
            print('恭喜您猜对了!')
            break
        count -= 1
        print(f'你已经猜测{10 - count}次,剩余次数:{count}')


# 纸牌游戏
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['♣', '♦', '♥', '♠']
# 创建一副扑克牌
poker = [(rank, suit) for rank in ranks for suit in suits]

poker.append(('大王', ''))
poker.append(('小王', ''))
# 随机排列扑克牌顺序
random.shuffle(poker)


# 发牌，这里假设有两个玩家
# players = [poker[:27], poker[27:]]

# 创建玩家类,用于记录玩家手上的牌和牌的数量
# 只有发牌的时候玩家的持牌仓库增加,否则只增减数量

class player(object):
    def __init__(self, amount, pokers):
        self.amount = amount
        self.pokers = pokers

    def addpoker(self, pokers):
        self.pokers += pokers
        self.amount += len(pokers)


# 转换扑克牌的数字,将J-大王转换为对应的数字,方便后续比较
def transferpoker(element):
    if element == 'J':
        return 11
    elif element == 'Q':
        return 12
    elif element == 'K':
        return 13
    elif element == 'A':
        return 14
    elif element == '小王':
        return 15
    elif element == '大王':
        return 16
    else:
        return int(element)


# 扑克牌比较大小函数 参数为字符串类型
def comperpoker(you, computer):
    if you > computer:
        print("恭喜您本轮获胜")
        return 1
    elif you < computer:
        print("本轮电脑获胜")
        return 2
    else:
        print("本轮平局")
        return 3


# 随机生成两个不重复的数字
def generate_two_unique_numbers(a, b):
    # 初始化一个空集合
    numbers = set()
    while len(numbers) < 2:
        # 生成一个随机数
        number = random.randint(a, b)
        # 添加到集合中
        numbers.add(number)
    # 将集合转换回列表并返回
    return list(numbers)


def game_poker():
    global poker
    print('----------欢迎来玩扑克牌游戏--------')
    loopcount = 0
    player_you = player(0, [])
    player_compu = player(0, [])
    while len(poker) >= 0:
        print(f'第{loopcount + 1}轮发牌,每人五张牌')
        if len(poker) >= 10:
            pork_you = poker[loopcount*5:5 * (loopcount + 1)]
            pork_comp = poker[5 * (loopcount + 1):5 * (loopcount + 1) + 5]
            poker = poker[5 * (loopcount + 1) + 5:]
            player_you.addpoker(pork_you)
            player_compu.addpoker(pork_comp)
        else:
            num = len(poker)
            pork_you = poker[:num // 2]
            pork_comp = poker[num // 2:]
            poker.clear()
        loopcount += 1

        print(f'本轮您发到的牌为{pork_you}')
        result_you = int(input('请选择一张牌参与比较大小(输入序号):'))
        # 电脑随机出一张牌
        result_comp = random.randint(0, 4)
        number_you = transferpoker(player_you.pokers[result_you - 1][0])
        number_compu = transferpoker(player_compu.pokers[result_comp][0])
        print(f"本轮电脑出牌为:{player_compu.pokers[result_comp]}")
        # 各自卡牌数量减少1,卡牌池删除对应的牌
        del (player_you.pokers[result_you - 1])
        del (player_compu.pokers[result_comp])
        tmpnum = comperpoker(number_you, number_compu)
        if tmpnum == 1:
            player_you.amount += 1
            player_compu.amount -= 1
        elif tmpnum == 2:
            player_you.amount -= 1
            player_compu.amount += 1
        # 第二次,每人出两张牌
        print(f" 当前您的卡牌为{player_you.pokers}")
        result_you = input('请选择两张牌参与比较大小(输入序号):')
        # 每个人出完两张牌,卡牌池对应删除,卡牌数字相加,根据比较结果增加牌的数量
        print(result_you)
        result_you1 = result_you.split(' ')
        porknum_you = 0
        porknum_comp = 0
        delete_element = []
        for i in result_you1:
            porknum_you += transferpoker(player_you.pokers[int(i) - 1][0])
            delete_element.append(player_you.pokers[int(i) - 1])
        for i in delete_element:
            player_you.pokers.remove(i)
        # 电脑随机出两张牌
        numlist = generate_two_unique_numbers(0, 3)
        delete_element = []
        for i in numlist:
            porknum_comp += transferpoker(player_compu.pokers[int(i) - 1][0])
            delete_element.append(player_compu.pokers[int(i) - 1])
        for i in delete_element:
            player_compu.pokers.remove(i)
        tmpnum = comperpoker(porknum_you, porknum_comp)
        if tmpnum == 1:
            player_you.amount += 2
            player_compu.amount -= 2
        elif tmpnum == 2:
            player_you.amount -= 2
            player_compu.amount += 2
        # 最后胜两张牌直接累加并比较
        print(f" 当前您的卡牌为{player_you.pokers}")
        print("最后各自剩两张牌直接进行摊牌比较")
        porknum_you = 0
        porknum_comp = 0
        for i in player_you.pokers:
            porknum_you += transferpoker(i[0])
        for i in player_compu.pokers:
            porknum_comp += transferpoker(i[0])
        # 牌组清空
        player_you.pokers.clear()
        player_compu.pokers.clear()
        tmpnum = comperpoker(porknum_you, porknum_comp)
        if tmpnum == 1:
            player_you.amount += 2
            player_compu.amount -= 2
        elif tmpnum == 2:
            player_you.amount -= 2
            player_compu.amount += 2
    print(f'游戏结束,最终您手上的牌数量为:{player_you.amount},电脑手上牌的数量为{player_compu.amount}')



if __name__ == '__main__':
    while True:
        menu()
        game = int(input("请输入你要玩的游戏:"))
        if game == 1:
            game_gussnumber()
        elif game == 2:
            game_poker()
        else:
            break
