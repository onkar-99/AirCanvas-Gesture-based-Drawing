import random
import numpy as np
from matplotlib import pyplot as plt
import glob
import os
import matplotlib.figure
from PIL import Image
import cv2
from keras.models import load_model

def get_score(cat_done,x):
    score=0
    model = load_model('C:\\Users\\asus\\Desktop\\onkar\\Doodle-in-Air-main\\Model\\doodle_best(93%).h5')

    class_names=['t-shirt', 'book', 'door', 'axe', 'banana', 'donut', 'belt', 'eyeglasses', 'butterfly', 'alarm clock', 'lollipop', 'cell phone', 'scissors', 'bucket', 'basketball', 'bed', 'airplane', 'ceiling fan', 'backpack', 'apple', 'baseball bat', 'chair', 'candle', 'arm', 'bandage', 'birthday cake']
    class_names=sorted(class_names)
    print('done')
    _,idx=np.unique(x, axis=0,return_index=True)
    x=x[np.sort(idx)]
    print('done2')
    pred=model.predict(x)
    #random.shuffle(class_names)
    #predictions=class_names[:8]
    #print(predictions)
    #print(cat_done)
    predictions=[]
    print(pred)
    print(len(pred))
    print('cat done')
    print(cat_done)
    for p in pred:
        predictions.append(class_names[np.argmax(p)])
        print(predictions)
    for i in range(len(predictions)):
        if (cat_done[i] == predictions[i]):
            score+=1
    return score


    