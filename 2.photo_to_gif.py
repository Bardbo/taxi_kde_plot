# -*- coding: utf-8 -*-
# @Author: Bardbo
# @Date:   2020-10-17 13:26:57
# @Last Modified by:   Bardbo
# @Last Modified time: 2020-10-17 13:27:50

import imageio
import os


def create_gif(image_list, gif_name, duration):
    """[summary]

    Args:
        image_list ([List]): [所有图片的路径名称列表]
        gif_name ([str]): [输出的GIF图片名称]
        duration ([number]): [图片播放的间隔时长]
    """
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)


if __name__ == "__main__":
    # 输入图片路径
    img_path = 'pic'
    # 输入GIF保存路径与名称
    gif_name = r'2017_10_31_O.gif'
    # 间隔时长
    duration = 0.5
    image_list = [img_path + '/' + i for i in os.listdir(img_path)]
    create_gif(image_list, gif_name, duration)
    print('GIF图片已生成')