本文给大家带来的是Python中的一种热力图绘制方法，运用遍历的方法批量绘制图片，然后将多个图片合成GIF。如果装了Anaconda，应该是不需要额外安装库的，如果报错可能是所使用的库版本不一致，按照提示更新即可。本文中使用到了同济小旭学长（之前推荐的Python交通向教程作者）开发的在绘图中添加底图的脚本plot_map(在下文给出的GitHub项目中有提供)，挺好用的，不知道什么会时候添加对国内高德地图等的支持。

## 1. 项目地址和使用

本文所需代码和数据均以上传至GitHub， 传送门：https://github.com/Bardbo/taxi_kde_plot，使用前请下载（觉得下载速度慢的同学可以使用之前推荐的多线程下载方法哦，如NDM）

**快速使用：**

1. 批量绘制24个时段的热力图，以下命令均在GitHub下载文件的目录下进入命令行运行。

`python .\1.不同小时的热力图绘制.py`

2. 将24张图合成GIF

`python .\2.photo_to_gif.py`

这样就完成了，可以发现原本空的pic文件夹内多出了24张热力图，py文件同目录下多出了一个GIF文件：**2017_10_31_O.gif**

## 2. 代码解析等

本文所使用数据为滴滴开放的海口市出行数据，通过前期的简单清洗和坐标转换得到了可用的数据，由于原数据较大，大家需要完整数据的可以前往**盖亚开放平台**申请，传送门：https://outreach.didichuxing.com/research/opendata/

本文仅提供了处理好后一天的出行起点数据，就是那个csv，基于此分时段绘制海口市滴滴出行的起点热力图。

**1.不同小时的热力图绘制.py**文件是热力图的绘制代码，其中tqdm是一个显示循环进度的库，只需要在遍历一个可迭代对象时给它裹上一层包装就可以了（如下），简单实用。

`for h in tqdm(set(data['出发时间'].str[11:13])):`

本处使用遍历的方式来绘制24个时段的图。然后核心的绘图代码如下：

```python
# 绘制热力图
sns.kdeplot(
	data=data_h,
    x="起点经度_wgs84",
    y='终点纬度_wgs84',
    fill=True,
    alpha=0.3,  # 透明度
    cmap="RdYlGn_r",  # 色带
    bw_adjust=1)  # 核密度带宽
```

seaborn的绘图与matplotlib是有些不同的，seaborn针对于数据集进行绘图，因此传入的data为pandas.DataFrame形式，本次调用的是kdeplot方法，然后设置好x和y数据（都是列名，表示传入DataFrame中的该列），设置色带等（matplotlib提供了众多色带，其对应的代号可在其官方网站查阅 https://matplotlib.org/tutorials/colors/colormaps.html?highlight=rdylgn；

seaborn是基于matplotlib构建的，因此可以使用matplotlib的绘图方法对细节进行调整，比如关掉坐标轴等。特别需注意的是bw_adjust是核密度方法绘制热力图的核心参数，**带宽越大结果就越平滑**，在早些的版本中该参数是bw，但是在0.11版中被分离成了两个参数，一个是bw_adjust，另一个是bw_method，本文仅设置了带宽，没有设置估计带宽的方法。

**2.photo_to_gif.py**文件可以将图片合成GIF，原理实际上就是轮播图片，然后在图片播放时设置播放间隔，达到动图的效果，主要是使用**imageio.mimsave**来实现GIF的保存，就不过多介绍了，相对较简单。

来看看结果吧，上述两个文件运行的结果如下：

![2017_10_31_O](https://i.loli.net/2020/10/17/RYWdi7vBhgbm8EL.gif)