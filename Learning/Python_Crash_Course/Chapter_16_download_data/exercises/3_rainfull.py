import csv
from datetime import datetime
from matplotlib import pyplot as plt

# 无雨量数据，用云量代替
# 获取Sitka云量数据
dates, clouds = [], []
filename = r'Chapter_16_test_file\sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            cloud = int(row[20])
        except ValueError:
            print(current_date, "missing data.")
        else:
            dates.append(current_date)
            clouds.append(cloud)

# 可视化云量数据
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, clouds, c='red', alpha=0.5)
plt.fill_between(dates, clouds, facecolor='blue', alpha=0.1)

# 设置图形格式
title = "Daily cloud cover - 2014\nSitka, AK"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Cloud Cover", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
