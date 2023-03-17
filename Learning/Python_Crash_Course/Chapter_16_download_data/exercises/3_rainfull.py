import csv

filename = r'Learning\Python_Crash_Course\Chapter_16_download_data\sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column_name in enumerate(header_row):
        print(index, column_name)
