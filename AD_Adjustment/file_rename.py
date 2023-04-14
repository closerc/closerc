import os
import xlsxwriter as xw
import xlrd  # 只读excel


# 提取文件名到表格
def getName(rp):
    print("开始提取文件名！")
    # 创建excel
    xlsxName = '批量命名.xlsx'
    workbook = xw.Workbook(xlsxName)
    sheet1 = workbook.add_worksheet('sheet1')
    row_0 = ['ID', '旧文件名', '新文件名']
    sheet1.write_row('A1', row_0)
    # 遍历文档，批量提取文件名并写入到表格
    m = 0
    for root, dirs, files in os.walk(rp + '\\文件'):
        for file in files:
            curName = os.path.join(file)
            # curPath = os.path.join(root,file)
            m += 1
            # 序号
            sheet1.write(m, 0, m)
            # 旧文件名
            sheet1.write(m, 1, curName)
            # 新文件名

    workbook.close()  # 关闭excel后台运行
    print("文件名提取完毕！")


# 批量创建文件夹
def createFolder(rp, name):
    # 打开文档
    xlsxName = name
    file = xlrd.open_workbook(rp + '\\' + xlsxName)  # xlrd模块
    sheet1 = file.sheet_by_index(0)
    rows = sheet1.nrows  # 获取行数
    # sheet1.row_values(0, 6, 10)  # 取第1行，第6~10列（不含第10表）
    # sheet1.col_values(0, 0, 5)  # 取第1列，第0~5行（不含第5行）
    # sheet1.row_slice(2, 0, 2)  # 获取单元格值类型和内容
    # sheet1.row_types(1, 0, 2)  # 获取单元格数据类型
    folderNames = sheet1.col_values(0, 1,
                                    rows + 1)  # 取第1列，第2~rows+1行（不含第rows+1行）
    if len(folderNames) > 1:
        # 批量创建合并文件夹
        for folder in folderNames:
            curPath = rp + '\\' + folder
            if os.path.exists(curPath) is False:
                os.mkdir(curPath)


if __name__ == '__main__':
    rootPath = os.getcwd()  # 获取当前文件路径
    xlsxName = '文件夹.xlsx'
    createFolder(rootPath, xlsxName)  # 批量创建文件夹
