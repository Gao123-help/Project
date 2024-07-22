import socket

"""
1、创建套接字
2、建立连接
3、发送消息
4、接收消息
5、关闭套接字
"""
# socket.AF_INET---IPV4  socket.SOCK_STREAM--TCP协议
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client.connect(("192.168.27.1", 8000))
tcp_client.send("hello socket".encode(encoding='utf-8'))
conttent = tcp_client.recv(1024).decode(encoding='utf-8')
print(conttent)
tcp_client.close()
