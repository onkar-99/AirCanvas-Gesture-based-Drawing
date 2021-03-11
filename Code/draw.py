import numpy as np
import cv2
import imutils
import time
import keyboard
import data
from PIL import Image
import random
from datetime import datetime
from matplotlib import pyplot as plt
import scores as scores
def draw_img(name,low,high):
    def nothing(x):
        pass
    #def get_category
    class_names=['t-shirt', 'book', 'door', 'axe', 'banana', 'donut', 'belt', 'eyeglasses', 'butterfly', 'alarm clock', 'lollipop', 'cell phone', 'scissors', 'bucket', 'basketball', 'bed', 'airplane', 'ceiling fan', 'backpack', 'apple', 'baseball bat', 'chair', 'candle', 'arm', 'bandage', 'birthday cake']
    def get_category():
        category=''
        category=random.choice(class_names)
        class_names.remove(category)
        return category
    def draw_box(screen):
        cv2.line(screen, (150,130), (400,130), (0,0,0), 2)
        cv2.line(screen, (150,130), (150,300), (0,0,0), 2)
        cv2.line(screen, (150,300),(400,300), (0,0,0), 2)
        cv2.line(screen, (400,300), (400,130), (0,0,0), 2)
    cate=0
    counter=0
    append=0
    n_pressed=0
    arr = np.empty([0, 64,64,1])
    once = 0
    paint = np.zeros((480, 640, 3)) + 255
    #print(len(paint))
    paint_copy = paint.copy()
    #greenLower = tuple(low)
    #greenUpper = tuple(high)
    greenLower = low
    greenUpper = high
    pts = []
    cat_done=[]
    cat=''
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    time.sleep(2.0)
    pen_down = 0
    cv2.namedWindow('Frame')
    start_time = datetime.now()
    diff = (datetime.now() - start_time).seconds
    duration=60
    while ( diff <= duration ):
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        thickness = 2
        blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, greenLower, greenUpper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        
        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            if radius > 10:
                cv2.circle(frame, (int(x), int(y)), int(radius),
                           (0, 255, 255), 2)
                cv2.circle(frame, center, 5, (0,0,0), -1)
                #cv2.circle(paint, center, 5, (255, 0, 255), -1)
                draw_box(frame)
                draw_box(paint)                
                cv2.putText(frame, '00 :{}'.format(str(diff)), (350,60), cv2.FONT_HERSHEY_SIMPLEX , 2, (0, 0, 0), 4, cv2.LINE_AA)
                cv2.putText(frame, "{}'s turn".format(name), (70,60), cv2.FONT_HERSHEY_SIMPLEX , 1, (0, 0, 0), 2, cv2.LINE_AA)
            if keyboard.is_pressed('space'):
                pen_down = 1
            if keyboard.is_pressed('b'):
                pen_down = 0
                once = 1
            if keyboard.is_pressed('d'):
                append=1
                n_pressed=0
            if append:
                append=0
                copy=paint.copy()
                plot=data.score(paint)
                if not np.array_equal(copy, plot):
                    
                    plot=plot.reshape(1,64,64,1)
                    
                    arr = np.concatenate((arr, plot), axis=0)
                #print('draw',arr.shape)
                #break  
            if cv2.waitKey(1) & 0xFF == ord('n'):
                if n_pressed:
                    pop=cat_done.pop()
                    print('Popped',pop)
                cat=get_category()
                cat_done.append(cat)
                n_pressed=1
               
                
            if cat:
                cv2.putText(frame, cat, (230,100), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,0),2)  
                
            if pen_down == 1:
                pts.append(center)
            if pen_down == 0 and once == 1:
                pts.append('b')
                once = 0
            for i in range(1, len(pts)):
                if pts[i - 1] is None or pts[i] is None:
                    continue
                if pts[i] == 'b' or pts [i-1]=='b':
                    pass
                else:
                    cv2.line(frame, pts[i - 1], pts[i], (0,0,0), thickness)
          
                    if pen_down == 1:
               
                        cv2.line(paint, pts[i - 1], pts[i], (0,0,0), thickness)
        
            if keyboard.is_pressed('c'):
                pts.clear()
                paint = cv2.bitwise_or(paint, paint_copy)
            cv2.putText(paint, "b-stop | space-start | c-clear", (80,50), 
                cv2.FONT_HERSHEY_PLAIN, 2, (0,0,0),2)
            cv2.putText(paint, "s-save | n-new object", (130,90), 
                cv2.FONT_HERSHEY_PLAIN, 2, (0,0,0),2)
            diff = (datetime.now() - start_time).seconds
        cv2.imshow("Frame", frame)
        cv2.imshow('Paint', paint)
        if keyboard.is_pressed('esc'):

            break

    cv2.destroyAllWindows()
    cap.release()
    arr /= 255.0
    np.save('Players//Player {}-draw.npy'.format(name),arr)
    np.save('Players//Player {}-categories.npy'.format(name),cat_done)
    return scores.get_score(cat_done,arr)
