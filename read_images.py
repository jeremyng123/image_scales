import re
import os
from fnmatch import fnmatch
import time
import cv2
import numpy as np

def walk(folder):
    for dirpath, dirnames, files in os.walk(folder):
        print(f"##################\n{dirpath}\n##################")
        # curr_family = re.split('/|\\\\', dirpath)[-1]
        return [f"{folder}\{file}" for file in files if fnmatch(file, "*.jpg")]

# https://stackoverflow.com/questions/44650888/resize-an-image-without-distortion-opencv
# This site also gave suggestions on padding to keep size constant
def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized

def mmtopx(mm):
    return int(3.7795275591 * mm)

def landscapeOrPortrait(h,w):
    if h < w: # landscape
        return None, mmtopx(99)
    else:
        return mmtopx(99), None


# specific to this event only
def get_location_of_photo(filename):
    arr = filename.split("_")
    key = arr[0]
    if key == "IMG" or  "0506" in key:
        return f"_segway_{key}"
    elif "0508" in key:
        return f"_clementi_{key}"
    elif "0512" in key:
        return f"_haircut_{key}"
    elif "0518" in key:
        return f"_movie_night_{key}"
    elif "0520" in key:
        return f"_pasta_lunch_homemade_{key}"
    elif "0521" in key:
        return f"_river_walk_{key}"
    elif "0605" in key:
        return f"_random_gym_night_and_mcd_{key}"
    elif "0610" in key:
        return f"_io_italian_osteria_{key}"
    elif "0702" in key:
        return f"_bridget_jero_early_bday_celeb_{key}"
    else:
        return f"__{key}"




def read_images(folder_name):
    folder = os.path.join(os.getcwd(), folder_name)
    images = walk(folder)
    for i,image in enumerate(images):
        img=cv2.imread(image,1)
        h,w = img.shape[:2]
        new_h, new_w = landscapeOrPortrait(h,w)
        new_img = image_resize(img, new_w, new_h)
        location = get_location_of_photo(image.split("\\")[-1])
        cv2.imwrite(f"output/{i+1}{location}.jpg", new_img)
        print(f"saved output/{i+1}{location}.jpg")

read_images("images")
