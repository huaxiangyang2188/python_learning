import csv
filename = '下载数据\sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    events = []
    for row in reader:
        events.append(row[19])
    print(events)
