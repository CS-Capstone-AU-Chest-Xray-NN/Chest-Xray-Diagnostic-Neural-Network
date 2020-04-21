import time

import cv2
import numpy as np
import pandas as pd

def resize_image(path):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    size = (1024, 1024)
    height, width = image.shape
    if (width, height) != size:
        resized = cv2.resize(image, size)
        return resized
    return image

if __name__ == '__main__':
    start = time.time()

    data = pd.read_csv('data/data.csv')
    images = [i for i in data['Image Index']]
    array = np.array([np.array(resize_image('data/images/{}'.format(image))) for image in images])
    np.save('data/images.npy', array)

    end = time.time()
    print('Seconds: {}'.format(round(end - start, 2)))
