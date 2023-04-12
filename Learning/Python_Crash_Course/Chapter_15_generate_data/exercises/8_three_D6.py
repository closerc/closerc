import pygal

from die import Die

# 创建三个D6
die_1 = Die()
die_2 = Die()
die_3 = Die()

# 掷骰子多次，并将结果存储在一个列表中
results = [die_1.roll() + die_2.roll() + die_3.roll()
           for roll_num in range(50000)]

# 分析结果
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequencies = [results.count(value)
               for value in range(3, max_result + 1)]

# 可视化结果
hist = pygal.Bar()
hist.title = "Results of rolling three D6 50,000 times."
hist.x_labels = [str(x) for x in range(3, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6+D6+D6', frequencies)
hist.render_to_file(r'Chapter_15_test_file\three_D6.svg')
