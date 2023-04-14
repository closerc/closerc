import os
import datetime

target_dir = r"D:/shopee月数据/2023/shopee月数据_3/no_data"
num = 0
err = 0
start_time = datetime.datetime.now()
for paths, dirnames, filenames in os.walk(target_dir):
    for dirname in dirnames:
        dirname_path = os.path.join(paths, dirname)
        try:
            content = os.listdir(dirname_path)  # 这是列表结构
            if content:
                pass
            else:
                num += 1
                print("空文件夹", dirname)
        except PermissionError:
            err += 1
            print("异常", "跳过", dirname)
end_time = datetime.datetime.now()
time = end_time - start_time
print("\n检测到了{}个空文件夹，{}个异常文件夹,消耗时间{}。".format(num, err, time))
