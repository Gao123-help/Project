"""
1、with语句等价于try...except...finally语句。
    with里面封装了两个方法__enter__()上文管理器和__exit__()下文管理器，分别创建文件和关闭文件
2、生成器可以提高性能，节约大量资源。
    生成器中并没有保存具体数据，只保存了规则，通过生成器获取数据时，根据保存的规则生成数据
"""
# 推导式创建生成器
my_generator = (i * 2 for i in range(5))
# 调用
next(my_generator)
# 2、循环遍历
for value in my_generator:
    print(value)


# yield 生成器
def generator():
    my_list = [1, 2, 3, 4, 5]
    for i in my_list:
        print("开始生成")
        yield i
        print("结束生成")


g = generator()
for i in g:
    print(i)
