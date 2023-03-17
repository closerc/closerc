import pygal

from random_walk import RandomWalk

# 创建一个RandomWalk实例，并将其包含的点都绘制出来
rw = RandomWalk(1000)
rw.fill_walk()
values = list(map(lambda x, y: (x, y), rw.x_values, rw.y_values))

# 可视化结果
scatter = pygal.XY(stroke=False)
scatter.title = "Random Walk"
scatter.add('rw', values)
scatter.render_to_file('random_walk.svg')
