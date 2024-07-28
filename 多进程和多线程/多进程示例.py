# import time
# import multiprocessing
#
#
# def music():
#     while True:
#         print("听音乐")
#         time.sleep(0.3)
#
#
# def coding():
#     while True:
#         print("写代码")
#         time.sleep(0.3)
#
#
# if __name__ == '__main__':
#     # 创建任务
#     music_process = multiprocessing.Process(target=music)
#     coding_process = multiprocessing.Process(target=coding)
#     # 启动进程执行任务
#     music_process.start()
#     coding_process.start()
#

from multiprocessing import Process
import time

from multiprocessing import Process
import time
import threading

# 定义在进程创建之前
# def task(n):
#     for i in range(n):
#         print(i)
#         time.sleep(1)
#
#
# if __name__ == "__main__":
#     p = threading.Thread(target=task, args=(4,))
#     p.setDaemon(True)
#     p.start()
#     time.sleep(1)
#     print('主线程结束')
# 假设有一个列表 numbers，里面包含了一些整数。请编写一个程序，
# 使用多线程计算列表中每个数字的平方，并将结果存储到另一个列表 results 中，
# 要求每个数字都启动一个新线程来计算。
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = []


def func(num):
    result.append(num)


if __name__ == '__main__':
    list1 = list(range(100))
    for i in range(5):
        thread = threading.Thread(target=func, args=(list1[i*20:(i+1)*20],))
        thread.run()
    print(result)
