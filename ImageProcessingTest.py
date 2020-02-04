from PIL import Image
import numpy as np
import os
from os import listdir
from os.path import isfile, join, splitext

path = 'data/00000001_000.png'

temppath = 'data/'

img_list = []

#function that appends the name of all files in a folder to a list
def feed_function(temppath):
    img_list = [f for f in listdir(temppath) if isfile(join(temppath, f))]

    acceptable_extensions = ['.png', '.jpg']

    for file_name in img_list:
        extension = os.path.splitext(file_name)
        if(extension[1] in acceptable_extensions):
            path = str(temppath + str(file_name))
            print(path)
            check_size(path)
            image = Image.open(path)
        else:
            pass

        #load_image(path) # set this equal to an array or something

#function that processes each image based on the pixels - three dimensional array.
def load_image(path):

    # (width, height, channels) < the order of the three dimensional array
    with Image.open(path) as image:
        im_arr = np.frombuffer(image.tobytes(), dtype=np.uint8)
        im_arr = im_arr.reshape((image.size[1], image.size[0], -1)) # this line reshapes the one dimensional array into an array of arrays

    return im_arr

def check_size(path):
    image = Image.open(path)
    if(image.size != (1024, 1024)):
        new_image = image.resize((1024, 1024))
        print(new_image.size)


print(feed_function(temppath))
