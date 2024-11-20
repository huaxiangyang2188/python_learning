import csv
from matplotlib import pyplot as plt
from datetime import datetime
def get_weather_data(filename,datas,highs,lows):
    # get highs and lows from file
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        for row in reader:
            try:
                current_date = datetime.strptime(row[0],"%Y-%m-%d")
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print(current_date,'missing data')
            else:
                datas.append(current_date)
                highs.append(high)
                lows.append(low)
    # Get wheather data for Sitka
filename = '下载数据\sitka_weather_2014.csv'
datas = []
highs = []
lows = []
get_weather_data(filename,datas,highs,lows)
    # Plot data
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(datas,highs,c='red',alpha=0.5)
plt.plot(datas,lows,c='blue',alpha=0.5)
plt.fill_between(datas,highs,lows,facecolor='blue',alpha=0.15)
   # Get data for Death Valley
filename = '下载数据\death_valley_2014.csv'
datas = []
highs = []
lows = []
get_weather_data(filename,datas,highs,lows)
plt.plot(datas,highs,c='orange',alpha=0.5)
plt.plot(datas,lows,c='green',alpha=0.5)
plt.fill_between(datas,highs,lows,facecolor='green',alpha=0.15)
# Format plot
title = "Daily high and low temperatures - 2018"
title += "\nSitka, AK & Death Valley, CA"
plt.title(title,fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.ylim(10,130)

plt.show()





