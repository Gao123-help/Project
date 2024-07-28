import re

"""
1、查找特定开头的字符串
2、数据隐藏
3、敏感词过滤
"""
# str1 = 'suodjqu9dqdj'
# result = re.match('suo', str1)
# result2 = re.findall('9', str1)
# result3 = re.findall('\d', str1)  # \D代表非数字
# print(result)
# print(result2)
# print(result3)

# 正则表达式匹配多个字符,只能匹配连续的
str2 = '123adnj3nndj2'
result = re.match('\d{3}',str2)
print(result.group())

# 复杂的正则表达式匹配，可以使用正则工具箱辅助生成正则表达式，网上搜索正则工具箱
