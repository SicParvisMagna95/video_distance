import argparse
from utils import *
import time

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--file', '-f',
        required=True,
        help='video file path'
    )
    parser.add_argument(
        '--frame_number','-n',
        required=True,
        type=int,
        help='number of frames to extract'
    )
    parser.add_argument(
        '--distance','-d',
        default='manhattan',
        help='distance function\n'
             'manhattan, euclidean, cosine, phash_hamming'
    )

    return parser.parse_args()


if __name__ == '__main__':

    args = get_args()
    start = time.time()
    frame_id = extract_frame(file=args.file,   # 视频文件路径
                             frame_number=args.frame_number,  # 需要抽多少帧
                             distance_name=args.distance) # 使用的距离 'manhattan', 'euclidean', 'cosine', 'phash_hamming'
    end = time.time()


    print('Finished! Cost',round(end-start,1), f'second to extract frames!')
    print(f'The extracted frames are saved at {{video_file_dir}}/{{video_name}}/extract_frame_{args.distance}')
    # 抽取的关键帧分布示意图
    plt.figure(figsize=(18,5))
    plt.plot(frame_id, [1]*len(frame_id), '.')
    plt.title('The extract frame id')
    plt.show()

