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
                    all_data = pd.read_excel(filename)
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
    zip_file = zip_file + '.zip'
    z = zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED)
    for path, dirname, file_name in os.walk(start_dir):
        fpath = path.replace(start_dir, '')
        fpath = fpath and fpath + os.sep

        for filename in file_name:
            z.write(os.path.join(path, filename), fpath + filename)
    z.close()
    return zip_file


if __name__ == "__main__":
    root_path = r'D:\lazada月数据'
    lazada_placement(root_path)
    lazada_zip(r'D:\lazada超级推荐', r'D:\lazada超级推荐')
    lazada_zip(r'D:\lazada全效宝', r'D:\lazada全效宝')
    lazada_zip(r'D:\lazada直通车', r'D:\lazada直通车')
