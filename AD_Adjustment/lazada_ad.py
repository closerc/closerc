# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 16:43:02 2021

@author: Administrator
"""

import os
import pandas as pd
import math
from functools import reduce
import warnings

warnings.filterwarnings("ignore")
"""
处理lazada广告，新增、调整建议
1、生意参谋-商品明细-商品维度
2、广告-推广商品明细
"""


def lazada_ad(account):
    # 设置最低限价
    global min_price
    if country == 'ph':
        min_price = 100
    elif country == 'th':
        min_price = 300

    def bfh(x):
        if isinstance(x, str):
            x = x.replace("%", "")
        return x

    def hg(x):
        if isinstance(x, str):
            x = x.replace("-", "0")
        return x

    def get_percent(x, y):
        if y > 0:
            z = round(x / y * 100, 1)
        else:
            z = 0
        return z

    def get_roi(spend, sale):
        if spend > 0:
            roi = round(sale / spend, 2)
        else:
            roi = 0
        return roi

    def get_type(x, y):
        ad_type = x.split('_')[y]
        return ad_type

    def get_spend_percent(order, spend, price):
        if math.isnan(price):
            x = '-'
        else:
            if order == 0:
                x = round(spend / price * 100, 1)
            else:
                x = '-'
        return x

    # 读取数据
    def get_data(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                if '$' not in file:
                    if '生意参谋' in file:
                        shop_filename = path + "\\" + file
                        shop_data = pd.read_excel(shop_filename, skiprows=5)
                        shop_data = shop_data[shop_data['支付件数'] > 0]
                        shop_data = shop_data.loc[:, [
                            '商品名称', '商品/SKU访客数', '访客价值', '买家数', '支付订单量', '支付件数',
                            '支付金额', '转化率', '客单价'
                        ]]
                        shop_data = shop_data.drop_duplicates(subset='商品名称')
                        shop_data['转化率'] = shop_data['转化率'].map(hg)
                        shop_data['转化率'] = shop_data['转化率'].map(bfh).astype(float)
                        shop_data['访客价值'] = shop_data['访客价值'].map(hg).astype(float)
                        shop_data['客单价'] = shop_data['客单价'].astype(float)

                    elif '--202' in file:
                        ad_filename = path + "\\" + file
                        ad_data = pd.read_excel(ad_filename, skiprows=5)
                        ad_data.rename(columns={
                            '推广商品': '商品名称',
                            '加购的商品件数（全店维度）': '加购的商品件数'
                        }, inplace=True)
                        ad_data['推广类型'] = ad_data.apply(
                            lambda row: get_type(row['投放计划名称'], 0), axis=1)
                        ad_data['展示位'] = ad_data.apply(
                            lambda row: get_type(row['投放计划名称'], 1), axis=1)
                        ad_data['关键词类型'] = ad_data.apply(
                            lambda row: get_type(row['投放计划名称'], 2), axis=1)
                        ad_data = ad_data.groupby([
                            '投放计划名称', '推广类型', '展示位', '关键词类型', '商品名称', '推广商品ID',
                            '出价'
                        ])['花费', '曝光', '点击', '店铺订单数', '店铺销售件数', '店铺收入',
                           '直接引导销售件数', '直接引导收入'].sum().reset_index()
                        ad_data['CPC'] = ad_data.apply(
                            lambda row: get_roi(row["点击"], row["花费"]), axis=1)
                        ad_data['CTR%'] = ad_data.apply(
                            lambda row: get_percent(row["点击"], row["曝光"]),
                            axis=1)
                        ad_data['CR%'] = ad_data.apply(
                            lambda row: get_percent(row["店铺销售件数"], row["点击"]),
                            axis=1)
                        ad_data['ROI'] = ad_data.apply(
                            lambda row: get_roi(row["花费"], row["店铺收入"]),
                            axis=1)

        return shop_data, ad_data

    shop_data, ad_data = get_data(file_path)

    # 新增广告
    def new_ad(shop_cr, visit_value, cost, order, price):
        if math.isnan(cost):
            if visit_value >= 12 and shop_cr >= 2 and order > 1 and price >= min_price:
                x = 'New'
            else:
                x = '不做'
        else:
            x = '已做'
        return x

    dfs = [shop_data, ad_data]
    shop_ad_data = reduce(
        lambda left, right: pd.merge(left, right, on='商品名称', how='left'), dfs)
    shop_ad_data['ad'] = shop_ad_data.apply(lambda row: new_ad(
        row["转化率"], row["访客价值"], row["花费"], row["支付件数"], row["客单价"]), axis=1)
    shop_ad_data.drop(shop_ad_data.columns[9:27], axis=1, inplace=True)
    ad_new = shop_ad_data[(shop_ad_data['ad'] == 'New')]
    ad_new.to_excel(file_path + "\\0001 新增.xlsx", index=False)
    print('新增完成')

    # 调整广告
    def adjust_ad(click, roi, spend, ad_order, shop_order, sale_percent,
                  spend_percent):
        global adjust
        if 0 < roi < 8:
            adjust = '降'
        elif 8 <= roi < 15:
            adjust = '不调整'
        elif 15 <= roi:
            if sale_percent < 30 or ad_order >= 3:
                adjust = '加'
            else:
                adjust = '不调整'
        else:
            if math.isnan(shop_order):
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

        return adjust

    ad_data['广告总销(直接)'] = ad_data.商品名称.apply(
        lambda x: ad_data.直接引导收入.loc[ad_data.商品名称 == x].sum())
    ad_data['广告总销'] = ad_data.商品名称.apply(
        lambda x: ad_data.店铺收入.loc[ad_data.商品名称 == x].sum())
    shop_data_temp = shop_data.loc[:, [
        '商品名称', '访客价值', '支付件数', '支付金额', '转化率', '客单价'
    ]]
    df_ad = [ad_data, shop_data_temp]
    ad_shop_data = reduce(
        lambda left, right: pd.merge(left, right, on='商品名称', how='left'),
        df_ad)
    ad_shop_data['销售占比%'] = ad_shop_data.apply(
        lambda row: get_percent(row['广告总销(直接)'], row['支付金额']), axis=1)
    ad_shop_data['花费占比%'] = ad_shop_data.apply(
        lambda row: get_spend_percent(row['店铺销售件数'], row['花费'], row['客单价']),
        axis=1)
    ad_shop_data.sort_values(by=["花费"],
                             axis=0,
                             ascending=[False],
                             inplace=True)
    ad_shop_data['调整'] = ad_shop_data.apply(
        lambda row: adjust_ad(row["点击"], row["ROI"], row["花费"], row["店铺销售件数"],
                              row["支付件数"], row["销售占比%"], row["花费占比%"]),
        axis=1)
    ad_shop_data.to_excel(file_path + "\\0002 广告调整.xlsx", index=False)

    repeat_ad_temp = ad_shop_data.loc[:, ['推广类型', '展示位', '关键词类型', '商品名称']]
    repeat_ad_temp.drop_duplicates(keep=False, inplace=True)
    repeat_ad = pd.merge(ad_shop_data,
                         repeat_ad_temp,
                         on=['推广类型', '展示位', '关键词类型', '商品名称'],
                         how='left',
                         indicator=True)
    repeat_ad = repeat_ad.query('_merge == "left_only"').drop('_merge', 1)
    repeat_ad.to_excel(file_path + "\\0003 重复广告.xlsx", index=False)

    shop_sales = round(sum(shop_data['支付金额']), 0)
    print("店铺销售额：", shop_sales)
    shop_order = round(sum(shop_data['支付件数']), 0)
    # print('店铺订单数：', shop_order)
    shop_ATV = round(shop_sales / shop_order, 0)
    print('店铺客单价：', shop_ATV)
    shop_click = round(sum(shop_data['商品/SKU访客数']), 0)
    # print('店铺访客数：', shop_click)
    shop_cr = str(round(shop_order / shop_click * 100, 2)) + '%'
    print('店铺转化率：', shop_cr)
    ad_click = sum(ad_data['点击'])
    # print("点击：", ad_click)
    ad_spend = round(sum(ad_data['花费']), 0)
    print("广告花费：", ad_spend)
    ad_order = sum(ad_data['店铺销售件数'])
    # print("销售件数：", ad_order)
    ad_sales = round(sum(ad_data['店铺收入']), 0)
    print("广告销售额：", ad_sales)
    ad_ATV = round(ad_sales / ad_order, 0)
    print("广告客单价：", ad_ATV)
    ad_cr = str(round(ad_order / ad_click * 100, 2)) + '%'
    print("广告转化率：", ad_cr)
    ad_roi = round(ad_sales / ad_spend, 2)
    print("ROI：", ad_roi)
    ad_shop = str(round(ad_sales / shop_sales * 100, 2)) + '%'
    print("广告占比：", ad_shop)
    cpc = round(ad_spend / ad_click, 2)
    print("CPC：", cpc)
    spend_percent = str(round(ad_spend / shop_sales * 100, 2)) + '%'
    print("花费占比", spend_percent)


if __name__ == "__main__":
    account = 'YSwimming'
    country = 'th'
    root_path = r'D:\紫鸟\Super Browser\Lazada'
    file_path = root_path + "\\" + account + "\\" + country
    if os.path.exists(file_path):
        print('\033[1;33;40m----------------BEGIN:', account,
              '----------------\033[0m')
        lazada_ad(account)
    else:
        print('地址不存在')
