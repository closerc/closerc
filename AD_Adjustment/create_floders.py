import os
import xlrd


def get_floders_name(filename, sheet_index):
    """从Excel文件中获取要创建的文件夹名字列表"""
    file = xlrd.open_workbook(filename)
    sheet = file.sheet_by_index(sheet_index)
    rows = sheet.nrows
    floder_names = sheet.col_values(1, 1, rows + 1)

    return floder_names


def create_floder(floder_names, path):
    """在指定的目录下创建文件夹

    Args:
        floder_names (list): 包含文件夹名字的列表
        path (str): 指定目录
    """
    for floder_name in floder_names:
        full_path = os.path.join(path, floder_name)
        if os.path.exists(full_path):
            print("文件夹 {} 已存在".format(floder_name))
        else:
            os.mkdir(full_path)


if __name__ == '__main__':
    filename = r'C:\Users\Administrator\Desktop\关键词12.31.xlsx'
    sheet_index = 3
    path = r'D:\shopee月数据\2023\shopee月数据_3\new_station'
    floder_names = get_floders_name(filename, sheet_index)
    create_floder(floder_names, path)
