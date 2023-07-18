# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 10:30:58 2022

@author: Administrator
"""

import os
import pandas as pd
import shutil
import zipfile
import warnings
warnings.filterwarnings("ignore")


def lazada_placement(root_path):
    for root, dirs, files in os.walk(root_path):
        shop_station = root.split("\\")[-1]
        shop = shop_station.split('-')[0]
        print(shop_station)
        # print(shop)
        for file in files:
            if '$' not in file:
                if '--' in file:
                    filename = root_path + '\\' + shop + '\\' + shop_station + '\\' + file
                    # print(filename)
                    all_data = pd.read_excel(filename, skiprows=7, engine='openpyxl')
                    SS_data = all_data[all_data['Placement'] == 'Sponsored Search']
                    SP_data = all_data[all_data['Placement'] == 'Sponsored Products']
                    SS_SP_data = all_data[(all_data['Placement'] == 'All - Sponsored Products') | (all_data['Placement'] == 'All - Sponsored Search')]

                    SS_path = r"D:\lazada直通车\\" + shop + '\\' + shop_station
                    if os.path.exists(SS_path):
                        pass
                    else:
                        os.makedirs(SS_path)

                    if SS_data.empty:
                        pass
                    else:
                        SS_data.to_excel(SS_path + '\\' + file, index=False)

                    SP_path = r"D:\lazada超级推荐\\" + shop + '\\' + shop_station
                    if os.path.exists(SP_path):
                        pass
                    else:
                        os.makedirs(SP_path)

                    if SP_data.empty:
                        pass
                    else:
                        SP_data.to_excel(SP_path + '\\' + file, index=False)

                    SS_SP_path = r"D:\lazada全效宝\\" + shop + '\\' + shop_station
                    if os.path.exists(SS_SP_path):
                        pass
                    else:
                        os.makedirs(SS_SP_path)

                    if SS_SP_data.empty:
                        pass
                    else:
                        SS_SP_data.to_excel(SS_SP_path + '\\' + file, index=False)

                if 'Business' in file:
                    old_path = root_path + '\\' + shop + '\\' + shop_station + '\\' + file
                    shutil.copy(old_path, SS_path + '\\' + file)
                    shutil.copy(old_path, SP_path + '\\' + file)
                    shutil.copy(old_path, SS_SP_path + '\\' + file)


def lazada_zip(start_dir, zip_file):
    # start_dir要压缩的文件路径
    # zip_file输出zip文件的路径
    zip_file = zip_file + '.zip'
    z = zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED)
    # print(z)
    for path, dirname, file_name in os.walk(start_dir):
        # print('文件夹根路径', path)
        fpath = path.replace(start_dir, '')  # 去除根路径名称
        # print('--去除根路径：', fpath)
        fpath = fpath and fpath + os.sep   # 在原fpath加上\
        # print('**去除根路径+\:', fpath)

        for filename in file_name:
            z.write(os.path.join(path, filename), fpath + filename)
    z.close()
    return zip_file


if __name__ == "__main__":
    root_path = r'D:\lazada月数据'
    # root_path = 'r' + input('路径（shift+右键，复制为路径）：')
    lazada_placement(root_path)
    lazada_zip(r'D:\lazada超级推荐', r'D:\lazada超级推荐')
    lazada_zip(r'D:\lazada全效宝', r'D:\lazada全效宝')
    lazada_zip(r'D:\lazada直通车', r'D:\lazada直通车')
