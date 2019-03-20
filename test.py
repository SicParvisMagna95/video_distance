import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d

from utils import *

# frame
# distribution = distance_distribution(r'E:\video\RECORD20_0127.20190101035308.mp4',
#                                      'manhattan')

file = r'E:\video\RECORD20_0127.20190101035308.mp4'
# file_dir = os.path.dirname(file)
# save_dir = os.path.join(file_dir, os.path.basename(file)[:-4], 'extract_frame')
#
# pass
frame_id = extract_frame(file)

