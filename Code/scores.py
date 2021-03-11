import random
import numpy as np
from matplotlib import pyplot as plt
import glob
import os
import matplotlib.figure
#from keras.models import load_model
from PIL import Image
import cv2
from keras.models import load_model

def get_score(cat_done,x):
    score=0
    model = load_model('/content/doodle_best(93%).h5')

    class_names=['t-shirt', 'book', 'door', 'axe', 'banana', 'donut', 'belt', 'eyeglasses', 'butterfly', 'alarm clock', 'lollipop', 'cell phone', 'scissors', 'bucket', 'basketball', 'bed', 'airplane', 'ceiling fan', 'backpack', 'apple', 'baseball bat', 'chair', 'candle', 'arm', 'bandage', 'birthday cake']
    class_names=sorted(class_names)

    _,idx=np.unique(x, axis=0,return_index=True)
    x=x[np.sort(idx)]
    pred=model.predict(x)
    #random.shuffle(class_names)
    #predictions=class_names[:8]
    #print(predictions)
    #print(cat_done)
    predictions=[]
    for p in pred:
        predictions.append(class_names[np.argmax(p)])
        print(predictions)
    for i in range(len(cat_done)):
        if (cat_done[i] == predictions[i]):
            score+=1
    return score


    