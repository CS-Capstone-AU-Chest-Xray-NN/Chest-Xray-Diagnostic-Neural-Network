import cv2
import numpy as np
import pandas as pd

def resize_image(path):
    im = cv2.imread(path)
    dim = (1024, 1024)
    h, w, _ = im.shape
    if (w, h) != dim:
        resized = cv2.resize(im, dim, interpolation=cv2.INTER_CUBIC)
        return resized
    return im

if __name__ == '__main__':
    pass