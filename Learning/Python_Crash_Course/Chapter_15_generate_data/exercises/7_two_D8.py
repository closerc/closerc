import pygal

from die import Die

# 创建两个D8
die_1 = Die(8)
die_2 = Die(8)

# 掷骰子多次，并将结果存储在一个列表中
results = [die_1.roll() + die_2.roll()
           for roll_num in range(500000)]

# 分析结果
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value)
               for value in range(2, max_result + 1)]

# 可视化结果
hist = pygal.Bar()
hist.title = "Results of rolling two D8 500,000 times."
hist.x_labels = [str(x) for x in range(2, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D8+D8', frequencies)
hist.render_to_file('two_D8.svg')
