import pygal
from itertools import groupby


def draw_line(x_data, y_data, title, y_legend):
    """按时间序列分组作图

    Args:
        x_data (list)): x轴数据
        y_data (list): y轴数据
        title (str): 图表标题
        y_legend (str): y轴图例
    """
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])
    x_unique, y_mean = [*zip(*xy_map)]

    # 可视化
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title + '.svg')

    return line_chart
