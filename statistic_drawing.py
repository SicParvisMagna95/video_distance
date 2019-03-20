import glob
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from utils import *
from dist import *
from PIL import Image
import time

distance_name = 'manhattan'
video = 'video2'
video_dic = {'video1':'E:\\video\\RECORD20_0127.20190101035308\\',
             'video2':'E:\\video\\RECORD21_0131.20190101010821_2\\'}
distance_method_dic = {'manhattan':manhattan,
                       'euclidean':euclidean,
                       'cosine':cosine,
                       'phash_hamming':phash_hamming}


"""以缩放后的图像，去计算距离"""

# 缩放
times_list = [0.05]
# times_list = [0.05+i*0.05 for i in range(11)]

# plt.figure(figsize=(20,12))
#
# # 开始时间
# start_time = time.time()

s=0

for times in times_list:
    image_dir = video_dic[video]
    files = glob.glob(image_dir+'*.jpg')
    dist_list = []
    for i in range(0,1750,15):
        # 15为每隔半秒
        start = cv2.imread(files[i], flags=cv2.IMREAD_GRAYSCALE)
        start = shrink(start, times)

        end = cv2.imread(files[i+1], flags=cv2.IMREAD_GRAYSCALE)
        end = shrink(end, times)
        if distance_name=='phash_hamming':
            # 使用哈希编码需将 ndarray 转成 PIL 对象
            start = Image.fromarray(start)
            end = Image.fromarray(end)
            distance = phash_hamming(start, end, hash_size=32, highfreq_factor=2)
        else:
            distance = distance_method_dic[distance_name](start, end)
        # dist_list.append(distance*(1/times)**2)
        # dist_list.append(distance/times)
        dist_list.append(distance)
        s+=distance
    # 可视化距离
    # plt.plot(range(0, len(dist_list)*15, 15), dist_list, label=f"{round(times,2)}")
    plt.plot(range(0, len(dist_list)), dist_list)
print(s)
# 结束时间
# end_time = time.time()
# print(end_time-start_time, '秒')
#
# plt.legend()
# plt.title('Distance curves with different scales')
#
# # plt.xticks(range(0, 1750))
# plt.xlabel('frame id')

# plt.savefig(f'./curve/{video}_{distance_name}_scale-0.05-0.5.png')
# plt.show()
# plt.close()


pass