import csv
from datetime import datetime
from matplotlib import pyplot as plt
import os
# 读取数据文件

filename = '.\下载数据\death_valley_2014.csv'

path = os.path.dirname(filename)
print(path)
# filename = 'C:\\Users\\lenovo\\Desktop\\python_project\\数据可视化\\下载数据\\death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    print(reader)