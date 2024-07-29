import re

# 定义字符串，获取123，单独获取2和3
str1 = 'askdn123sjdio'
# 若正则表达式中带有分组，则建议用findall或search
result = re.search(r'\d(\d)(\d)', str1)
# 子表达式测结果会保存到对应的缓存区
print(result.group())
print(result.group(1))
print(result.group(2))

# 反向引用：\n，n表示缓冲区编号。例如\1表示都在第一个缓冲区
# 反向引用能用于匹配特定格式的字符，比如1111，2222
str2 = 'asds111sdk222k123'
result2 = re.finditer(r'(\d)\1\1', str2)
for i in result2:
    print(i.group())
