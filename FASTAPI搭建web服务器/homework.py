"""
请爬取地址为：https://mip.phb123.com/hangye/qiche/pinpai/ ,
请求爬取汽车品牌销量排行榜2023中前100的数据并保存到cars.csv, 按照品牌以及全年销量，
取前15名进行柱状图绘制，注意按照销量来展示图形，并生成保存资源，html命名为cars_top15.html并用于展示。
绘制柱状图提示：

"""
import re
import requests
from pyecharts import options as opts
from pyecharts.charts import Bar
import csv

# 导出到csv的格式为[[],[],[]]的格式
# 每个元素为排名 品牌 1月销量 全年销量 最佳车型
# 定义全局变量存储爬取到的数据
data_list = []
headline = ('排名', '品牌', '1月销量', '全年销量', '最佳车型')
data_list.append(headline)

"""
<a href="/hangye/qiche/pinpai/dc_16.html" title="比亚迪" target="_blank">比亚迪</a>
<td>264438</td>
<span class="number num100">100</span>
"""


def get_car_data():
    data_html = requests.get('https://mip.phb123.com/hangye/qiche/pinpai/')
    datas = data_html.content.decode('utf-8')
    data_lines = datas.split('\n')
    randnames = []  # 品牌名称
    cars = []  # 最佳车型
    sale_amount_1 = []  # 1月销量
    sale_year = []  # 年销量
    ranking = []
    count = 0
    count2 = 0
    # 根据数据特征用正则表达式筛选出想要的数据
    for line in range(len(data_lines)):
        # 品牌名称 这里得到的结果第n个是品牌名称,n+1个是最佳车辆
        rand_name = re.match(r'.*dc_.*\.html" title="(.*[^月])" target=.*', data_lines[line])
        if rand_name:
            count += 1
            ranking.append(count)
            if count % 2 == 0:
                cars.append(rand_name.group(1))
            else:
                randnames.append(rand_name.group(1))
        # 销量,第n个是1月销量,n+1是年销量
        # print(data_lines[line])
        saleAmount = re.match(r'^\s{1,}<td>([0-9]*)</td>$', data_lines[line])
        if saleAmount:
            count2 += 1
            if count2 % 2 == 0:
                sale_year.append(saleAmount.group(1))
            else:
                sale_amount_1.append(saleAmount.group(1))
        # 排名

        if count == 200:
            break
    # print(f'获得的品牌名称:{randnames}')
    # print(f'最佳车型:{cars}')
    # print(f'1月销量:{sale_amount_1}')
    # print(f'年销量:{sale_year}')
    result = list(zip(ranking, randnames, sale_amount_1, sale_year, cars))
    return result


def save_to_csv(data):
    # 将数据保存到CSV文件
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)


def create_tree_graphic(data, num):
    # 创建 Bar 实例
    x_data = []
    y_data = []
    for i in range(1, num+1):
        x_data.append(data[i][1])
        y_data.append(data[i][3])
    print(x_data)
    print(y_data)

    bar = (
        Bar()
        .add_xaxis(x_data)
        .add_yaxis("销量", y_data)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="汽车销量排行"),
            xaxis_opts=opts.AxisOpts(name="品牌"),
            yaxis_opts=opts.AxisOpts(name="销量"),
        )
    )

    # 渲染生成柱状图（默认为 HTML 文件）
    bar.render("bar_chart.html")


if __name__ == '__main__':
    result = get_car_data()
    data_list += result
    print(data_list)
    save_to_csv(data_list)
    create_tree_graphic(data_list, 15)
