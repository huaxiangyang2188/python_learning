import csv
from datetime import datetime
from matplotlib import pyplot as plt
# 读取数据文件

filename = '.\下载数据\death_valley_2014.csv'
# filename = 'C:\\Users\\lenovo\\Desktop\\python_project\\数据可视化\\下载数据\\death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates,highs,lows,rainfalls = [], [],[],[]
    for row in reader:
        try:
            current_date = datetime.strptime(row[0],"%Y-%m-%d")

            high = int(row[1])
            
            low = int(row[3])
            rainfall = float(row[19])
        except ValueError:
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
            rainfalls.append(rainfall)

# 根据数据绘制图表
fig =  plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.plot(dates,rainfalls,c='green',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
# 添加标题和轴标签
title = "Daily high and low temperatures-2014\nDeath Valley,CA"
plt.title(title,fontsize=20)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F), fontsize=16")
plt.tick_params(axis= 'both', which='major', labelsize=16)
plt.show()