import matplotlib.pyplot as plt

from die import Die

# 创建一个D6
die = Die()

# 掷几次骰子，并将结果存储在一个列表中
results = [die.roll() for roll_num in range(1000)]

# 分析结果
frequencies = [results.count(value)
               for value in range(1, die.num_sides + 1)]

# 对结果进行可视化
x_labels = [str(x) for x in range(1, die.num_sides + 1)]
plt.bar(x_labels, frequencies, width=0.6)

plt.title("Results of rolling one D6 1000 times.", fontsize=24)
plt.xlabel("Result", fontsize=14)
plt.ylabel("Frequency of Result", fontsize=14)

plt.show()
