from PIL import Image
import numpy as np
from os import listdir
from os.path import isfile, join

path = 'data/00000001_000.png'

temppath = 'data/'

img_list = []

#function that appends the name of all files in a folder to a list
def feed_function():
    img_list = [f for f in listdir(temppath) if isfile(join(temppath, f))]

    for file_name in img_list:
        path = str(temppath + str(file_name))
        print(path)

        #load_image(path) # set this equal to an array or something

#function that processes each image based on the pixels - three dimensional array.
def load_image(path):

    # (width, height, channels) < the order of the three dimensional array

    with Image.open(path) as image:
        im_arr = np.frombuffer(image.tobytes(), dtype=np.uint8)
        im_arr = im_arr.reshape((image.size[1], image.size[0], -1)) # this line reshapes the one dimensional array into an array of arrays

    return im_arr

#images = load_image(path)

#print(images)

#print(len(images))

print(feed_function())
