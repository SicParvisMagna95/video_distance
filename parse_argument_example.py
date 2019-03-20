import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mtcnn_type",
        default='xpeng',
        help='Please choose one of the following:\noriginal\nxpeng',
    )
    parser.add_argument(
        "--input_dataset_list",
        default='/data-private/face/public_dataset/vggface2_train/vggface2data_list.txt',
        help="Input open data set directory."
    )
    parser.add_argument(
        "--input_dataset_path",
        default='/data-private/face/public_dataset/',
        help="Input open data set directory."
    )
    parser.add_argument(
        "--output_dataset_path",
        default='/data-private/face/public_dataset/vggface2_train_cropped/',
        help="Input open data set directory."
    )
    parser.add_argument(
        "--draw_visdom",
        action='store_true',
        help="Indicating whether to draw test images on visdom server")
    parser.add_argument(
        "--visdom_env",
        default='',
        help="name of visdom environment")
    parser.add_argument(
        "--p_thr",
        default='0.6',
        help='Threshold for P-Net output',
    )
    parser.add_argument(
        "--r_thr",
        default='0.7',
        help='Threshold for R-Net output',
    )
    parser.add_argument(
        "--o_thr",
        default='0.7',
        help='Threshold for O-Net output',
    )

    return parser.parse_args()





if __name__ == "__main__":
    args = get_args()
    do_something(args.mtcnn_type)
    do_something(args.output_dataset_path)
    do_something(args.p_thr)
