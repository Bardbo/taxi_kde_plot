# -*- coding: utf-8 -*-
# @Author: Bardbo
# @Date:   2020-10-17 11:05:30
# @Last Modified by:   Bardbo
# @Last Modified time: 2020-10-17 16:18:28
# 数据处理常用库，当成Excel就行

import pandas as pd
# 绘图库
import matplotlib.pyplot as plt
import seaborn as sns
# 计时库
import time
# 进度条显示
from tqdm import tqdm
# plot_map是之前推荐的python交通向教程作者同济小旭学长写的添加底图的库
# 推文地址：https://mp.weixin.qq.com/s/pOnJrTCpvl4xIErtq3iOZA
import plot_map

# 设置为seaborn风格
sns.set()
# 解决matplotlib中文字体无法显示，以及负号显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# 绘图函数
def plot_hours_pic(hours, data, img_savepath='..'):
    """[绘制给定小时的滴滴出行热力图，并保存]

    Args:
        hours ([str]): [指定的时间（小时），如 '05', 表示早上5点]
        data ([pandas.DataFrame]): [传入的需要可视化的数据，本次以海口市2017-10-31日的滴滴出行的起点数据为例，数据来源于盖亚开放平台，经过了筛选和坐标转换等处理]
        img_savepath (str, optional): [存放底图瓦片数据的路径]. Defaults to '..'.
    """
    # 筛选出当前传入hours的数据
    data_h = data[data['出发时间'].str[11:13] == hours]
    # 创建画布
    fig = plt.figure(1, (3, 3), dpi=300)
    ax = plt.subplot(111)
    plt.sca(ax)
    # 绘制底图
    plot_map.plot_map(plt,
                      bounds=[110.20, 19.90, 110.50, 20.10],
                      zoom=12,
                      style=3,
                      imgsavepath=img_savepath)
    # 绘制热力图
    sns.kdeplot(
        data=data_h,
        x="起点经度_wgs84",
        y='起点纬度_wgs84',
        fill=True,
        alpha=0.3,  # 透明度
        cmap="RdYlGn_r",  # 色带
        bw_adjust=1)  # 核密度带宽
    # 关闭坐标轴
    plt.axis('off')
    # 设置显示范围
    plt.xlim(110.20, 110.50)
    plt.ylim(19.90, 20.10)
    # 将当前时间设置为标题
    plt.title(f'小时{hours}')
    # 保存图片
    plt.savefig(f'pic/{hours}.png')
    plt.close()


if __name__ == "__main__":
    # 读取数据
    data = pd.read_csv('haikou_2017_10_31_O.csv')
    # 记录开始时间
    start_time = time.time()
    # 遍历所有时段进行热力图的绘制与保存
    for h in tqdm(set(data['出发时间'].str[11:13])):
        plot_hours_pic(h, data)
        print(f'已完成时段{h}')
    # 打印出绘图所耗费的时间
    print(f'共耗时{time.time() - start_time}秒')
