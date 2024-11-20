import csv
filename = '下载数据\sitka_rainfall_2015.csv'
with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)
    for index, column_header in enumerate(head_row):
        print(index, column_header)
    for row in reader:
        highs = int(row[1])
        lows = int(row[3])
        rainfall = row[21]
        date = row[0]
        print(date, '-', highs, '-', lows, '-', rainfall)
