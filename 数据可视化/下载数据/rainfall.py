import csv
from datetime import datetime
from matplotlib import pyplot as plt
# Get data and raimfall data from file 
filename = '下载数据\sitka_rainfall_2015.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, rainfalls,totals = [],[],[]
  
    for row in reader:

        try:
            current_date = datetime.strptime(row[0],"%Y/%m/%d")
            # dates.append(current_date)
            rainfall = float(row[19])
        except ValueError:
            print(row[0],'missing data')
        else:
            rainfalls.append(rainfall)
            dates.append(current_date)
            if totals:
                totals.append(totals[-1]+rainfall)
            else:
                totals.append(rainfall)
# plot date
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, rainfalls, c='blue',alpha=0.5)
plt.fill_between(dates, rainfalls, facecolor='blue', alpha=0.2)
plt.plot(dates, totals, c='red', alpha=0.5)
plt.fill_between(dates,totals,facecolor='red',alpha=0.3)

# format plot
plt.title("Daily Rainfall Amount - 2015", fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Rainfall Amount (mm)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)
plt.show()

