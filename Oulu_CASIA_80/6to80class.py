import pandas as pd
import pickle
import numpy as np
from PIL import Image
import os, random as r
from keras.preprocessing import image
from PIL import Image
from os import path

def return_list(data_path, data_type):
    file_list = [file for file in os.listdir(data_path) if file.lower().endswith(data_type)]
    # print(str(len(file_list)))
    return file_list

def mk_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    return dir_path

data_save_path = mk_dir('./Oulu_CASIA80Class_NIR1/')


persons = list(os.listdir('./Oulu_CASIA80Class_NIR/'))

print(persons)

for x in persons:
    moods = list(os.listdir('./Oulu_CASIA80Class_NIR/'+x+'/'))
    pth = './Oulu_CASIA80Class_NIR/'+x+'/'
    temp1 = mk_dir(data_save_path +x)
    for y in moods:
        files = return_list(pth+y, '.jpeg')
        for imgFile in files:
            orgImg = np.asarray(image.load_img(pth+y+'/'+imgFile))
            saveImg = Image.fromarray(orgImg)
            saveImg.save(path.join(temp1 +'/'+ y + '_' + imgFile))
s           
