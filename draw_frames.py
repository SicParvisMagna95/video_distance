import cv2
import os
import shutil


video_file = r'E:\video\test.mp4'
save_path = os.path.dirname(video_file) + '\\'\
            + os.path.basename(video_file)[:-4]

# 若保存路径不存在，则创建
save_path_exist = os.path.exists(save_path)
if not save_path_exist:
    os.makedirs(save_path)
    print(f"{save_path}\nis created.")

# 路径存在，抽帧开始
video = cv2.VideoCapture(video_file)

i = 0
while video.isOpened():
    ret, frame = video.read()
    print(i, ret)

    if not ret:
        print("抽帧完毕！")
        break

    # save_name = os.path.join(save_path, str(i).zfill(8) +'.jpg')
    # cv2.imwrite(save_name, frame)

    i+=1
video.release()
pass
