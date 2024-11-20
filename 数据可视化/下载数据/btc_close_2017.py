import json
import pygal
import math
from itertools import groupby

# 将数据加载到一个列表中
filename = '下载数据\\btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)
#创建五个列表分别存储日期和收盘价等。
dates = []
months = []
weeks = []
weekdays = []
close = []
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))
# 创建图表
line_chart = pygal.Line(x_label_rotation=20,show_minor_x_labels=False)
line_chart.title = 'Bitcoin Closing Prices for 2017'
line_chart.x_labels = dates
N = 20  #每隔20天显示一次
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in close]
line_chart.add('close', close_log)
line_chart.render_to_file('btc_close_2017$.svg')
def draw_line(x_data,y_data,title,y_legend):
    xy_map = []
    for x,y in groupby(sorted(zip(x_data,y_data)),key=lambda _:_[0]):
        y_list = [v for _,v in y]
        xy_map.append((x,sum(y_list)/len(y_list)))
    x_unique,y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title+'.svg')
    return line_chart

idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(months[:idx_month],close[:idx_month], '收盘价月日均值', '月日均值')
line_chart_month





















    