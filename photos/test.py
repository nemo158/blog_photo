#coding=utf-8
import numpy as np
import matplotlib
import os
import image
 
def img_seg(dir):
    files = os.listdir(dir)
    for file in files:
        a, b = os.path.splitext(file)
        img = image.open(os.path.join(dir + "\\" + file))
        hight, width = img.size
        w = 256
        id = 1
        i = 0
        while (i + w <= hight):
            j = 0
            while (j + w <= width):
                new_img = img.crop((i, j, i + w, j + w))
                rename = "D:\nemo'space\blog_photo\photos"
                new_img.save(rename + a + "_" + str(id) + b)
                id += 1
                j += w
            i = i + w
 
 
if __name__ == '__main__':
    path = "D:\nemo'space\blog_photo\photos\"
    img_seg(path)
