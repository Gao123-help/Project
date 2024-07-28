"""
假设有一个仓库，仓库的容量为10。编写一个 Python 程序来模拟生产者-消费者场景。
程序需要使用多线程的方式实现生产者向仓库中放入产品，消费者从仓库中取出产品，并输出每次操作的结果。

要求：

定义一个全局变量 warehouse 来表示仓库，初始为空列表。
定义一个全局变量 capacity 来表示仓库的容量，初始为10。
定义一个生产者函数 producer()，函数内部实现将产品放入仓库的逻辑。
定义一个消费者函数 consumer()，函数内部实现从仓库中取出产品的逻辑。
使用多线程的方式同时启动多个生产者和消费者线程，并模拟生产者向仓库放入产品，消费者从仓库取出产品的过程。
每次成功放入产品或取出产品后，输出当前操作的结果。

# start_producer(3)  # 启动3个生产者线程
# start_consumer(2)  # 启动2个消费者线程
#
# 如下是运行过程中的打印
# Producer 1: Produced product 1
# Producer 2: Produced product 2
# Producer 1: Produced product 3
# Consumer 1: Consumed product 1
# Consumer 2: Consumed product 2
# Producer 2: Produced product 4
# Producer 3: Produced product 5
# Consumer 1: Consumed product 3
# Producer 1: Produced product 6
# Consumer 2: Consumed product 4
"""
import threading
import time

# warehouse = []  # 仓库
# capacity = 10  # 仓库容量

# def producer(num):
#     global capacity
#     warehouse.append(num)
#     capacity += 1
#
#
# def consumer(num):
#     global capacity
#     warehouse.remove(num)
#     capacity -= 1
#
#
# def start_producer(n):
#     # 启动n个生产者线程
#     for i in range(n):
#         producer_thread = threading.Thread(target=producer, args=(i,))
#         producer_thread.start()
#         time.sleep(1)
#         print(f'Producer{i + 1}:Producered Product {i}')
#
#
# def start_consumer(n):
#     # 启动n个生产者线程
#     for i in range(n):
#         consumer_thread = threading.Thread(target=consumer, args=(i,))
#         consumer_thread.start()
#         time.sleep(1)
#         print(f'consumer{i + 1}:consumer Product {i}')
#
#
# if __name__ == '__main__':
#     start_producer(3)
#     start_consumer(2)

"""
假设您正在开发一个在线聊天程序，需要实现一个多线程的服务器和一个简单的客户端。请编写服务器端和客户端的代码。

提示：

服务器端工作原理：

    服务器端通过 socket 模块创建一个 TCP 套接字，绑定在本地的 8000 端口，并开始监听客户端连接。
    当有客户端连接时，服务器接受连接并为每个客户端创建一个独立的线程来处理连接和消息。
    在每个客户端线程中，服务器不断接收客户端发送的消息，并输出到控制台。
    当客户端关闭连接时，线程退出，连接关闭。

客户端工作原理：

    客户端通过 socket 模块创建一个 TCP 套接字，连接到服务器的 localhost 地址和 8000 端口。
    客户端调用 send_message() 函数，并传入要发送的消息作为参数。
    send_message() 函数将消息字符串编码为字节串，并使用 sendall() 函数发送给服务器。
    发送完成后，客户端关闭套接字。
"""
# import socket
#
#
# def receiveandsend(server):
#     client_socket, client_ip = server.recv(1024)
#     data = client_socket.recv(1024)
#     print("收到的数据：" + data.decode())
#     response = "已收到数据"
#     client_socket.send(response.encode(encoding='utf-8'))
#     client_socket.close()
#
#
# # server端
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind("", 8000)
# server.listen()
# # while True:
# #     process1 = threading.Thread(target=receiveandsend, args=(server,))
#
# # client 端
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect("127.0.0.1", 8000)
# data = "你好".encode(encoding='utf-8')
# client.send(data)
# recv_data = client.recv(1034).decode(encoding='utf-8')
# print(recv_data)
# client.close()

import copy

# 原始列表
original_list = [1, 2, [3, 4], 5]

# 浅拷贝
shallow_copy = copy.copy(original_list)

# 修改浅拷贝中的嵌套列表
shallow_copy[2][0] = 'A'

# 深拷贝
deep_copy = copy.deepcopy(original_list)

# 修改深拷贝中的嵌套列表
deep_copy[2][1] = 'B'

# 输出结果
print("原始列表:", original_list)
print("浅拷贝:", shallow_copy)
print("深拷贝:", deep_copy)
