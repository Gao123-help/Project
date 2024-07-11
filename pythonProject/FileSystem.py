# 文件操作
"""
请编写一个程序，实现从文本文件中读取数据，并进行简单的处理和输出。

    首先，程序需要从文本文件中读取一串数字，每个数字占据一行。文本文件的名称为 numbers.txt。
    然后，程序需要将读取到的数字进行累加求和，并输出求和结果。

注意：

    文本文件中的每行只包含一个整数。
    文件中的数字可能有正数、负数或零。

"""
f = open("numbers.txt", 'r')
# content = f.readlines()
# newcontent = [i.rstrip('\n') for i in content]
# print(newcontent)
sum = 0
while True:
    content = f.readline()
    content.rstrip('\n')
    print(content)
    if content == "":
        break
    sum += int(content)
print(sum)
f.close()
