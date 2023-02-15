# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 11:22:02 2021

@author: Administrator
"""

import os
import pandas as pd
import math
import time
import warnings
warnings.filterwarnings("ignore")

"""
处理shopee广告,需下3个表：
1.综合广告数据
2.商业分析--关键指标
3.商业分析--商品--表现
"""


def shopee_ad(account):
    country = account[-2:].lower()
    file_path = root_path + "\\" + account
    print('\033[1;33;40m----------------BEGIN:', account, '----------------\033[0m')

    # 设置花费限制,最低客单价
    global min_cost, min_price
    if country == 'ph':
        min_cost = 30
        min_price = 100
    elif country == 'my':
        min_cost = 2
        min_price = 15
    elif country == 'th':
        min_cost = 35
        min_price = 300
    elif country == 'vn':
        min_cost = 5000
        min_price = 60000

    def replace_dh(x):
        if isinstance(x, str):
            x = x.replace(",", "")
        return x

    def get_percent(x, y):
        if y != '-':
            if y > 0:
                z = round(x / y * 100, 1)
            else:
                z = 0
        else:
            z = '-'
        return z

    def get_roi(spend, sale):
        if spend > 0:
            roi = round(sale / spend, 2)
        else:
            roi = 0
        return roi

    def get_cpc(spend, click):
        if click > 0:
            cpc = round(spend / click, 2)
        else:
            cpc = 0
        return cpc

    def get_sale_percent(x, y):
        if y > 0:
            sale_percent = round(x / y * 100, 2)
        else:
            if x > 0:
                sale_percent = 1
            else:
                sale_percent = ''
        return sale_percent

    def get_atv(sales, order):
        if order > 0:
            atv = round(sales / order, 0)
        else:
            atv = '-'
        return atv

    def get_Visitor_value(sales, click):
        if click > 0:
            Visitor_value = round(sales / click, 2)
        else:
            Visitor_value = 0
        return Visitor_value

    def vn_xsd(x):
        if isinstance(x, str):
            x = x.replace(".", "")
        return x

    def get_data(path):
        for root, dirs, files in os.walk(file_path):
            for file in files:
                if '$' not in file:
                    if '-shop-stats' in file:
                        shop_filename = file_path + "\\" + file
                        if country == 'vn':
                            # encoding="unicode_escape"
                            shop_data = pd.read_excel(shop_filename, sheet_name="已下订单").applymap(vn_xsd).applymap(replace_dh)
                        else:
                            shop_data = pd.read_excel(shop_filename, sheet_name="已下订单").applymap(replace_dh)

                    elif 'parentskudetail' in file:
                        skusale_filename = file_path + "\\" + file
                        skusale_data = pd.read_excel(skusale_filename).applymap(replace_dh)

                        for a in list(skusale_data):
                            if '销售额(已下单)' in a:
                                skusale_data.rename(columns={a: '销售额(已下单)'}, inplace=True)
                            elif '商品页面访客' in a:
                                skusale_data.rename(columns={a: '商品页面访问量'}, inplace=True)

                        skusale_data = skusale_data[skusale_data['商品页面访问量'] != '-']

                        if country == 'vn':
                            skusale_data['销售额(已下单)'] = skusale_data['销售额(已下单)'].map(vn_xsd).astype(float)

                        for col in ['商品页面访问量', '销售额(已下单)']:
                            skusale_data[col] = skusale_data[col].astype('float')

                        sku_sale = skusale_data.loc[:, ['商品编号', '商品页面访问量', '买家数 (已下单)', '件数（已下单）', '销售额(已下单)']]

                    elif 'Overall' in file:
                        ad_filename = file_path + "\\" + file
                        new_ad_name = file_path + "\\副本.csv"
                        old_file = open(ad_filename, 'r', encoding='utf-8')
                        a = old_file.readlines()
                        new_file = open(new_ad_name, 'w', encoding='utf-8')
                        b = ''.join(a[6:])
                        new_file.write(b)
                        old_file.close()
                        new_file.close()
                        ad_data_all = pd.read_csv(open(new_ad_name, encoding='utf-8'))

                        if '展示次数' in ad_data_all.columns:
                            ad_data_all.rename(columns={'展示次数': '浏览数'}, inplace=True)

        return shop_data, sku_sale, ad_data_all

    # 调整广告
    def ad_adjust(status, roi, sale_percent, spend_percent, shop_order, ad_order, click, spend):
        global adjust
        if status == '进行中':
            if 0 < roi < 8:
                adjust = '降'
            elif 8 <= roi < 15:
                adjust = '不调整'
            elif 15 <= roi:
                if ad_order >= 3:
                    adjust = '加'
                else:
                    adjust = '不调整'
            else:
                if math.isnan(shop_order) or shop_order == 0:
                    adjust = '关'
                else:
                    if click >= 40:
                        adjust = '降'
                    elif 20 <= click < 40:
                        if spend_percent >= 10:
                            adjust = '降'
                        else:
                            adjust = '不调整'
                    elif 10 <= click < 20:
                        adjust = '不调整'
                    else:
                        if sale_percent < 30:
                            adjust = '加'
                        else:
                            adjust = '不调整'
        else:
            adjust = '-'
        return adjust

    # 新增广告
    def new_ad(ad_name, shop_cr, shop_order, shop_atv, visit_value):
        if str(ad_name) == 'nan':
            if visit_value >= 12 and shop_cr >= 2 and shop_order > 1 and shop_atv >= min_price:
                x = 'New'
            else:
                x = '不做'
        else:
            x = '已做'
        return x

    def get_spend_percent(order, spend, price):
        if price == '-':
            x = '-'
        else:
            if order == 0:
                x = round(spend / price * 100, 1)
            else:
                x = '-'
        return x

    shop_data, sku_sale, ad_data_all = get_data(file_path)

    ad_data = ad_data_all.loc[:, ['广告名称', '商品编号', '状态', '广告类型', '浏览数', '点击数', '花费',
                              '转化', '直接转化', '商品已出售', '直接已售商品', '销售金额', '直接销售金额']]

    ad_data['广告总直接销售'] = ad_data.商品编号.apply(lambda x: ad_data_all.直接销售金额.loc[ad_data_all.商品编号 == x].sum())
    ad_data['广告总销'] = ad_data.商品编号.apply(lambda x: ad_data_all.销售金额.loc[ad_data_all.商品编号 == x].sum())
    ad_data['CPC'] = ad_data.apply(lambda row: get_cpc(row["花费"], row["点击数"]), axis=1)
    ad_data['ROI'] = ad_data.apply(lambda row: get_roi(row["花费"], row["销售金额"]), axis=1)
    ad_data['CTR'] = ad_data.apply(lambda row: get_percent(row["点击数"], row["浏览数"]), axis=1)
    ad_data['CR'] = ad_data.apply(lambda row: get_percent(row["商品已出售"], row["点击数"]), axis=1)

    sku_sale['CR_shop'] = sku_sale.apply(lambda row: get_percent(row["件数（已下单）"], row["商品页面访问量"]), axis=1)
    sku_sale['访问价值'] = sku_sale.apply(lambda row: get_Visitor_value(row['销售额(已下单)'], row['商品页面访问量']), axis=1)

    ad_shop_sale = ad_data.merge(sku_sale, on='商品编号', how='outer')
    ad_shop_sale['客单价'] = ad_shop_sale.apply(lambda row: get_atv(row['销售额(已下单)'], row['件数（已下单）']), axis=1)
    ad_shop_sale['销售占比'] = ad_shop_sale.apply(lambda row: get_sale_percent(row["广告总直接销售"], row["销售额(已下单)"]), axis=1)
    ad_shop_sale['花费占比'] = ad_shop_sale.apply(lambda row: get_spend_percent(row["商品已出售"], row["花费"], row["客单价"]), axis=1)

    ad_shop_sale['新增建议'] = ad_shop_sale.apply(lambda row: new_ad(row['广告名称'], row['CR_shop'], row['件数（已下单）'], row['客单价'], row['访问价值']), axis=1)
    ad_shop_sale['调整建议'] = ad_shop_sale.apply(lambda row: ad_adjust(row['状态'], row['ROI'], row['销售占比'], row['花费占比'], row['件数（已下单）'],
                                                                    row['商品已出售'], row['点击数'], row['花费']), axis=1)

    ad_shop_sale = ad_shop_sale.loc[:, ['广告名称', '商品编号', '状态', '广告类型', 'CPC', 'ROI', '销售占比', '花费', '花费占比', '广告总销', 'CR',
                                        'CR_shop', '点击数', '浏览数', 'CTR', '转化', '商品已出售', '销售金额', '商品页面访问量',
                                        '买家数 (已下单)', '件数（已下单）', '销售额(已下单)', '客单价', '访问价值', '新增建议', '调整建议']]
    ad_shop_sale.columns = ['广告名称', '商品编号', '状态', '广告类型', 'CPC', 'ROI', '销售占比', '花费', '花费占比', '广告总销', 'CR', 'CR_shop', '点击数', '浏览数',
                            'CTR', '转化', '广告件数', '广告销售额', '店铺点击', '店铺买家数', '店铺件数', '店铺销售额', '客单价', '访问价值', '新增建议', '调整建议']
    ad_shop_sale.sort_values(by=["广告总销", "店铺销售额"], axis=0, ascending=[False, False], inplace=True)
    timetemp = time.strftime("%y.%m.%d", time.localtime(time.time()))
    ad_shop_sale.to_excel(file_path + '\\' + timetemp + ' 广告新增调整.xlsx', index=False)

    shop_sales = round(float(shop_data.iat[0, 1]), 2)
    print("店铺销售额：", shop_sales)
    shop_order = round(float(shop_data.iat[0, 2]), 0)
    # print('店铺订单数：', shop_order)
    shop_ATV = round(shop_sales / shop_order, 0)
    print('店铺客单价：', shop_ATV)
    shop_click = round(float(shop_data.iat[0, 5]), 0)
    # print('店铺访客数：', shop_click)
    shop_cr = str(round(shop_order / shop_click * 100, 2)) + '%'
    print('店铺转化率：', shop_cr)
    ad_click = sum(ad_data['点击数'])
    # print("点击：", ad_click)
    ad_spend = round(sum(ad_data['花费']), 0)
    print("广告花费：", ad_spend)
    ad_order = sum(ad_data['商品已出售'])
    # print("销售件数：", ad_order)
    ad_sales = round(sum(ad_data['销售金额']), 0)
    print("广告销售额：", ad_sales)
    ad_ATV = round(ad_sales / ad_order, 0)
    print("广告客单价：", ad_ATV)
    ad_cr = str(round(ad_order / ad_click * 100, 2)) + '%'
    print("广告转化率：", ad_cr)
    ad_roi = round(ad_sales / ad_spend, 2)
    print("ROI：", ad_roi)
    ad_shop = str(round(ad_sales / shop_sales * 100, 2)) + '%'
    print("广告占比：", ad_shop)
    spend_percent = str(round(ad_spend / shop_sales * 100, 2)) + '%'
    print('花费占比：', spend_percent)
    cpc = round(ad_spend / ad_click, 2)
    print("CPC：", cpc)

    os.remove(file_path + "\\副本.csv")


if __name__ == "__main__":
    account_list = ['kuike061.th']
    root_path = r'D:\紫鸟\Super Browser\Shopee'
    for account in account_list:
        shopee_ad(account)
