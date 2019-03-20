import cv2
import numpy as np
from PIL import Image
from dist import *
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d
import os


def extract_frame(file, frame_number=100, distance_name='manhattan'):
    """
    :param file: 文件名
    :param frame_number: 抽取的帧数
    :param distance_name: 采用的距离
    :return:
    """
    extract_id = []

    distribution = distance_distribution(file, distance_name)

    print('Start extracting...')

    distance_sum = np.sum(distribution)
    block = float(distance_sum/frame_number)
    s = 0
    block_start = 0
    block_end = 0
    for i in range(distribution.size):
        if s>block:
            block_end = i
            # 提取block第一帧
            frame_id = block_start
            extract_id.append(frame_id)
            block_start = block_end

            # 初始化block
            s = 0
        s+=distribution[i]
    video = cv2.VideoCapture(file)

    i = 0
    j = 0
    file_dir = os.path.dirname(file)
    if not os.path.exists(os.path.join(file_dir, os.path.basename(file)[:-4])):
        os.makedirs(os.path.join(file_dir, os.path.basename(file)[:-4]))

    while j<len(extract_id):
        ret, frame = video.read()
        if i==extract_id[j]:
            # 抽取该帧
            save_dir = os.path.join(file_dir, os.path.basename(file)[:-4], f'extract_frame_{distance_name}')
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
            cv2.imwrite(os.path.join(save_dir, str(i).zfill(8)+'.jpg'), frame)

            # 跳转到要抽取的下一帧
            j+=1

        i+=1

    print('Extract frame id:\n', extract_id)
    return extract_id

    pass

def distance_distribution(video_file, distance_name):
    """
    :param video_file: 视频文件名
    :return: 距离分布，ndarray
    """
    distance_method_dic = {'manhattan': manhattan,
                           'euclidean': euclidean,
                           'cosine': cosine,
                           'phash_hamming': phash_hamming}
    times = 0.05    # 缩放倍数

    video = cv2.VideoCapture(video_file)
    i = 1
    dist_list = []

    print('Loading...')
    # 读取第一帧
    ret, frame = video.read()
    # print(i, ret)
    start = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    start = shrink(start, times=times)

    while video.isOpened():
        ret, frame = video.read()
        # print(i, ret)

        if not ret:
            print(f"The video has {i} frames!")
            break


        if i % 15 == 0:
            end = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            end = shrink(end, times=0.05)

            if distance_name == 'phash_hamming':
                # 使用哈希编码需将 ndarray 转成 PIL 对象
                start = Image.fromarray(start)
                end = Image.fromarray(end)
                distance = phash_hamming(start, end, hash_size=32, highfreq_factor=2)
            else:
                distance = distance_method_dic[distance_name](start, end)
            # dist_list.append(distance*(1/times)**2)
            # dist_list.append(distance/times)
            dist_list.append(distance)

            start = end

        i += 1
    video.release()
    dist_list = np.array(dist_list)
    distribution = interpolation(dist_list)
    return distribution

def interpolation(y=None, method='linear'):
    """
    距离分布插值，将半秒间隔的插成每帧
    :param y: 待插值的距离分布
    :param method: 插值方式，默认为线性插值 'linear', 'nearest', 'zero', 'slinear', 'quadratic', 'cubic', 'previous', 'next'
    :return: 插值后的距离分布，ndarray
    """

    # x = np.linspace(0, 10 * np.pi, num=20)
    # y = np.sin(x)

    x = np.array([i*15 for i in range(y.size)])
    f1 = interp1d(x, y, kind=method)  # 线性插值
    x_pred = np.array(range(x[-1]))
    y1 = f1(x_pred)

    return y1

def shrink(image, times=0.05):
    """
    缩放图像
    :param image_path:  ndarray
    :param times: 缩放为原来的times，取值 0-1，默认为1
    :return: ndarray
    """
    small_image = cv2.resize(image, None, fx=times, fy=times)
    return small_image


