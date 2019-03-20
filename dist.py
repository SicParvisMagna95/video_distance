import numpy as np
import cv2
import imagehash
'''定义了一些距离函数'''
"""
:param image1: ndarray
:param image2: ndarray
:return: float64
"""

def euclidean(image1, image2):
    '''必须转为np.float,否则为opencv默认的uint8,加减会出问题'''
    minus = image1.astype(np.float)-image2.astype(np.float)
    # mean = np.mean(minus)
    # sigma = np.std(minus)
    # matrix = (minus-mean)/sigma
    return np.linalg.norm(minus,
                          ord='fro')

def manhattan(image1, image2):
    minus = image1.astype(np.float)-image2.astype(np.float)
    return np.linalg.norm(minus.flatten(),
                          ord=1)

def cosine(image1, image2):
    image1, image2 = image1.astype(np.float), image2.astype(np.float)
    distance = 1-np.sum(image1*image2)\
               /(np.linalg.norm(image1, ord='fro')*np.linalg.norm(image2, ord='fro'))
    return distance

def hamming(hash1, hash2):
    # return bin(hash1^hash2).count('1')
    return (hash1 - hash2) / len(hash1.hash) ** 2


def phash_hamming(image1, image2, hash_size=32, highfreq_factor=1):
    """
    两个参数，一起决定了图片resize的大小，最适合的才最好，按照公式：
    img_size = hash_size * highfreq_factor
    :param image1:
    :param image2:
    :param hash_size: 代表最终返回hash数值长度
    :param highfreq_factor: 代表resize的尺度
    :return: phash后的汉明距离
    """
    hash1 = imagehash.phash(image1, hash_size, highfreq_factor)
    hash2 = imagehash.phash(image2, hash_size, highfreq_factor)
    return hamming(hash1, hash2)


def averagehash_hamming():
    pass

def differencehash_hamming():
    pass

def wavelethash_hamming():
    pass














