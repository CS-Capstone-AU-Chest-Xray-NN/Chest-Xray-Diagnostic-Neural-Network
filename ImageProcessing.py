from PIL import Image
import numpy as np
import os
from os import listdir
from os.path import isfile, join, splitext

path = 'data/test.png'

temppath = "data/"

img_list = []

#Checks the size of an image, if it is not standard, it standardizes it (1024, 1024)
def check_size(path):
    image = Image.open(path)
    if(image.size != (1024, 1024)):
        new_image = image.resize((1024, 1024))
        print(new_image.size)
        return new_image
    return image

#Function to load the image into a usable array: Each individual array is a line of pixels
def load_image(image):
    im_arr = np.frombuffer(image.tobytes(), dtype=np.uint8)
    im_arr = im_arr.reshape((image.size[1], image.size[0], -1)) # this line reshapes the one dimensional array into an array of arrays
    
    return im_arr

def feed_function(temppath):
    img_list = [f for f in listdir(temppath) if isfile(join(temppath, f))]

    acceptable_extensions = ['.png', '.jpg']

    for file_name in img_list:
        extension = os.path.splitext(file_name)
        if(extension[1] in acceptable_extensions):
            path = str(temppath + str(file_name))
            arr = load_image(check_size(path))
            print(arr)
            
        else:
            pass

        #load_image(path) # set this equal to an array or something 


if __name__ == '__main__':
    feed_function(temppath)