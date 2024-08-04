import requests
import re
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker
import threading
# 使用爬虫获取表格数据，并生成饼图
"""
1 首先看饼图生成模块,传入参数的数据格式为[[],[],[]]形式,所以我们需要将数据组装成这种格式
  首先获取国家名称,可以看到html里面带有国家名称的部分html是这样的,所以根据这个就可以使用正则表达式筛选出国家名称
<a href=""><font>美国</font></a>
  再看数据部分,html的格式
<font>$218463.3<font>亿</font></font>
再将数据提取出来,然后封装正需要的数据结构,就可以生成饼图了
爬取的网页:http://127.0.0.1:8000/gdp.html
"""
countries = []
GDPDatas = []

def save_pic(url_list):
    num = 0
    for picurl in url_list:
        # 每循环次1次，模拟发送请求，获取图片字节流数据
        data = requests.get(picurl)
        data = data.content  # 不要解码，否则无法保存资源图片
        with open(f'source/spyder/{num}.jpg', 'wb') as f:
            f.write(data)
        num += 1


def get_pic():
    # 爬取http://127.0.0.1:8000/index.html页面的所有信息
    data = requests.get('http://127.0.0.1:8000/index.html')
    # 爬取到的内容，要根据.content属性获取数据
    data = data.content.decode('utf-8')
    # print(data)
    # 对data数据进行解析，采集所有的.jpg图片
    data_list = data.split('\n')
    # 使用for循环对data_list列表进行遍历
    # <td><img src="./images/1.jpg" width="184px" height="122px" /></td>
    url_list = []
    for line in data_list:
        # 对line变量进行解析，获取图片标签中的src图片地址
        result = re.match('.*src="(.*)" width.*', line)
        if result:
            url = result.group(1)  # ./images/0.jpg => http://127.0.0.1:8000/images/0.jpg
            url = 'http://127.0.0.1:8000' + url[1:]
            url_list.append(url)
    return url_list
def get_GDP_data():
    global countries
    global GDPDatas
    htmldata = requests.get('http://127.0.0.1:8000/gdp.html')
    data = htmldata.content.decode('utf-8')
    # 获取到数据后,通过\n分割,获取到每一行的html字符串
    lines = data.split('\n')
    for country in lines:
        countrydata = re.match('.*<font>(.*)</font></a>', country)
        if countrydata:
            countries.append(countrydata.group(1))
        # 接着提取数据
        GDPdata = re.match('.*\$(.*)<font>亿</font></font>', country)
        if GDPdata:
            GDPDatas.append(GDPdata.group(1))
    resultlist = list(zip(countries, GDPDatas))
    return resultlist


if __name__ == '__main__':
    data = get_GDP_data()
    jpg_threading = threading.Thread(target=get_pic,)
    gdp_threading = threading.Thread(target=get_GDP_data)
    jpg_threading.start()
    gdp_threading.start()
    c = (
        Pie()
        .add("", data)
        .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])
        .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        .render("pie_base.html")
    )
