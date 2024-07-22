import time
import multiprocessing


def music():
    while True:
        print("听音乐")
        time.sleep(0.3)


def coding():
    while True:
        print("写代码")
        time.sleep(0.3)


if __name__ == '__main__':
    # 创建任务
    music_process = multiprocessing.Process(target=music)
    coding_process = multiprocessing.Process(target=coding)
    # 启动进程执行任务
    music_process.start()
    coding_process.start()

